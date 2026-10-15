import os
import json
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

base_dir = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4"
cache_dir = os.path.join(base_dir, "cache")
results_path = os.path.join(cache_dir, "query_results.json")
logo_path = os.path.join(cache_dir, "logo_lp.png")
target_docx = os.path.join(base_dir, "Лемішка А_ПП-24_ЛР4.docx")

with open(results_path, "r", encoding="utf-8") as f:
    query_data = json.load(f)

doc = docx.Document()

# Set standard page margins (2 cm)
sections = doc.sections
for s in sections:
    s.top_margin = Cm(2)
    s.bottom_margin = Cm(2)
    s.left_margin = Cm(2.5)
    s.right_margin = Cm(1.5)

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(14)
font.color.rgb = RGBColor(0, 0, 0)

def add_p(text="", bold=False, italic=False, align='JUSTIFY', space_after=Pt(4), space_before=Pt(0), indent=Cm(1.25)):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = space_before
    p.paragraph_format.space_after = space_after
    p.paragraph_format.line_spacing = 1.15
    if align == 'CENTER':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p.paragraph_format.first_line_indent = 0
    elif align == 'RIGHT':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
        p.paragraph_format.first_line_indent = 0
    elif align == 'LEFT':
        p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        p.paragraph_format.first_line_indent = indent
    else:
        p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        p.paragraph_format.first_line_indent = indent
        
    if text:
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
    return p

def add_code(text):
    p = doc.add_paragraph()
    p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.first_line_indent = 0
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text)
    run.font.name = 'Consolas'
    run.font.size = Pt(10.5)
    run.font.color.rgb = RGBColor(20, 20, 80)
    return p

def add_fig(img_path, caption, width=Inches(6.2)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_img.paragraph_format.first_line_indent = 0
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(3)
        run = p_img.add_run()
        run.add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p_cap.paragraph_format.first_line_indent = 0
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(8)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(12)
        run_cap.italic = True
    else:
        add_p(f"[{caption}]", align='CENTER', indent=0)

def add_data_table(columns, rows):
    if not rows:
        return
    # Add small table caption/header
    num_rows = min(len(rows) + 1, 9)
    num_cols = len(columns)
    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    hdr_cells = table.rows[0].cells
    for i, col in enumerate(columns):
        hdr_cells[i].text = str(col)
        # shading
        shading = parse_xml(r'<w:shd {} w:fill="E9EEF4"/>'.format(nsdecls('w')))
        hdr_cells[i]._tc.get_or_add_tcPr().append(shading)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.first_line_indent = 0
        if p.runs:
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10.5)
            p.runs[0].bold = True

    # Data rows
    for r_idx, row_data in enumerate(rows[:num_rows-1]):
        row_cells = table.rows[r_idx + 1].cells
        for c_idx, col in enumerate(columns):
            val = row_data.get(col, "")
            val_str = "NULL" if val is None else str(val)
            row_cells[c_idx].text = val_str
            if r_idx % 2 == 1:
                shd = parse_xml(r'<w:shd {} w:fill="F8F9FA"/>'.format(nsdecls('w')))
                row_cells[c_idx]._tc.get_or_add_tcPr().append(shd)
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(1.5)
            p.paragraph_format.first_line_indent = 0
            if p.runs:
                p.runs[0].font.name = 'Times New Roman'
                p.runs[0].font.size = Pt(10)
                if val is None:
                    p.runs[0].italic = True
                    p.runs[0].font.color.rgb = RGBColor(120, 120, 120)

    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_after = Pt(4)
    p_after.paragraph_format.first_line_indent = 0

print("Helpers configured.")
