import os
import math
from PIL import Image, ImageDraw, ImageFont

def render_marketplace_diagram():
    # Canvas setup matching DbDesigner export
    width = 1860
    height = 870
    bg_color = (248, 248, 249) # #F8F8F9
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Fonts
    font_path_bold = "C:\\Windows\\Fonts\\arialbd.ttf"
    font_path_regular = "C:\\Windows\\Fonts\\arial.ttf"
    font_path_italic = "C:\\Windows\\Fonts\\ariali.ttf"
    
    font_header = ImageFont.truetype(font_path_bold, 17)
    font_pk = ImageFont.truetype(font_path_bold, 14)
    font_row = ImageFont.truetype(font_path_regular, 14)
    font_type = ImageFont.truetype(font_path_regular, 13)
    font_watermark = ImageFont.truetype(font_path_italic, 14)

    # Colors
    c_blue = (51, 130, 201)        # #3382C9
    c_pk_bg = (173, 181, 189)      # #ADB5BD
    c_row_bg = (255, 255, 255)
    c_border = (220, 224, 230)
    c_text_dark = (33, 37, 41)
    c_text_row = (60, 64, 67)
    c_text_type = (108, 117, 125)
    c_watermark = (160, 174, 192)

    # Tables definition
    # (name, x, y, width, [ (field, type, is_pk, is_fk) ])
    tables = {
        "buyer": {
            "x": 80, "y": 70, "w": 320,
            "fields": [
                ("id_buyer", "integer", True, False),
                ("email", "varchar", False, False),
                ("registration_date", "date", False, False)
            ]
        },
        "cart": {
            "x": 80, "y": 270, "w": 320,
            "fields": [
                ("id_cart", "integer", True, False),
                ("id_buyer", "integer", False, True),
                ("status", "varchar", False, False),
                ("total_amount", "decimal", False, False),
                ("created_date", "date", False, False)
            ]
        },
        "cart_item": {
            "x": 80, "y": 550, "w": 320,
            "fields": [
                ("id_item", "integer", True, False),
                ("id_cart", "integer", False, True),
                ("id_model", "integer", False, True),
                ("fixed_price", "decimal", False, False)
            ]
        },
        "seller": {
            "x": 520, "y": 70, "w": 320,
            "fields": [
                ("id_seller", "integer", True, False),
                ("nickname", "varchar", False, False),
                ("rating", "decimal", False, False)
            ]
        },
        "review": {
            "x": 520, "y": 290, "w": 320,
            "fields": [
                ("id_review", "integer", True, False),
                ("id_model", "integer", False, True),
                ("id_buyer", "integer", False, True),
                ("rating", "integer", False, False),
                ("comment_text", "varchar", False, False)
            ]
        },
        "category": {
            "x": 960, "y": 70, "w": 320,
            "fields": [
                ("id_category", "integer", True, False),
                ("name", "varchar", False, False)
            ]
        },
        "model_3d": {
            "x": 960, "y": 250, "w": 320,
            "fields": [
                ("id_model", "integer", True, False),
                ("id_seller", "integer", False, True),
                ("id_category", "integer", False, True),
                ("id_license", "integer", False, True),
                ("name", "varchar", False, False),
                ("description", "varchar", False, False),
                ("price", "decimal", False, False),
                ("polygon_count", "integer", False, False),
                ("has_texture", "varchar", False, False)
            ]
        },
        "model_file": {
            "x": 960, "y": 640, "w": 320,
            "fields": [
                ("id_file", "integer", True, False),
                ("id_model", "integer", False, True),
                ("format", "varchar", False, False),
                ("size_mb", "decimal", False, False)
            ]
        },
        "license": {
            "x": 1400, "y": 250, "w": 330,
            "fields": [
                ("id_license", "integer", True, False),
                ("id_change", "integer", False, False),
                ("license_name", "varchar", False, False),
                ("usage_type", "varchar", False, False),
                ("allow_modification", "varchar", False, False),
                ("creation_date", "date", False, False),
                ("creation_time", "time", False, False)
            ]
        }
    }

    header_h = 50
    row_h = 30

    ports = {}
    table_boxes = {}

    for tname, tinfo in tables.items():
        tx, ty, tw = tinfo["x"], tinfo["y"], tinfo["w"]
        total_h = header_h + len(tinfo["fields"]) * row_h
        table_boxes[tname] = (tx, ty, tw, total_h)

        for fidx, (fname, ftype, is_pk, is_fk) in enumerate(tinfo["fields"]):
            row_y = ty + header_h + fidx * row_h + row_h / 2
            ports[(tname, fname, "left")] = (tx, row_y)
            ports[(tname, fname, "right")] = (tx + tw, row_y)

    # Relationships definition
    relationships = [
        # 1. cart.id_buyer -> buyer.id_buyer (left to left, inner track)
        {
            "src": ("cart", "id_buyer", "left"),
            "tgt": ("buyer", "id_buyer", "left"),
            "c1_dx": -45, "c1_dy": 0,
            "c2_dx": -45, "c2_dy": 0
        },
        # 2. cart_item.id_cart -> cart.id_cart (left to left, outer track)
        {
            "src": ("cart_item", "id_cart", "left"),
            "tgt": ("cart", "id_cart", "left"),
            "c1_dx": -65, "c1_dy": 0,
            "c2_dx": -65, "c2_dy": 0
        },
        # 3. cart_item.id_model -> model_3d.id_model (right to left, through open space below review)
        {
            "src": ("cart_item", "id_model", "right"),
            "tgt": ("model_3d", "id_model", "left"),
            "c1_dx": 240, "c1_dy": 20,
            "c2_dx": -200, "c2_dy": 170
        },
        # 4. review.id_buyer -> buyer.id_buyer (left to right)
        {
            "src": ("review", "id_buyer", "left"),
            "tgt": ("buyer", "id_buyer", "right"),
            "c1_dx": -55, "c1_dy": -60,
            "c2_dx": 55, "c2_dy": 60
        },
        # 5. review.id_model -> model_3d.id_model (right to left)
        {
            "src": ("review", "id_model", "right"),
            "tgt": ("model_3d", "id_model", "left"),
            "c1_dx": 60, "c1_dy": -25,
            "c2_dx": -60, "c2_dy": 25
        },
        # 6. model_3d.id_seller -> seller.id_seller (left to right)
        {
            "src": ("model_3d", "id_seller", "left"),
            "tgt": ("seller", "id_seller", "right"),
            "c1_dx": -65, "c1_dy": -50,
            "c2_dx": 65, "c2_dy": 50
        },
        # 7. model_3d.id_category -> category.id_category (left to left)
        {
            "src": ("model_3d", "id_category", "left"),
            "tgt": ("category", "id_category", "left"),
            "c1_dx": -45, "c1_dy": -40,
            "c2_dx": -45, "c2_dy": 40
        },
        # 8. model_3d.id_license -> license.id_license (right to left)
        {
            "src": ("model_3d", "id_license", "right"),
            "tgt": ("license", "id_license", "left"),
            "c1_dx": 55, "c1_dy": -25,
            "c2_dx": -55, "c2_dy": 25
        },
        # 9. model_file.id_model -> model_3d.id_model (left to left)
        {
            "src": ("model_file", "id_model", "left"),
            "tgt": ("model_3d", "id_model", "left"),
            "c1_dx": -85, "c1_dy": -70,
            "c2_dx": -85, "c2_dy": 90
        }
    ]

    # Helper: draw smooth bezier curve
    def draw_bezier(p0, p1, p2, p3, steps=120):
        points = []
        for i in range(steps + 1):
            t = i / steps
            u = 1 - t
            x = (u**3)*p0[0] + 3*(u**2)*t*p1[0] + 3*u*(t**2)*p2[0] + (t**3)*p3[0]
            y = (u**3)*p0[1] + 3*(u**2)*t*p1[1] + 3*u*(t**2)*p2[1] + (t**3)*p3[1]
            points.append((x, y))
        for i in range(len(points) - 1):
            draw.line([points[i], points[i+1]], fill=c_blue, width=2)

    # 1. DRAW RELATIONSHIPS FIRST
    for rel in relationships:
        s_table, s_field, s_side = rel["src"]
        t_table, t_field, t_side = rel["tgt"]

        p0 = ports[(s_table, s_field, s_side)]
        p3 = ports[(t_table, t_field, t_side)]

        p1 = (p0[0] + rel["c1_dx"], p0[1] + rel["c1_dy"])
        p2 = (p3[0] + rel["c2_dx"], p3[1] + rel["c2_dy"])

        draw_bezier(p0, p1, p2, p3)

        # Draw circle at start (FK)
        r_circ = 3.5
        draw.ellipse([p0[0]-r_circ, p0[1]-r_circ, p0[0]+r_circ, p0[1]+r_circ], fill=c_blue)

        # Draw triangle arrowhead at end (PK)
        aw = 9
        ah = 5.5
        if t_side == "left":
            tri = [p3, (p3[0] - aw, p3[1] - ah), (p3[0] - aw, p3[1] + ah)]
        else:
            tri = [p3, (p3[0] + aw, p3[1] - ah), (p3[0] + aw, p3[1] + ah)]
        draw.polygon(tri, fill=c_blue)

    # 2. DRAW TABLES
    for tname, tinfo in tables.items():
        tx, ty, tw = tinfo["x"], tinfo["y"], tinfo["w"]
        fields = tinfo["fields"]
        total_h = header_h + len(fields) * row_h

        # Table subtle shadow
        shadow_rect = [tx + 1, ty + 1, tx + tw + 2, ty + total_h + 2]
        draw.rectangle(shadow_rect, fill=(235, 237, 240))

        # Main table container
        table_rect = [tx, ty, tx + tw, ty + total_h]
        draw.rectangle(table_rect, fill=c_row_bg, outline=c_border, width=1)

        # Header
        header_rect = [tx, ty, tx + tw, ty + header_h]
        draw.rectangle(header_rect, fill=c_blue)

        # Header Text (centered)
        h_bbox = draw.textbbox((0, 0), tname, font=font_header)
        hw = h_bbox[2] - h_bbox[0]
        hh = h_bbox[3] - h_bbox[1]
        draw.text((tx + (tw - hw)/2, ty + (header_h - hh)/2 - 2), tname, fill=(255, 255, 255), font=font_header)

        # Rows
        for fidx, (fname, ftype, is_pk, is_fk) in enumerate(fields):
            curr_y = ty + header_h + fidx * row_h
            row_rect = [tx, curr_y, tx + tw, curr_y + row_h]

            if is_pk:
                draw.rectangle(row_rect, fill=c_pk_bg)
                f_font = font_pk
                t_font = font_pk
                fn_color = c_text_dark
                ft_color = c_text_dark
            else:
                draw.rectangle(row_rect, fill=c_row_bg)
                f_font = font_row
                t_font = font_type
                fn_color = c_text_row
                ft_color = c_text_type
                # bottom line separator
                draw.line([(tx, curr_y + row_h), (tx + tw, curr_y + row_h)], fill=c_border, width=1)

            # Field Name (left-aligned)
            fn_bbox = draw.textbbox((0, 0), fname, font=f_font)
            fn_h = fn_bbox[3] - fn_bbox[1]
            draw.text((tx + 14, curr_y + (row_h - fn_h)/2 - 1), fname, fill=fn_color, font=f_font)

            # Field Type (right-aligned)
            ft_bbox = draw.textbbox((0, 0), ftype, font=t_font)
            ft_w = ft_bbox[2] - ft_bbox[0]
            ft_h = ft_bbox[3] - ft_bbox[1]
            draw.text((tx + tw - 14 - ft_w, curr_y + (row_h - ft_h)/2 - 1), ftype, fill=ft_color, font=t_font)

    # 3. WATERMARK
    draw.text((20, height - 28), "Generated with erd.dbdesigner.net", fill=c_watermark, font=font_watermark)

    # Save image in Лаб 2
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "DbDesigner_Marketplace.png")
    img.save(out_path, format="PNG")
    print(f"Successfully generated {out_path} ({width}x{height})")

if __name__ == "__main__":
    render_marketplace_diagram()
