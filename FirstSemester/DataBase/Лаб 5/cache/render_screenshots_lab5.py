import os
import re
import random
from PIL import Image, ImageDraw, ImageFont

base_dir = r"Лаб 5\cache"
base_im0_path = os.path.join(base_dir, r"lab3_imgs\img_0.png")
base_im4_path = os.path.join(base_dir, r"lab3_imgs\img_4.png")

im0 = Image.open(base_im0_path).convert("RGB")
im4 = Image.open(base_im4_path).convert("RGB")

top_toolbar = im0.crop((0, 0, 998, 74))
grid_toolbar = im0.crop((0, 234, 998, 291))
right_sidebar_src = im0.crop((885, 291, 998, 628))
null_badge = im0.crop((362, 317, 389, 328))

font_code = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 13)
font_code_bold = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 13)
font_ui = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 12)

KEYWORDS = {
    'SELECT', 'FROM', 'WHERE', 'ORDER', 'BY', 'DESC', 'ASC', 'LIMIT',
    'DISTINCT', 'IS', 'NULL', 'NOT', 'IN', 'BETWEEN', 'AND', 'OR', 'LIKE',
    'REGEXP', 'ROUND', 'AVG', 'SUM', 'MIN', 'MAX', 'COUNT', 'GROUP',
    'HAVING', 'CREATE', 'VIEW', 'AS', 'JOIN', 'ON', 'LEFT', 'RIGHT',
    'INNER', 'OUTER', 'CROSS', 'UNION', 'ALL', 'INTERSECT', 'EXCEPT',
    'CASE', 'WHEN', 'THEN', 'ELSE', 'END', 'EXISTS', 'COALESCE',
    'USE', 'DROP', 'IF', 'TABLE', 'UPDATE', 'SET', 'PARTITION',
    'PARTITIONS', 'RANGE', 'LIST', 'HASH', 'VALUES', 'LESS', 'THAN',
    'MAXVALUE', 'YEAR', 'EXPLAIN', 'INFORMATION_SCHEMA'
}

TOKEN_PATTERN = re.compile(r"('[^']*'|\"[^\"]*\"|\b\d+(?:\.\d+)?\b|\b[A-Za-z_][A-Za-z0-9_]*\b|\s+|.)")

DECIMAL_COLS = {
    'price', 'price_diff', 'avg_cat_price', 'total_amount', 'fixed_price',
    'sale_price', 'with_vat', 'final_price', 'val', 'rating', 'size_mb'
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
    lines = [l for l in sql_text.rstrip().split('\n')]
    if not lines or not any(l.strip() for l in lines):
        lines = [sql_text.strip()]
    num_lines = len(lines)
    
    # Base window dimensions before human crop
    base_w = random.choice([960, 980, 998, 1015, 1030, 975, 990])
    editor_pad = random.choice([8, 14, 20, 26, 34])
    
    line_h = 20
    y_start = 78
    editor_bottom = max(135, y_start + num_lines * line_h + editor_pad)
    
    y_grid = editor_bottom
    grid_h = 57
    y_tbl_hdr = y_grid + grid_h
    hdr_h = 25
    y_rows = y_tbl_hdr + hdr_h
    row_h = 22
    
    total_available = len(rows)
    if total_available == 0:
        max_rows = 0
    elif total_available <= 2:
        max_rows = total_available
    elif total_available in [3, 4]:
        max_rows = random.choice([min(total_available, 3), total_available])
    else:
        max_rows = random.choice([3, 4, 4, 5, 5, 6])
        max_rows = min(max_rows, total_available)
        
    base_h = y_rows + max_rows * row_h + 30
    
    # Outer padding for realistic human snip bounding box
    pad_left = 18
    pad_top = 22
    pad_right = 20
    pad_bottom = 45
    
    full_w = base_w + pad_left + pad_right
    full_h = base_h + pad_top + pad_bottom
    
    # Background frame simulating Windows desktop / outer window frame
    frame_bg = random.choice([(238, 239, 242), (232, 233, 236), (242, 243, 245)])
    full_canvas = Image.new("RGB", (full_w, full_h), color=frame_bg)
    draw_full = ImageDraw.Draw(full_canvas)
    
    # Top menu bar simulation (File Edit View...)
    draw_full.rectangle([pad_left, pad_top - 18, pad_left + base_w, pad_top], fill=(245, 245, 247))
    draw_full.line([pad_left, pad_top - 1, pad_left + base_w, pad_top - 1], fill=(215, 215, 218))
    
    # Workbench window canvas
    wb_canvas = Image.new("RGB", (base_w, base_h), color=(255, 255, 255))
    draw_wb = ImageDraw.Draw(wb_canvas)
    
    # 1. Top toolbar
    split_x = min(base_w - 113, 885)
    wb_canvas.paste(im0.crop((0, 0, split_x, 74)), (0, 0))
    if base_w - 113 > split_x:
        for x in range(split_x, base_w - 113):
            for y in range(74):
                wb_canvas.putpixel((x, y), (231, 231, 232))
    wb_canvas.paste(im0.crop((885, 0, 998, 74)), (base_w - 113, 0))
    
    # 2. Grid toolbar
    wb_canvas.paste(grid_toolbar.crop((0, 0, split_x, 57)), (0, y_grid))
    if base_w - 113 > split_x:
        for x in range(split_x, base_w - 113):
            for y in range(y_grid, y_grid + 57):
                wb_canvas.putpixel((x, y), (240, 240, 240))
    wb_canvas.paste(grid_toolbar.crop((885, 0, 998, 57)), (base_w - 113, y_grid))
    
    # 3. Right sidebar
    sidebar_needed_h = base_h - y_grid
    if sidebar_needed_h > 0:
        sidebar_piece = right_sidebar_src.crop((0, 0, right_sidebar_src.width, min(right_sidebar_src.height, sidebar_needed_h)))
        wb_canvas.paste(sidebar_piece, (base_w - 113, y_grid))
        
    # SQL Editor gutter & highlight
    draw_wb.rectangle([0, 74, 17, base_h], fill=(240, 240, 240))
    draw_wb.line([17, 74, 17, base_h], fill=(200, 200, 200))
    
    non_empty_indices = [i for i, l in enumerate(lines) if l.strip()]
    active_line_idx = non_empty_indices[-1] if non_empty_indices else (num_lines - 1)
    y_active = y_start + active_line_idx * line_h - 2
    draw_wb.rectangle([104, y_active, base_w - 118, y_active + line_h], fill=(239, 239, 239))
    
    # SQL Text rendering
    is_new_stmt = True
    max_code_x = 200
    for idx, line in enumerate(lines):
        curr_line_num = start_line_num + idx
        y_curr = y_start + idx * line_h
        
        draw_wb.text((32, y_curr), f"{curr_line_num:>3}", font=font_code, fill=(35, 120, 147))
        
        stripped = line.strip()
        if not stripped:
            continue
            
        if stripped.startswith('--'):
            draw_wb.text((104, y_curr), line, font=font_code, fill=(145, 145, 145))
            continue
            
        if is_new_stmt:
            draw_wb.ellipse([68, y_curr + 5, 74, y_curr + 11], fill=(16, 125, 197))
            
        is_new_stmt = stripped.endswith(';')
        x_tok = 104
        
        line_clean = line.replace('\t', '    ')
        tokens = TOKEN_PATTERN.findall(line_clean)
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
                
            draw_wb.text((x_tok, y_curr), tok, font=f_curr, fill=color)
            x_tok += draw_wb.textlength(tok, font=f_curr)
            
        max_code_x = max(max_code_x, x_tok)
        if idx == active_line_idx:
            draw_wb.line([x_tok + 1, y_curr + 1, x_tok + 1, y_curr + 15], fill=(0, 0, 0), width=1)
            
    # Calculate column widths
    col_widths = []
    col_pad = random.choice([20, 24, 28])
    min_col_w = random.choice([60, 65, 70])
    for col in columns:
        col_str = str(col)
        bbox = draw_wb.textbbox((0, 0), col_str, font=font_ui)
        w = bbox[2] - bbox[0]
        for row in rows[:max_rows]:
            val_fmt = format_cell_value(col, row.get(col, None))
            val_str = "NULL" if val_fmt is None else val_fmt
            bb = draw_wb.textbbox((0, 0), val_str, font=font_ui)
            w = max(w, bb[2] - bb[0])
        col_widths.append(max(w + col_pad, min_col_w))
        
    total_table_w = min(base_w - 130, 31 + sum(col_widths))
    
    # Table header
    draw_wb.line([17, y_tbl_hdr, 17 + total_table_w, y_tbl_hdr], fill=(178, 178, 178))
    draw_wb.line([17, y_tbl_hdr + hdr_h, 17 + total_table_w, y_tbl_hdr + hdr_h], fill=(181, 181, 181))
    draw_wb.line([17, y_tbl_hdr, 17, y_tbl_hdr + hdr_h], fill=(178, 178, 178))
    draw_wb.line([48, y_tbl_hdr, 48, y_tbl_hdr + hdr_h], fill=(205, 205, 205))
    
    curr_x = 48
    for col_idx, col in enumerate(columns):
        cw = col_widths[col_idx]
        draw_wb.text((curr_x + 7, y_tbl_hdr + 4), str(col), font=font_ui, fill=(20, 20, 20))
        draw_wb.line([curr_x + cw, y_tbl_hdr, curr_x + cw, y_tbl_hdr + hdr_h], fill=(205, 205, 205))
        curr_x += cw
        
    # Table rows
    for r_idx in range(max_rows):
        y_r = y_rows + r_idx * row_h
        bg_col = (255, 255, 255) if r_idx % 2 == 0 else (237, 243, 253)
        
        draw_wb.rectangle([17, y_r, 17 + total_table_w, y_r + row_h - 1], fill=bg_col)
        draw_wb.line([17, y_r, 17, y_r + row_h], fill=(178, 178, 178))
        sep_col = (225, 225, 225) if r_idx % 2 == 0 else (215, 228, 245)
        draw_wb.line([48, y_r, 48, y_r + row_h], fill=sep_col)
        
        if r_idx == 0:
            draw_wb.polygon([(26, y_r + 5), (31, y_r + 9), (31, y_r + 10), (26, y_r + 14)], fill=(50, 50, 50))
            
        curr_x = 48
        row_data = rows[r_idx]
        for col_idx, col in enumerate(columns):
            cw = col_widths[col_idx]
            val_fmt = format_cell_value(col, row_data.get(col, None))
            
            if val_fmt is None:
                wb_canvas.paste(null_badge, (curr_x + 6, y_r + 5))
            else:
                draw_wb.text((curr_x + 7, y_r + 3), val_fmt, font=font_ui, fill=(20, 20, 20))
                
            draw_wb.line([curr_x + cw, y_r, curr_x + cw, y_r + row_h], fill=sep_col)
            curr_x += cw
            
    y_table_bot = y_rows + max_rows * row_h
    draw_wb.line([17, y_table_bot, 17 + total_table_w, y_table_bot], fill=(205, 205, 205))
    
    # Action Output panel separator simulation below table
    y_output_sep = y_table_bot + 24
    draw_wb.line([0, y_output_sep, base_w, y_output_sep], fill=(185, 185, 185))
    draw_wb.rectangle([0, y_output_sep + 1, base_w, base_h], fill=(235, 235, 238))
    
    # Paste wb_canvas onto full_canvas
    full_canvas.paste(wb_canvas, (pad_left, pad_top))
    
    # -------------------------------------------------------------
    # REALISTIC HUMAN SNIPPING (Snipping Tool mouse drag simulation)
    # -------------------------------------------------------------
    # Top crop (y1):
    top_choice = random.choice(['clean_tab', 'cut_tab', 'skip_tab', 'extra_top'])
    if top_choice == 'clean_tab':
        y1 = pad_top
    elif top_choice == 'cut_tab':
        y1 = pad_top + random.randint(4, 15)  # partially cut tab
    elif top_choice == 'skip_tab':
        y1 = pad_top + random.randint(24, 30) # starts right at button toolbar
    else:
        y1 = max(0, pad_top - random.randint(3, 12)) # captured a sliver of menu bar
        
    # Left crop (x1):
    left_choice = random.choice(['clean_left', 'cut_gutter', 'extra_left'])
    if left_choice == 'clean_left':
        x1 = pad_left
    elif left_choice == 'cut_gutter':
        x1 = pad_left + random.randint(4, 14)  # cut slightly into line-number gutter
    else:
        x1 = max(0, pad_left - random.randint(3, 10)) # captured 3-10px outside window
        
    # Right crop (x2):
    table_edge_on_full = pad_left + 17 + total_table_w
    right_choice = random.choice(['full_sidebar', 'cut_sidebar', 'no_sidebar', 'extra_right'])
    if right_choice == 'full_sidebar':
        x2 = min(full_w, pad_left + base_w + random.randint(-4, 4))
    elif right_choice == 'cut_sidebar':
        x2 = pad_left + base_w - 113 + random.randint(18, 65) # cuts into sidebar
    elif right_choice == 'no_sidebar':
        # stops after table grid or code
        x2 = min(pad_left + base_w - 113, max(table_edge_on_full + random.randint(15, 55), pad_left + max_code_x + 80))
    else:
        x2 = min(full_w, pad_left + base_w + random.randint(5, 14)) # grabbed outside window
        
    # Bottom crop (y2):
    bot_choice = random.choice(['tight', 'mid', 'loose', 'has_output_slice'])
    if bot_choice == 'tight':
        y2 = pad_top + y_table_bot + random.randint(3, 8)
    elif bot_choice == 'mid':
        y2 = pad_top + y_table_bot + random.randint(10, 18)
    elif bot_choice == 'loose':
        y2 = pad_top + y_table_bot + random.randint(20, 28)
    else:
        y2 = min(full_h, pad_top + y_output_sep + random.randint(5, 14)) # captures bottom output divider
        
    # Ensure minimum reasonable bounding box
    x2 = max(x2, x1 + 450)
    y2 = max(y2, y1 + 160)
    
    final_snip = full_canvas.crop((x1, y1, x2, y2))
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_snip.save(output_path, "PNG")
