import docx
doc = docx.Document(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 3\Лемішка А_ПП-24_ЛР3.docx")
p4 = doc.paragraphs[4]
for r in p4.runs:
    if 'graphic' in r._r.xml:
        # find blip
        import xml.etree.ElementTree as ET
        tree = ET.fromstring(r._r.xml)
        for elem in tree.iter():
            if elem.tag.endswith('blip'):
                embed_id = elem.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                print('P4 embed_id:', embed_id, doc.part.rels[embed_id].target_ref)
