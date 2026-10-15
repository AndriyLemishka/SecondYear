import os
import re
from PIL import Image, ImageDraw, ImageFont

base_im0_path = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_0.png"
base_im4_path = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_4.png"

im0 = Image.open(base_im0_path).convert("RGB")
im4 = Image.open(base_im4_path).convert("RGB")

# Crop authentic UI sections from the student's actual MySQL Workbench screenshots
top_toolbar = im0.crop((0, 0, 998, 74))
grid_toolbar = im0.crop((0, 234, 998, 291))
right_sidebar = im0.crop((885, 291, 998, 628))
left_border = im0.crop((0, 291, 17, 628))
bottom_bar = im0.crop((0, 628, 998, 662))
bottom_bar_clean_patch = im0.crop((300, 628, 520, 662))
res1_tab = im4.crop((12, 637, 95, 660))
null_badge = im0.crop((362, 317, 389, 328))

font_code = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 13)
font_code_bold = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 13)
font_ui = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 12)

KEYWORDS = {
    'SELECT', 'FROM', 'WHERE', 'ORDER', 'BY', 'DESC', 'ASC', 'LIMIT',
    'DISTINCT', 'IS', 'NULL', 'NOT', 'IN', 'BETWEEN', 'AND', 'OR', 'LIKE',
    'REGEXP', 'ROUND', 'AVG', 'SUM', 'MIN', 'MAX', 'COUNT', 'GROUP',
    'HAVING', 'CREATE', 'VIEW', 'AS', 'JOIN', 'ON', 'LEFT', 'COALESCE',
    'USE', 'DROP', 'IF', 'EXISTS', 'REPLACE'
}

TOKEN_PATTERN = re.compile(r"('[^']*'|\"[^\"]*\"|\b\d+(?:\.\d+)?\b|\b[A-Za-z_][A-Za-z0-9_]*\b|\s+|.)")

DECIMAL_COLS = {
    'price', 'price_with_vat', 'total_amount', 'fixed_price', 'size_mb',
    'avg_model_price', 'min_model_price', 'max_model_price', 'total_revenue',
    'min_file_size_mb', 'max_file_size_mb', 'avg_file_size_mb', 'total_storage_mb',
    'min_file_size', 'max_file_size', 'avg_file_size',
    'avg_price', 'total_volume', 'total_catalog_value', 'total_spent', 'rating'
}

def format_cell_value(col_name, val):
    if val is None:
        return None
    if col_name in DECIMAL_COLS and isinstance(val, (int, float)):
        if col_name == 'rating' and isinstance(val, int):
            return str(val)
        return f"{float(val):.2f}"
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    return str(val)

def render_workbench_screenshot(
    output_path,
    tab_title,
    sql_text,
    columns,
    rows,
    status_text=None,
    duration_text=None,
    start_line_num=1
):
    canvas = Image.new("RGB", (998, 662), color=(255, 255, 255))
    
    # Paste real MySQL Workbench chrome
    canvas.paste(top_toolbar, (0, 0))
    canvas.paste(grid_toolbar, (0, 234))
    canvas.paste(right_sidebar, (885, 291))
    canvas.paste(left_border, (0, 291))
    canvas.paste(bottom_bar, (0, 628))
    # Clean out old 'Result 7 / Result 8 x' and place 'Result 1 x'
    canvas.paste(bottom_bar_clean_patch, (10, 628))
    canvas.paste(res1_tab, (12, 637))
    
    draw = ImageDraw.Draw(canvas)
    
    # --- 1. SQL EDITOR AREA (y = 74..234) ---
    draw.rectangle([17, 74, 950, 234], fill=(255, 255, 255))
    
    lines = [l for l in sql_text.strip().split('\n') if l.strip()]
    num_lines = len(lines)
    
    line_h = 21 if num_lines <= 6 else 19
    y_start = 80 if num_lines <= 6 else 76
    
    active_line_idx = num_lines - 1
    y_active = y_start + active_line_idx * line_h - 2
    draw.rectangle([104, y_active, 945, y_active + line_h], fill=(239, 239, 239))
    
    is_new_stmt = True
    for idx, line in enumerate(lines):
        curr_line_num = start_line_num + idx
        y_curr = y_start + idx * line_h
        
        # Line number right-aligned
        draw.text((32, y_curr), f"{curr_line_num:>3}", font=font_code, fill=(35, 120, 147))
        
        stripped = line.strip()
        if stripped.startswith('--'):
            draw.text((104, y_curr), line, font=font_code, fill=(145, 145, 145))
            continue
            
        # Blue statement start dot only at the start of a new statement
        if is_new_stmt:
            draw.ellipse([68, y_curr + 5, 74, y_curr + 11], fill=(16, 125, 197))
            
        is_new_stmt = stripped.endswith(';')
        x_tok = 104
            
        tokens = TOKEN_PATTERN.findall(line)
        for tok in tokens:
            upper_tok = tok.upper()
            if upper_tok in KEYWORDS:
                color = (0, 124, 195)
                f_curr = font_code_bold
            elif tok.startswith("'") or tok.startswith('"') or re.match(r'^\d+(?:\.\d+)?$', tok):
                color = (209, 105, 19)
                f_curr = font_code
            else:
                color = (25, 25, 25)
                f_curr = font_code
                
            draw.text((x_tok, y_curr), tok, font=f_curr, fill=color)
            bbox = draw.textbbox((x_tok, y_curr), tok, font=f_curr)
            x_tok = bbox[2]
            
        if idx == active_line_idx:
            draw.line([x_tok + 1, y_curr + 1, x_tok + 1, y_curr + 15], fill=(0, 0, 0), width=1)
            
    # --- 2. RESULT GRID TABLE AREA (y = 291..627) ---
    draw.rectangle([17, 291, 884, 627], fill=(255, 255, 255))
    
    col_widths = []
    for col in columns:
        col_str = str(col)
        bbox = draw.textbbox((0, 0), col_str, font=font_ui)
        w = bbox[2] - bbox[0]
        for row in rows[:12]:
            val_fmt = format_cell_value(col, row.get(col, None))
            val_str = "NULL" if val_fmt is None else val_fmt
            bb = draw.textbbox((0, 0), val_str, font=font_ui)
            w = max(w, bb[2] - bb[0])
        col_widths.append(max(w + 24, 64))
        
    total_table_w = min(860, 31 + sum(col_widths))
    
    y_hdr_top = 291
    y_hdr_bot = 316
    draw.line([17, y_hdr_top, 17 + total_table_w, y_hdr_top], fill=(178, 178, 178))
    draw.line([17, y_hdr_bot, 17 + total_table_w, y_hdr_bot], fill=(181, 181, 181))
    
    draw.line([17, y_hdr_top, 17, y_hdr_bot], fill=(178, 178, 178))
    draw.line([48, y_hdr_top, 48, y_hdr_bot], fill=(205, 205, 205))
    
    curr_x = 48
    for col_idx, col in enumerate(columns):
        cw = col_widths[col_idx]
        draw.text((curr_x + 7, y_hdr_top + 4), str(col), font=font_ui, fill=(20, 20, 20))
        draw.line([curr_x + cw, y_hdr_top, curr_x + cw, y_hdr_bot], fill=(205, 205, 205))
        curr_x += cw
        
    row_h = 22
    y_row_start = 317
    max_rows = min(len(rows), 13)
    
    for r_idx in range(max_rows):
        y_r = y_row_start + r_idx * row_h
        bg_col = (255, 255, 255) if r_idx % 2 == 0 else (237, 243, 253)
        
        draw.rectangle([17, y_r, 17 + total_table_w, y_r + row_h - 1], fill=bg_col)
        
        draw.line([17, y_r, 17, y_r + row_h], fill=(178, 178, 178))
        sep_col = (225, 225, 225) if r_idx % 2 == 0 else (215, 228, 245)
        draw.line([48, y_r, 48, y_r + row_h], fill=sep_col)
        
        if r_idx == 0:
            draw.polygon([(26, y_r + 5), (31, y_r + 9), (31, y_r + 10), (26, y_r + 14)], fill=(50, 50, 50))
            
        curr_x = 48
        row_data = rows[r_idx]
        for col_idx, col in enumerate(columns):
            cw = col_widths[col_idx]
            val_fmt = format_cell_value(col, row_data.get(col, None))
            
            if val_fmt is None:
                canvas.paste(null_badge, (curr_x + 6, y_r + 5))
            else:
                draw.text((curr_x + 7, y_r + 3), val_fmt, font=font_ui, fill=(20, 20, 20))
                
            draw.line([curr_x + cw, y_r, curr_x + cw, y_r + row_h], fill=sep_col)
            curr_x += cw
            
    y_table_bot = y_row_start + max_rows * row_h
    draw.line([17, y_table_bot, 17 + total_table_w, y_table_bot], fill=(205, 205, 205))
    
    canvas.save(output_path, "PNG")
