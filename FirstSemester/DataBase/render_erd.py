import json
import math
import os
from PIL import Image, ImageDraw, ImageFont

def render_diagram():
    with open("Завд2_Лаб1.erdplus", encoding="utf-8") as f:
        data = json.load(f)

    nodes = data["data"]["nodes"]
    edges = data["data"]["edges"]

    font_path = "C:\\Windows\\Fonts\\arial.ttf"
    font_main = ImageFont.truetype(font_path, 15)
    font_bold = ImageFont.truetype(font_path, 15)
    font_small = ImageFont.truetype(font_path, 13)

    # Map node positions
    entities = {}
    attributes = {}
    relationships = {}

    for n in nodes:
        t = n["type"]
        nid = n["id"]
        if t == "Entity":
            entities[nid] = {
                "id": nid,
                "label": n["data"]["label"],
                "x": n["position"]["x"],
                "y": n["position"]["y"],
                "w": 130,
                "h": 54
            }
        elif t == "Relationship":
            relationships[nid] = {
                "id": nid,
                "label": n["data"]["label"],
                "x": n["position"]["x"],
                "y": n["position"]["y"],
                "w": 120,
                "h": 60,
                "data": n["data"]
            }

    for n in nodes:
        if n["type"] == "Attribute":
            nid = n["id"]
            pid = n["parentId"]
            parent = entities[pid]
            abs_x = parent["x"] + n["position"]["x"]
            abs_y = parent["y"] + n["position"]["y"]
            is_pk = bool(n["data"].get("types") and n["data"]["types"].get("Unique"))
            lbl = n["data"]["label"]
            bbox = font_small.getbbox(lbl)
            lbl_w = bbox[2] - bbox[0]
            att_w = max(120, lbl_w + 24)
            attributes[nid] = {
                "id": nid,
                "label": lbl,
                "parentId": pid,
                "x": abs_x,
                "y": abs_y,
                "w": att_w,
                "h": 46,
                "is_pk": is_pk
            }

    # Determine canvas bounds
    all_x = []
    all_y = []
    for d in list(entities.values()) + list(attributes.values()) + list(relationships.values()):
        all_x.extend([d["x"] - d["w"]/2, d["x"] + d["w"]/2])
        all_y.extend([d["y"] - d["h"]/2, d["y"] + d["h"]/2])

    pad = 120
    min_x = min(all_x) - pad
    min_y = min(all_y) - pad
    max_x = max(all_x) + pad
    max_y = max(all_y) + pad

    width = int(max_x - min_x)
    height = int(max_y - min_y)

    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    def tx(x):
        return x - min_x
    def ty(y):
        return y - min_y

    # 1. Draw Edges
    for e in edges:
        if e["type"] == "Attribute":
            ent = entities[e["source"]]
            att = attributes[e["target"]]
            x1, y1 = tx(ent["x"]), ty(ent["y"])
            x2, y2 = tx(att["x"]), ty(att["y"])
            draw.line([(x1, y1), (x2, y2)], fill="#555555", width=1)

        elif e["type"] == "Relationship":
            rel = relationships[e["source"]]
            ent = entities[e["target"]]
            x1, y1 = tx(rel["x"]), ty(rel["y"])
            x2, y2 = tx(ent["x"]), ty(ent["y"])
            draw.line([(x1, y1), (x2, y2)], fill="#222222", width=2)

            # Draw Martin cardinality notation
            card = e["data"]["maxCardinality"] # 'One' or 'Many'
            dx = x1 - x2
            dy = y1 - y2
            dist = math.hypot(dx, dy)
            if dist > 0:
                ux = dx / dist
                uy = dy / dist
                # point near entity edge
                px = x2 + ux * 68
                py = y2 + uy * 68
                nx = -uy
                ny = ux
                if card == "One":
                    # double vertical slash for (1,1)
                    draw.line([(px - nx*9, py - ny*9), (px + nx*9, py + ny*9)], fill="#222222", width=2)
                    px2 = px + ux * 8
                    py2 = py + uy * 8
                    draw.line([(px2 - nx*9, py2 - ny*9), (px2 + nx*9, py2 + ny*9)], fill="#222222", width=2)
                elif card == "Many":
                    # crow's foot
                    draw.line([(px - nx*9, py - ny*9), (px + nx*9, py + ny*9)], fill="#222222", width=2)
                    tip_x = x2 + ux * 55
                    tip_y = y2 + uy * 55
                    base_x = px + ux * 16
                    base_y = py + uy * 16
                    draw.line([(tip_x, tip_y), (base_x - nx*10, base_y - ny*10)], fill="#222222", width=2)
                    draw.line([(tip_x, tip_y), (base_x + nx*10, base_y + ny*10)], fill="#222222", width=2)

    # 2. Draw Relationships (Diamonds)
    for r in relationships.values():
        cx, cy = tx(r["x"]), ty(r["y"])
        hw, hh = r["w"] / 2, r["h"] / 2
        pts = [(cx, cy - hh), (cx + hw, cy), (cx, cy + hh), (cx - hw, cy)]
        draw.polygon(pts, fill="white", outline="#222222", width=2)
        
        # text
        bbox = draw.textbbox((0, 0), r["label"], font=font_small)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((cx - tw/2, cy - th/2 - 2), r["label"], fill="#111111", font=font_small)

    # 3. Draw Entities (Rectangles)
    for ent in entities.values():
        cx, cy = tx(ent["x"]), ty(ent["y"])
        hw, hh = ent["w"] / 2, ent["h"] / 2
        rect = [(cx - hw, cy - hh), (cx + hw, cy + hh)]
        draw.rectangle(rect, fill="#FAFAFA", outline="#111111", width=2)

        bbox = draw.textbbox((0, 0), ent["label"], font=font_bold)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((cx - tw/2, cy - th/2 - 2), ent["label"], fill="#000000", font=font_bold)

    # 4. Draw Attributes (Ellipses)
    for att in attributes.values():
        cx, cy = tx(att["x"]), ty(att["y"])
        hw, hh = att["w"] / 2, att["h"] / 2
        ellipse = [(cx - hw, cy - hh), (cx + hw, cy + hh)]
        draw.ellipse(ellipse, fill="white", outline="#333333", width=1)

        label = att["label"]
        bbox = draw.textbbox((0, 0), label, font=font_small)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        lx = cx - tw / 2
        ly = cy - th / 2 - 1
        draw.text((lx, ly), label, fill="#111111", font=font_small)

        if att["is_pk"]:
            # Underline primary key
            draw.line([(lx, ly + th + 2), (lx + tw, ly + th + 2)], fill="#111111", width=1)

    out_path = os.path.abspath("Schema.png")
    img.save(out_path, format="PNG")
    print(f"Successfully rendered Schema.png: {width}x{height} pixels to {out_path}!")

    lab1_schema = os.path.join("Лаб 1", "Schema.png")
    if os.path.exists("Лаб 1"):
        img.save(lab1_schema, format="PNG")
        print(f"Saved copy to {lab1_schema}!")

if __name__ == "__main__":
    render_diagram()
