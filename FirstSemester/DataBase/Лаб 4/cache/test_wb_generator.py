import os
import re
from PIL import Image, ImageDraw, ImageFont
import numpy as np

base_im0_path = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_0.png"
base_im4_path = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_4.png"

im0 = Image.open(base_im0_path).convert("RGB")
im4 = Image.open(base_im4_path).convert("RGB")

# Crop reusable real UI assets from im0 and im4
# 1. Top bar + toolbar (y=0..74)
top_toolbar = im0.crop((0, 0, 998, 74))

# 2. Result Grid toolbar (y=234..291)
grid_toolbar = im0.crop((0, 234, 998, 291))

# 3. Right vertical sidebar (x=885..998, y=291..628)
right_sidebar = im0.crop((885, 291, 998, 628))

# 4. Left border (x=0..17, y=291..628)
left_border = im0.crop((0, 291, 17, 628))

# 5. Bottom bar (y=628..662)
bottom_bar = im0.crop((0, 628, 998, 662))

# 6. 'Result 1 x' tab from im4 (x=12..85, y=637..660)
res1_tab = im4.crop((12, 637, 95, 660))

# 7. NULL badge from im0 (x=362..389, y=317..328)
null_badge = im0.crop((362, 317, 389, 328))

# Fonts
font_code = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 13)
font_code_bold = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 13)
font_ui = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 12)
font_ui_bold = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 12)

KEYWORDS = {
    'SELECT', 'FROM', 'WHERE', 'ORDER', 'BY', 'DESC', 'ASC', 'LIMIT',
    'DISTINCT', 'IS', 'NULL', 'NOT', 'IN', 'BETWEEN', 'AND', 'OR', 'LIKE',
    'REGEXP', 'ROUND', 'AVG', 'SUM', 'MIN', 'MAX', 'COUNT', 'GROUP',
    'HAVING', 'CREATE', 'VIEW', 'AS', 'JOIN', 'ON', 'LEFT', 'COALESCE',
    'USE', 'DROP', 'IF', 'EXISTS'
}

def generate_workbench_image(sql_text, columns, rows, start_line_num=1):
    # Base image from im0
    canvas = Image.new("RGB", (998, 662), color=(255, 255, 255))
    
    # Paste fixed UI chrome
    canvas.paste(top_toolbar, (0, 0))
    canvas.paste(grid_toolbar, (0, 234))
    canvas.paste(right_sidebar, (885, 291))
    canvas.paste(left_border, (0, 291))
    canvas.paste(bottom_bar, (0, 628))
    # Replace Result 8 tab with Result 1 tab
    canvas.paste(res1_tab, (12, 637))
    
    draw = ImageDraw.Draw(canvas)
    
    # --- SQL EDITOR (y = 74..234) ---
    # Clear editor area
    draw.rectangle([17, 74, 950, 234], fill=(255, 255, 255))
    
    lines = sql_text.strip().split('\n')
    num_lines = len(lines)
    
    # Calculate line positions
    y_start = 82
    line_h = 22
    
    # Highlight active line (the last non-empty line of the query)
    active_line_idx = num_lines - 1
    y_active = y_start + active_line_idx * line_h - 3
    draw.rectangle([104, y_active, 945, y_active + line_h], fill=(239, 239, 239))
    
    first_stmt_line = True
    for idx, line in enumerate(lines):
        curr_line_num = start_line_num + idx
        y_curr = y_start + idx * line_h
        
        # Line number (right-aligned at x=52 in blue-teal)
        draw.text((32, y_curr), f"{curr_line_num:>3}", font=font_code, fill=(35, 120, 147))
        
        # Blue statement dot on lines that begin statements
        if not line.strip().startswith('--') and (first_stmt_line or line.strip().startswith(('SELECT', 'USE', 'CREATE', 'DROP'))):
            # Blue circle dot at x=70
            draw.ellipse([68, y_curr + 4, 74, y_curr + 10], fill=(16, 125, 197))
            if not line.strip().startswith('USE'):
                first_stmt_line = False
                
        # Tokenize line
        x_tok = 104
        if line.strip().startswith('--'):
            # Comment
            draw.text((x_tok, y_curr), line, font=font_code, fill=(150, 150, 150))
            continue
            
        tokens = re.split(r'(\s+|[(),;*+\-])', line)
        for tok in tokens:
            if not tok:
                continue
            upper_tok = tok.upper()
            
            if upper_tok in KEYWORDS:
                color = (0, 124, 195)
                f_curr = font_code_bold
            elif tok.startswith("'") or tok.startswith('"') or tok.isdigit() or re.match(r'^\d+(\.\d+)?$', tok):
                color = (209, 105, 19)
                f_curr = font_code
            else:
                color = (25, 25, 25)
                f_curr = font_code
                
            draw.text((x_tok, y_curr), tok, font=f_curr, fill=color)
            bbox = draw.textbbox((x_tok, y_curr), tok, font=f_curr)
            x_tok = bbox[2]
            
        # Draw blinking cursor '|' at the end of active line
        if idx == active_line_idx:
            draw.line([x_tok + 1, y_curr + 1, x_tok + 1, y_curr + 14], fill=(0, 0, 0), width=1)
            
    # --- RESULT GRID TABLE (y = 291..628) ---
    # Clear middle table area
    draw.rectangle([17, 291, 884, 627], fill=(255, 255, 255))
    
    # Calculate column widths
    col_widths = []
    for col in columns:
        # Measure max width
        col_str = str(col)
        bbox = draw.textbbox((0, 0), col_str, font=font_ui)
        w = bbox[2] - bbox[0]
        for row in rows[:10]:
            val_str = str(row.get(col, ""))
            bb = draw.textbbox((0, 0), val_str, font=font_ui)
            w = max(w, bb[2] - bb[0])
        col_widths.append(max(w + 24, 65))
        
    total_table_w = 31 + sum(col_widths) # 31 is indicator column
    
    # Top border of table
    y_hdr_top = 291
    y_hdr_bot = 316
    draw.line([17, y_hdr_top, 17 + total_table_w, y_hdr_top], fill=(178, 178, 178))
    draw.line([17, y_hdr_bot, 17 + total_table_w, y_hdr_bot], fill=(181, 181, 181))
    
    # Left indicator column header (empty)
    draw.line([17, y_hdr_top, 17, y_hdr_bot], fill=(178, 178, 178))
    draw.line([48, y_hdr_top, 48, y_hdr_bot], fill=(205, 205, 205))
    
    # Column headers
    curr_x = 48
    for col_idx, col in enumerate(columns):
        cw = col_widths[col_idx]
        draw.text((curr_x + 7, y_hdr_top + 4), str(col), font=font_ui, fill=(20, 20, 20))
        draw.line([curr_x + cw, y_hdr_top, curr_x + cw, y_hdr_bot], fill=(205, 205, 205))
        curr_x += cw
        
    # Table rows
    row_h = 22
    y_row_start = 317
    
    max_rows = min(len(rows), 13)
    for r_idx in range(max_rows):
        y_r = y_row_start + r_idx * row_h
        bg_col = (255, 255, 255) if r_idx % 2 == 0 else (237, 243, 253)
        
        # Row background
        draw.rectangle([17, y_r, 17 + total_table_w, y_r + row_h - 1], fill=bg_col)
        
        # Left indicator column border
        draw.line([17, y_r, 17, y_r + row_h], fill=(178, 178, 178))
        draw.line([48, y_r, 48, y_r + row_h], fill=(225, 225, 225) if r_idx % 2 == 0 else (210, 225, 245))
        
        # First row indicator arrow ▶
        if r_idx == 0:
            draw.polygon([(26, y_r + 5), (31, y_r + 9), (31, y_r + 10), (26, y_r + 14)], fill=(50, 50, 50))
            
        # Cell data
        curr_x = 48
        row_data = rows[r_idx]
        for col_idx, col in enumerate(columns):
            cw = col_widths[col_idx]
            val = row_data.get(col, None)
            
            if val is None:
                # Paste real NULL badge!
                canvas.paste(null_badge, (curr_x + 6, y_r + 4))
            else:
                val_str = str(val)
                draw.text((curr_x + 7, y_r + 3), val_str, font=font_ui, fill=(20, 20, 20))
                
            # Vertical column separator line
            draw.line([curr_x + cw, y_r, curr_x + cw, y_r + row_h], fill=(225, 225, 225) if r_idx % 2 == 0 else (210, 225, 245))
            curr_x += cw
            
    # Bottom border of table
    y_table_bot = y_row_start + max_rows * row_h
    draw.line([17, y_table_bot, 17 + total_table_w, y_table_bot], fill=(205, 205, 205))
    
    return canvas

# Test generating shot_1_1
test_sql = """USE marketplace_3d;
-- Запит 1.1: Вибірка каталогу моделей
SELECT id_model, name, price, polygon_count, has_texture 
FROM model_3d 
LIMIT 6;"""

test_cols = ['id_model', 'name', 'price', 'polygon_count', 'has_texture']
test_rows = [
    {'id_model': 1, 'name': 'Cyberpunk Character', 'price': 25.0, 'polygon_count': 150000, 'has_texture': 'Yes'},
    {'id_model': 2, 'name': 'Sports Car', 'price': 15.0, 'polygon_count': 25000, 'has_texture': 'Yes'},
    {'id_model': 3, 'name': 'Assault Rifle', 'price': 10.0, 'polygon_count': 8000, 'has_texture': 'Yes'},
    {'id_model': 4, 'name': 'Forest Terrain', 'price': 0.01, 'polygon_count': 500000, 'has_texture': 'No'},
    {'id_model': 5, 'name': 'Wooden Barrel', 'price': 5.0, 'polygon_count': 1200, 'has_texture': 'Yes'},
    {'id_model': 6, 'name': 'Wolf Animation', 'price': 30.0, 'polygon_count': 45000, 'has_texture': 'Yes'}
]

out = generate_workbench_image(test_sql, test_cols, test_rows, start_line_num=42)
out.save(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\test_shot_1_1.png")
print("Saved test_shot_1_1.png successfully!")
