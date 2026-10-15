import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

LAB_DIR = r"d:\Studing\SecondYear\FirstSemester\OperatingSystems\Lab5"

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="D0D7DE"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def format_cell(cell, text, bold=False, italic=False, size=10.5, color=RGBColor(0x22, 0x22, 0x22), align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color
    return run

def add_header_styled(doc, text, level):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.bold = True
    run.font.name = "Times New Roman"
    if level == 1:
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    elif level == 2:
        run.font.size = Pt(13.5)
        run.font.color.rgb = RGBColor(0x00, 0x4B, 0x87)
    else:
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

def add_body_p(doc, text, bold_prefix=None, italic_prefix=None, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
        
    if italic_prefix:
        r_it = p.add_run(italic_prefix)
        r_it.italic = True
        r_it.font.name = "Times New Roman"
        r_it.font.size = Pt(12)
        
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

def add_callout(doc, text, title="ПРИМІТКА / РЕЗУЛЬТАТ ЕКСПЕРИМЕНТУ:"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F0F4F8")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    tcPr = cell._tc.get_or_add_tcPr()
    border = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="1B365D"/>
            <w:top w:val="none"/>
            <w:right w:val="none"/>
            <w:bottom w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(border)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    
    r_title = p.add_run(title + "\n")
    r_title.bold = True
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(10.5)
    r_title.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    r_txt = p.add_run(text)
    r_txt.font.name = "Times New Roman"
    r_txt.font.size = Pt(10.5)
    r_txt.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def add_screenshot_figure(doc, img_filename, caption_text, width=Inches(5.7)):
    img_path = os.path.join(LAB_DIR, "screenshots", img_filename)
    if not os.path.exists(img_path):
        img_path = os.path.join(LAB_DIR, img_filename)
    if not os.path.exists(img_path):
        print(f"Warning: Image {img_filename} not found!")
        return
    
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(3)
    p_img.paragraph_format.keep_with_next = True
    
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=width)
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(10)
    run_cap = p_cap.add_run(caption_text)
    run_cap.font.name = "Times New Roman"
    run_cap.font.size = Pt(10)
    run_cap.italic = True
    run_cap.font.color.rgb = RGBColor(0x44, 0x44, 0x44)

def setup_page_margins(doc):
    for sec in doc.sections:
        sec.top_margin = Inches(0.79) # 2.0 cm
        sec.bottom_margin = Inches(0.79) # 2.0 cm
        sec.left_margin = Inches(0.98) # 2.5 cm
        sec.right_margin = Inches(0.59) # 1.5 cm

def build_lab_report():
    print("Building Lab Report docx...")
    doc = Document()
    setup_page_margins(doc)
    
    # Title Page
    p_min = doc.add_paragraph()
    p_min.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_min.paragraph_format.space_before = Pt(10)
    p_min.paragraph_format.space_after = Pt(2)
    r = p_min.add_run("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.bold = True
    
    p_univ = doc.add_paragraph()
    p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_univ.paragraph_format.space_before = Pt(0)
    p_univ.paragraph_format.space_after = Pt(2)
    r = p_univ.add_run("НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»")
    r.font.name = "Times New Roman"
    r.font.size = Pt(13)
    r.bold = True
    
    p_dep = doc.add_paragraph()
    p_dep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dep.paragraph_format.space_before = Pt(0)
    p_dep.paragraph_format.space_after = Pt(80)
    r = p_dep.add_run("Кафедра «Системи автоматизованого проектування» (САПР)")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    
    p_zvit = doc.add_paragraph()
    p_zvit.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_zvit.paragraph_format.space_before = Pt(0)
    p_zvit.paragraph_format.space_after = Pt(12)
    r = p_zvit.add_run("ЗВІТ\nдо лабораторної роботи №5")
    r.font.name = "Times New Roman"
    r.font.size = Pt(18)
    r.bold = True
    r.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    p_disc = doc.add_paragraph()
    p_disc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_disc.paragraph_format.space_before = Pt(0)
    p_disc.paragraph_format.space_after = Pt(8)
    r = p_disc.add_run("з навчальної дисципліни «Операційні системи»\nна тему:")
    r.font.name = "Times New Roman"
    r.font.size = Pt(13)
    
    p_tema = doc.add_paragraph()
    p_tema.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tema.paragraph_format.space_before = Pt(0)
    p_tema.paragraph_format.space_after = Pt(100)
    r = p_tema.add_run("«Робота з об'єктами Active Directory на платформі Windows Server»")
    r.font.name = "Times New Roman"
    r.font.size = Pt(15)
    r.bold = True
    
    p_info = doc.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_info.paragraph_format.line_spacing = 1.2
    p_info.paragraph_format.space_after = Pt(100)
    
    r1 = p_info.add_run("Виконав:\n")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(12)
    r2 = p_info.add_run("студент групи ПП-14\nЛемішка Андрій\n\n")
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(12)
    r2.bold = True
    r3 = p_info.add_run("Перевірив:\n")
    r3.font.name = "Times New Roman"
    r3.font.size = Pt(12)
    r4 = p_info.add_run("викладач кафедри САПР\nБелей О. І.")
    r4.font.name = "Times New Roman"
    r4.font.size = Pt(12)
    r4.bold = True
    
    p_city = doc.add_paragraph()
    p_city.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_city.paragraph_format.space_before = Pt(40)
    p_city.paragraph_format.space_after = Pt(0)
    r = p_city.add_run("Львів – 2026")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.bold = True
    
    doc.add_page_break()
    
    # Main Content
    add_header_styled(doc, "Лабораторна робота №5", 1)
    add_header_styled(doc, "Тема: Робота з об'єктами Active Directory на платформі Windows Server", 2)
    
    add_body_p(doc, "Ознайомитися з установкою контролера домену, DNS- та DHCP-серверів на платформі операційної системи Windows Server. Ознайомитися з налаштуванням профілів користувачів домену Windows Server. Вивчити способи завдання групових політик, види параметрів групових політик, об’єкти групових політик, навчитися задавати групові політики для різних об’єктів.", bold_prefix="Мета роботи: ")
    
    add_body_p(doc, "1) Середовище віртуалізації Oracle VM VirtualBox 7.2;\n2) Серверна операційна система Microsoft Windows Server 2008 R2 Standard (контролер домену Server.office.com);\n3) Клієнтська операційна система Microsoft Windows 10 Pro (клієнтська станція);\n4) Системні компоненти та оснастки: Active Directory Domain Services (AD DS), DNS Server, DHCP Server, Active Directory Users and Computers (dsa.msc), Group Policy Management Console (gpmc.msc), Server Manager, Microsoft Management Console (mmc.exe).", bold_prefix="Обладнання та програмне забезпечення: ")
    
    # Section 1. Theory
    add_header_styled(doc, "1. Теоретичні відомості", 1)
    
    add_header_styled(doc, "1.1. Архітектура та функціонування служби каталогів Active Directory (AD DS)", 2)
    add_body_p(doc, "Active Directory Domain Services (AD DS) — це розподілена масштабована служба каталогів компанії Microsoft, яка є фундаментом побудови корпоративних мереж на основі серверних платформ Windows Server. Active Directory реалізує підтримку стандартних мережевих протоколів, таких як LDAP (Lightweight Directory Access Protocol) для доступу та навігації по каталогу, Kerberos v5 для надійної захищеної взаємної автентифікації клієнтів і серверів, а також інтегровану службу доменних імен DNS (Domain Name System).")
    add_body_p(doc, "Логічна ієрархія каталогу AD базується на наступних фундаментальних абстракціях:\n"
                    "• Об'єкт (Object) — неподільний базовий іменований елемент каталогу, охарактеризований унікальним глобальним ідентифікатором GUID та набором атрибутів (наприклад, обліковий запис користувача, комп'ютер, група безпеки, мережева спільна папка або принтер).\n"
                    "• Організаційний підрозділ (Organizational Unit, OU) — логічний контейнер вищого порядку всередині домену, який слугує для відображення організаційної структури підприємства (відділи, філії, служби). Підрозділи є базовими структурними одиницями для делегування адміністративних повноважень та прив'язки групових політик (GPO).\n"
                    "• Домен (Domain) — ключова межа безпеки та централізованого адміністрування, що об'єднує комп'ютери та користувачів під управлінням спільної політики безпеки та єдиної бази даних каталогу NTDS.dit.\n"
                    "• Дерево та Ліс (Tree & Forest) — ієрархічне об'єднання одного або кількох доменів, що поділяють спільну схему каталогу (AD Schema), єдину конфігурацію лісу та глобальний каталог (Global Catalog, GC).")
    
    add_header_styled(doc, "1.2. Механізм групових політик (Group Policy Objects, GPO)", 2)
    add_body_p(doc, "Групові політики (GPO) забезпечують централізовану конфігурацію робочого середовища користувачів та комп'ютерів. Кожен об'єкт GPO складається з двох взаємопов'язаних компонентів:\n"
                    "1) Group Policy Container (GPC) — об'єкт каталогу Active Directory (клас groupPolicyContainer), що зберігає атрибути політики (версія, GUID, статус, розширення клієнтської сторони CSE);\n"
                    "2) Group Policy Template (GPT) — каталог у файловій системі спільних ресурсів контролера домену (%SystemRoot%\\SYSVOL\\sysvol\\<domain>\\Policies\\<GUID>), що містить реальні файли налаштувань, бінарні файли реєстру Registry.pol, адміністративні шаблони ADMX/ADML, безпекові дескриптори та стартові скрипти.")
    add_body_p(doc, "Застосування групових політик здійснюється клієнтськими комп'ютерами у суворій послідовності за правилом LSDOU:\n"
                    "1. Local — локальна політика безпеки даного комп'ютера;\n"
                    "2. Site — групова політика сайту Active Directory;\n"
                    "3. Domain — загальнодоменні групові політики (Default Domain Policy);\n"
                    "4. OU (Organizational Unit) — групові політики організаційних підрозділів, які обробляються від кореневих підрозділів до вкладених.")

    add_header_styled(doc, "1.3. Класифікація облікових записів та профілів користувачів", 2)
    add_body_p(doc, "В операційних системах Windows реалізовано чітке розмежування облікових записів на локальні (зберігаються виключно в базі даних SAM локального комп'ютера %SystemRoot%\\System32\\config\\SAM) та доменні (централізовано розміщені в сховищі NTDS.dit контролера домену). Профілі користувача поділяються на три основні категорії:\n"
                    "• Локальний профіль (Local Profile) — створюється на локальному диску робочої станції під час першого входу (C:\\Users\\<Username>);\n"
                    "• Переміщуваний профіль (Roaming Profile) — зберігається на централізованому файловому сервері (\\\\server\\Profiles\\%username%). При вході користувача профіль синхронізується на локальну робочу станцію, а при виході — всі зміни переносяться назад на сервер;\n"
                    "• Обов'язковий профіль (Mandatory Profile) — модифікація переміщуваного профілю, у якому системний файл куща реєстру користувача Ntuser.dat перейменовано на Ntuser.man. При цьому користувач має право модифікувати параметри робочого середовища лише протягом поточного сеансу — під час завершення роботи будь-які зміни анулюються.")

    # Section 2. Practical Steps
    add_header_styled(doc, "2. Хід виконання роботи", 1)
    
    # Task 1
    add_header_styled(doc, "Завдання 1. Розгортання контролера домену, DNS- та DHCP-серверів", 2)
    add_body_p(doc, "1.1. Базове мережеве налаштування сервера. Для забезпечення коректного функціонування доменних служб та DNS-сервера мережевий адаптер серверної машини Windows Server 2008 R2 налаштовано на статичні мережеві параметри: IP-адреса 192.168.1.5, маска підмережі 255.255.255.0, основний шлюз 192.168.1.4, DNS-сервер 192.168.1.5 (вказує на себе). Ім'я комп'ютера задано як Server.")
    add_screenshot_figure(doc, "screenshot_step1_net_connections.png", "Рис. 1. Графічне налаштування статичної IP-адреси та DNS сервера Windows Server 2008 R2")
    
    add_body_p(doc, "1.2. Встановлення ролі Active Directory Domain Services. Через інтерфейс диспетчера сервера (Server Manager) активовано Майстер додавання ролей (Add Roles Wizard), у списку вибрано роль «Active Directory Domain Services» з автоматичним підтвердженням необхідних системних компонентів .NET Framework.")
    add_screenshot_figure(doc, "screenshot_step2_server_manager.png", "Рис. 2. Головне вікно диспетчера сервера (Server Manager)")
    add_screenshot_figure(doc, "screenshot_step5_roles_select_adds.png", "Рис. 3. Вибір ролі «Active Directory Domain Services» у Майстрі ролей")
    add_screenshot_figure(doc, "screenshot_step11_install_results.png", "Рис. 4. Успішне завершення встановлення бінарних компонентів AD DS")
    
    add_body_p(doc, "1.3. Підвищення ролі до контролера домену (DCPromo). Запущено майстер dcpromo.exe. Обрано конфігурацію «Створити новий домен у новому лісі» (Create a new domain in a new forest). Задано кореневе ім'я лісу office.com, функціональний рівень лісу та домену встановлено на рівень Windows Server 2008 R2, активовано інтеграцію служби DNS, вказано шляхи до бази даних NTDS (%SystemRoot%\\NTDS) та журналу SYSVOL (%SystemRoot%\\SYSVOL), задано надійний пароль режиму відновлення служб каталогів DSRM (Pa$$word).")
    add_screenshot_figure(doc, "screenshot_step14_dcpromo_new_forest.png", "Рис. 5. Вибір створення нового домену в новому лісі Active Directory")
    add_screenshot_figure(doc, "screenshot_step16_dcpromo_fqdn_office.png", "Рис. 6. Введення повного доменного імені кореневого домену office.com")
    add_screenshot_figure(doc, "screenshot_step17_dcpromo_functional_level.png", "Рис. 7. Встановлення функціонального рівня лісу Windows Server 2008 R2")
    add_screenshot_figure(doc, "screenshot_step22_dcpromo_summary.png", "Рис. 8. Підсумкова конфігурація майстра розгортання Active Directory")
    add_screenshot_figure(doc, "screenshot_step25_dc_configured_summary.png", "Рис. 9. Завершення налаштування контролера домену Server.office.com")

    add_body_p(doc, "1.4. Налаштування DHCP-сервера. Додано роль DHCP Server через Server Manager. В оснастці dhcpmgmt.msc авторизовано сервер Server.office.com у каталозі Active Directory. Створено нову область «Офіс» відповідно до параметрів варіанту, наведено у Таблиці 1.")
    
    # Table 1
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    p_t1 = doc.add_paragraph()
    p_t1.paragraph_format.keep_with_next = True
    r = p_t1.add_run("Таблиця 1. Параметри конфігурації області DHCP-сервера")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(11)
    
    t1 = doc.add_table(rows=8, cols=3)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t1)
    
    headers = ["№", "Параметр налаштування", "Значення конфігурації"]
    widths = [Inches(0.6), Inches(2.8), Inches(2.6)]
    for i, h in enumerate(headers):
        cell = t1.cell(0, i)
        cell.width = widths[i]
        set_cell_background(cell, "1B365D")
        format_cell(cell, h, bold=True, size=10.5, color=RGBColor(0xFF, 0xFF, 0xFF), align=WD_ALIGN_PARAGRAPH.CENTER)
        
    t1_data = [
        ("1", "Назва області DHCP (Scope Name)", "Офіс"),
        ("2", "Діапазон адрес пулу (Address Pool)", "192.168.1.1 — 192.168.1.200 (маска /24)"),
        ("3", "Діапазон виключення (Exclusions)", "192.168.1.150 — 192.168.1.170"),
        ("4", "Окремі виключені адреси", "192.168.1.1 — 192.168.1.10 (включаючи 192.168.1.2, 192.168.1.3, 192.168.1.5)"),
        ("5", "Тривалість оренди (Lease Duration)", "8 днів"),
        ("6", "Шлюз за замовчуванням (Option 003 Router)", "192.168.1.4"),
        ("7", "Зарезервована адреса (Reservation)", "IP: 192.168.1.4, Ім'я: Gateway, MAC: 1a-2b-3c-4d-5e-6f")
    ]
    for row_idx, data in enumerate(t1_data, start=1):
        bg = "F9FBFD" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(data):
            cell = t1.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_background(cell, bg)
            align = WD_ALIGN_PARAGRAPH.CENTER if col_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            format_cell(cell, text, size=10, align=align)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    add_screenshot_figure(doc, "screenshot_step58_new_scope_wizard_welcome.png", "Рис. 10. Майстер створення нової області DHCP (New Scope Wizard)")
    add_screenshot_figure(doc, "screenshot_step60_new_scope_ip_range.png", "Рис. 11. Конфігурація пулу IP-адрес 192.168.1.1 — 192.168.1.200")
    add_screenshot_figure(doc, "screenshot_step61_new_scope_exclusions.png", "Рис. 12. Додавання діапазонів виключень з видачі DHCP")
    add_screenshot_figure(doc, "screenshot_step67_dhcp_reservation_dialog.png", "Рис. 13. Діалогове вікно резервування IP 192.168.1.4 для шлюзу")
    add_screenshot_figure(doc, "screenshot_step70_dhcp_scope_options_final.png", "Рис. 14. Сконфігуровані параметри області DHCP (Router, DNS, Domain Name)")

    # Task 2
    add_header_styled(doc, "Завдання 2. Створення структури Active Directory (OU, Користувачі, Групи безпеки)", 2)
    add_body_p(doc, "В оснастці «Active Directory - користувачі та комп'ютери» (dsa.msc) у домені office.com розгорнуто організаційну структуру підрозділів (OU), створено облікові записи користувачів та глобальні групи безпеки відповідно до Таблиці 2.")
    
    # Table 2
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    p_t2 = doc.add_paragraph()
    p_t2.paragraph_format.keep_with_next = True
    r = p_t2.add_run("Таблиця 2. Структура підрозділів, користувачів і груп безпеки домену office.com")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(11)
    
    t2 = doc.add_table(rows=6, cols=4)
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t2)
    
    headers2 = ["№", "Організаційний підрозділ (OU)", "Облікові записи користувачів", "Глобальні групи безпеки"]
    widths2 = [Inches(0.5), Inches(1.8), Inches(2.2), Inches(1.8)]
    for i, h in enumerate(headers2):
        cell = t2.cell(0, i)
        cell.width = widths2[i]
        set_cell_background(cell, "1B365D")
        format_cell(cell, h, bold=True, size=10, color=RGBColor(0xFF, 0xFF, 0xFF), align=WD_ALIGN_PARAGRAPH.CENTER)
        
    t2_data = [
        ("1", "Керівники", "Директор (director), Заступник (deputy)", "Керівники"),
        ("2", "Фінансисти", "Бухгалтер (accountant), Економіст (economist), Менеджер (manager)", "Фінансисти"),
        ("3", "IT-спеціалісти", "Адміністратор (admin_it), Програміст (programmer), Сервіс-інженер (service_eng)", "IT-спеціалісти"),
        ("4", "Групи", "— (виділений контейнер для збереження об'єктів груп)", "AllStaff, IT-спеціалісти, Керівники, Фінансисти"),
        ("5", "Комп'ютери", "— (виділений підрозділ для клієнтських робочих станцій)", "—")
    ]
    for row_idx, data in enumerate(t2_data, start=1):
        bg = "F9FBFD" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(data):
            cell = t2.cell(row_idx, col_idx)
            cell.width = widths2[col_idx]
            set_cell_background(cell, bg)
            align = WD_ALIGN_PARAGRAPH.CENTER if col_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            format_cell(cell, text, size=10, align=align)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    add_screenshot_figure(doc, "screenshot_step27_new_ou_dialog.png", "Рис. 15. Створення нового організаційного підрозділу (New Object - OU)")
    add_screenshot_figure(doc, "screenshot_step42_tree_all_active.png", "Рис. 16. Повне ієрархічне дерево організаційних підрозділів домену office.com")
    add_screenshot_figure(doc, "screenshot_step43_ou_kerivnyky_contents.png", "Рис. 17. Вміст підрозділу «Керівники» з обліковими записами")
    add_screenshot_figure(doc, "screenshot_step44_ou_finansysty_contents.png", "Рис. 18. Вміст підрозділу «Фінансисти»")
    add_screenshot_figure(doc, "screenshot_step48_ou_it_contents.png", "Рис. 19. Вміст підрозділу «IT-спеціалісти»")
    add_screenshot_figure(doc, "screenshot_step51_ou_groups_contents.png", "Рис. 20. Контейнер груп безпеки «Групи»")

    # Task 3
    add_header_styled(doc, "Завдання 3. Налаштування об'єкта групової політики (GPO) для підрозділу", 2)
    add_body_p(doc, "В оснастці керування груповою політикою gpmc.msc створено об'єкт групової політики «Фінансова політика безпеки» та виконано його лінкування (зв'язування) з організаційним підрозділом «Фінансисти». У редакторі Group Policy Management Editor здійснено перехід за вузлом:\n"
                    "Конфігурація користувача -> Політики -> Адміністративні шаблони -> Панель керування -> Персоналізація.\n"
                    "Сконфігуровано наступні параметри безпеки:\n"
                    "1) Тайм-аут екранної заставки (Screen saver timeout): стан — Увімкнено (Enabled), тайм-аут — 600 секунд (10 хвилин). Внесено коментар «Фінансова політика безпеки»;\n"
                    "2) Захист заставки паролем (Password protect the screen saver): стан — Увімкнено (Enabled);\n"
                    "3) Увімкнення заставки (Enable screen saver): стан — Увімкнено (Enabled).")
    add_screenshot_figure(doc, "screenshot_step71_gpmc_tree.png", "Рис. 21. Оснастка gpmc.msc: створення та прив'язка GPO до OU «Фінансисти»")
    add_screenshot_figure(doc, "screenshot_step72_gpo_screensaver_timeout_dialog.png", "Рис. 22. Налаштування тайм-ауту заставки (600 с) з обов'язковим коментарем")
    add_screenshot_figure(doc, "screenshot_step72_gpo_screensaver.png", "Рис. 23. Редактор групових політик: стан активованих параметрів персоналізації")

    # Task 4 & 5
    add_header_styled(doc, "Завдання 4. Конфігурація спільних мережевих папок та домашніх дисків", 2)
    add_body_p(doc, "На системному диску C: контролера домену створено структуру папок для спільної роботи підприємства C:\\Офіс з підпапками Керівники, Фінансисти, IT-спеціалісти, Users. Налаштовано комбіновані права доступу:\n"
                    "• Мережевий доступ (SMB Share Permissions): групі Domain Users надано права Change та Read;\n"
                    "• Права файлової системи (NTFS Permissions): налаштовано списки контролю доступу (ACL) з успадкуванням прав читання та вибірковим правом запису/модифікації виключно для відповідних груп підрозділів;\n"
                    "• Монтування домашнього диска: в оснастці dsa.msc у властивостях облікового запису Програміст на вкладці «Профіль» підключено мережевий диск P: за UNC-шляхом \\\\server\\Офіс.")
    add_screenshot_figure(doc, "screenshot_step73_ofis_sharing.png", "Рис. 24. Властивості папки C:\\Офіс: налаштування мережевого доступу SMB")
    add_screenshot_figure(doc, "screenshot_step74_ofis_security.png", "Рис. 25. Властивості папки C:\\Офіс: налаштування дескрипторів безпеки NTFS")
    add_screenshot_figure(doc, "screenshot_step49_programmer_profile.png", "Рис. 26. Налаштування монтування домашнього диска P: для користувача «Програміст»")

    add_header_styled(doc, "Завдання 5. Налаштування переміщуваних (Roaming) та обов'язкових (Mandatory) профілів", 2)
    add_body_p(doc, "Створено мережеве сховище профілів C:\\Profiles з мережевим ім'ям \\\\SERVER\\Profiles з повним доступом для автентифікованих користувачів та системи.\n"
                    "• Переміщуваний профіль: для користувача Сервіс-інженер вказано шлях \\\\server\\Profiles\\%username%. При вході та виході користувача вміст його робочого столу та налаштувань програм автоматично синхронізується з сервером;\n"
                    "• Обов'язковий профіль: для користувача Менеджер налаштовано шлях профілю, після першого входу файл куща реєстру Ntuser.dat на сервері перейменовано на Ntuser.man. Проведено експеримент: створено каталог на робочому столі «Шеф - завжди правий». Після завершення роботи та повторного входу створена папка зникла, що підтверджує режим обов'язкового профілю, захищеного від локальних модифікацій.")
    add_screenshot_figure(doc, "screenshot_step75_profiles_sharing.png", "Рис. 27. Мережевий доступ до сховища профілів C:\\Profiles")
    add_screenshot_figure(doc, "screenshot_step76_profiles_security.png", "Рис. 28. Рівень доступу NTFS сховища профілів")
    add_screenshot_figure(doc, "screenshot_step46_manager_profile_path.png", "Рис. 29. Завдання мережевого шляху до переміщуваного профілю користувача")
    
    add_callout(doc, "При перейменуванні файлу реєстру Ntuser.dat на Ntuser.man профіль стає обов'язковим (read-only). Операційна система Windows забороняє збереження змін у конфігурації профілю на сервері при виході користувача з системи, що гарантує захист робочого середовища від несанкціонованих правок.", title="РЕЗУЛЬТАТ ДОСЛІДЖЕННЯ ОБОВ'ЯЗКОВОГО ПРОФІЛЮ:")

    # Tasks 6, 7, 8
    add_header_styled(doc, "Завдання 6–8. Політики паролів, блокування облікових записів та ActiveDesktop", 2)
    add_body_p(doc, "• Політика складності паролів: у Default Domain Policy (Конфігурація комп'ютера -> Параметри безпеки -> Політики облікових записів -> Політика паролів) активовано: мінімальна довжина пароля — 8 символів, збереження історії — 3 паролі, вимоги складності — Увімкнено, максимальний термін дії — 60 днів;\n"
                    "• Політика блокування облікових записів (Account Lockout Policy): поріг блокування — 3 спроби невдалого входу, тривалість блокування — 5 хвилин, скидання лічильника блокування — через 5 хвилин;\n"
                    "• ActiveDesktop для підрозділу StudentSecurity: створено окремий OU StudentSecurity з прив'язкою GPO, яка блокує можливість користувача самостійно змінювати шпалери робочого столу (Prohibit changes to desktop background) та призначає корпоративне зображення.")

    # Task 9
    add_header_styled(doc, "Завдання 9. Приєднання клієнтської робочої станції Windows 10 до домену office.com", 2)
    add_body_p(doc, "Клієнтська робоча станція Windows 10 підключена до внутрішньої мережі office_net. Завдяки наявності авторизованого DHCP-сервера робоча станція автоматично отримала адресу з пулу 192.168.1.1, маску 255.255.255.0, шлюз 192.168.1.4, DNS 192.168.1.5 та доменний суфікс office.com з терміном оренди на 8 днів, що зафіксовано на знімку екрана (Рис. 30).")
    add_screenshot_figure(doc, "screenshot_step77_win10_dhcp_ipconfig.png", "Рис. 30. Клієнт Windows 10: підтвердження отримання параметрів від DHCP-сервера домену office.com")
    add_body_p(doc, "Властивості комп'ютера відкрито через діалогове вікно sysdm.cpl. У вкладці «Ім'я комп'ютера» натиснуто кнопку «Змінити», вибрано членство у домені office.com та введено облікові дані адміністратора домену (Administrator / Pa$$word). Після успішної перевірки автентифікації контролер домену відобразив повідомлення «Ласкаво просимо до домену office.com», після чого комп'ютер виконано перезавантаження та здійснено вхід під доменним користувачем.")

    # Tasks 10, 11, 12
    add_header_styled(doc, "Завдання 10–12. Спільні папки, механізм «Run As» та міграція SSRS", 2)
    add_body_p(doc, "• Спільна мережева папка: підключено мережевий ресурс \\\\server\\Users\\Студенти як локальний мережевий диск G: для доменних клієнтів;\n"
                    "• Механізм підвищення привілеїв «Run As»: досліджено запуск адміністративних оснасток та утиліт із сеансу рядового користувача. За допомогою контекстного меню (Shift + правий клік -> «Запустити від імені іншого користувача») введено реквізити office.com\\Administrator, що забезпечило виконання завдань управління без переривання користувацького сеансу;\n"
                    "• Міграція звітів SSRS (rs.exe): досліджено скриптову утиліту rs.exe та сценарій ssrs_migration.rss для реплікації об'єктів між серверами SQL Server Reporting Services. Підтримувані режими представлено в Таблиці 3.")
    
    # Table 3
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    p_t3 = doc.add_paragraph()
    p_t3.paragraph_format.keep_with_next = True
    r = p_t3.add_run("Таблиця 3. Режими серверів звітів для міграції утилітою rs.exe")
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(11)
    
    t3 = doc.add_table(rows=4, cols=3)
    t3.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t3)
    
    headers3 = ["№", "Сервер міграції", "Режим функціонування сервера звітів (Mode)"]
    widths3 = [Inches(0.6), Inches(2.7), Inches(2.7)]
    for i, h in enumerate(headers3):
        cell = t3.cell(0, i)
        cell.width = widths3[i]
        set_cell_background(cell, "1B365D")
        format_cell(cell, h, bold=True, size=10, color=RGBColor(0xFF, 0xFF, 0xFF), align=WD_ALIGN_PARAGRAPH.CENTER)
        
    t3_data = [
        ("1", "Сервер А (Вихідний)", "Власний режим (Native Mode)"),
        ("2", "Сервер В (Цільовий)", "SharePoint Integrated Mode"),
        ("3", "Сервер С (Резервний)", "SharePoint Integrated Mode")
    ]
    for row_idx, data in enumerate(t3_data, start=1):
        bg = "F9FBFD" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(data):
            cell = t3.cell(row_idx, col_idx)
            cell.width = widths3[col_idx]
            set_cell_background(cell, bg)
            align = WD_ALIGN_PARAGRAPH.CENTER if col_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            format_cell(cell, text, size=10, align=align)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Section 3. Control Questions
    add_header_styled(doc, "3. Відповіді на контрольні запитання", 1)
    
    add_body_p(doc, "Active Directory Domain Services (AD DS) — це масштабована, безпечна та стандартизована служба каталогів корпорації Microsoft, що діє як єдине централізоване сховище метаданих та облікових даних мережевих ресурсів (користувачів, комп'ютерів, груп, принтерів, спільних файлових ресурсів). Її ключовими функціями є: 1) централізація автентифікації та авторизації в масштабах підприємства за стандартами Kerberos v5 та NTLM; 2) забезпечення ієрархічної структури управління через підрозділи (OU); 3) доставка конфігурацій та параметрів безпеки за допомогою групових політик (GPO); 4) надання глобального пошуку через протокол LDAP та роль Global Catalog.", bold_prefix="1. Що таке Active Directory та яка її основна функція? ")
    
    add_body_p(doc, "Основні відмінності полягають у принципах управління та безпеки:\n"
                    "• У робочій групі (Workgroup) кожен комп'ютер є децентралізованим та ізольованим вузлом (peer-to-peer). Кожен вузол має власну локальну базу безпеки SAM, тому користувача необхідно створювати окремо на кожній машині, а централізоване керування політиками відсутнє;\n"
                    "• У домені (Domain) управління є строго централізованим на основі клієнт-серверної архітектури. Облікові записи створюються один раз у каталозі NTDS.dit контролера домену та діють на всіх робочих станціях, об'єднаних у довірчу зону.", bold_prefix="2. Чим відрізняється робоча група (Workgroup) від домену (Domain)? ")
    
    add_body_p(doc, "• Переміщуваний профіль (Roaming User Profile) зберігає робочий стіл, конфігураційні файли додатків та гілку реєстру HKEY_CURRENT_USER на централізованому файловому сервері (шлях \\\\server\\Profiles\\%username%). При вході на будь-яку робочу станцію профіль копіюється локально, а при виході — всі змінені файли та стан реєстру Ntuser.dat оновлюються на сервері;\n"
                    "• Обов'язковий профіль (Mandatory Profile) відрізняється наявністю перейменованого файлу Ntuser.man замість Ntuser.dat. Він є профілем лише для читання. Користувач може створювати документи на робочому столі або змінювати налаштування протягом поточного сеансу, але під час виходу операційна система відкидає всі модифікації і не записує їх на сервер. Це забезпечує ідентичний стандартний стан інтерфейсу при кожному запуску (наприклад, для терміналів, банківських кас, студентських аудиторій).", bold_prefix="3. Яка різниця між переміщуваним (Roaming) та обов'язковим (Mandatory) профілем? ")
    
    add_body_p(doc, "Утиліта dcpromo.exe (Domain Controller Promoter) — це спеціалізований майстер та системна утиліта Microsoft, призначена для перетворення рядового сервера (Member Server або Standalone Server) на контролер домену Active Directory, або навпаки — пониження контролера домену до звичайного сервера (Demotion). Утиліта виконує генерацію або підключення до лісу, створення інтегрованих зон DNS, формування розділів каталогу NTDS.dit та ініціалізацію реплікації SYSVOL.", bold_prefix="4. Для чого використовується утиліта dcpromo? ")

    # Section 4. Conclusions
    add_header_styled(doc, "4. Висновки", 1)
    add_body_p(doc, "Під час виконання лабораторної роботи №5 було успішно розгорнуто повну доменну інфраструктуру підприємства на базі контролера домену Windows Server 2008 R2 Standard (Server.office.com) та клієнтської станції Windows 10 Pro у віртуалізованому середовищі Oracle VM VirtualBox. В процесі роботи:\n"
                    "1. Набуто практичних навичок проектування мережевої архітектури: призначено статичні адреси серверу, розгорнуто та авторизовано службу динамічної роздачі адрес DHCP Server з пулом 192.168.1.1–192.168.1.200, налаштовано діапазони виключень, резервування IP-адреси шлюзу (192.168.1.4) та глобальні опції маршрутизації (Router, DNS Server, DNS Domain Name);\n"
                    "2. За допомогою оснастки Active Directory Users and Computers (dsa.msc) створено організаційну структуру підрозділів (Керівники, Фінансисти, IT-спеціалісти, Групи, Комп'ютери, StudentSecurity), зареєстровано облікові записи працівників, організовано глобальні групи безпеки та делеговано адміністративні повноваження;\n"
                    "3. Досліджено механізм функціонування об'єктів групової політики (GPO) через оснастку gpmc.msc: сформовано «Фінансову політику безпеки», що регулює параметри автоматичного блокування робочого столу екранною заставкою із захистом паролем через 600 секунд бездіяльності;\n"
                    "4. Налаштовано багаторівневу систему розмежування прав доступу до файлових ресурсів на основі комбінації мережевих дозволів SMB та списків керування доступом NTFS ACL для папки C:\\Офіс, змонтовано персональний мережевий диск P: для програміста;\n"
                    "5. Експериментально підтверджено різницю між функціонуванням переміщуваного (Roaming) та обов'язкового (Mandatory / Ntuser.man) профілів, досліджено захист сеансу обов'язкового профілю від локальних змін;\n"
                    "6. Перевірено взаємодію клієнтської машини Windows 10 з контролером домену, підтверджено отримання адреси 192.168.1.1 від DHCP-сервера та здійснено введення комп'ютера до домену office.com через графічний інтерфейс.")

    out_docx = os.path.join(LAB_DIR, "reports", "Лемішка_ПП_14_Лаб_5.docx")
    doc.save(out_docx)
    print(f"Report saved successfully to {out_docx}")

def build_runbook():
    print("Building Runbook docx...")
    doc = Document()
    setup_page_margins(doc)
    
    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(20)
    p_title.paragraph_format.space_after = Pt(6)
    r = p_title.add_run("ПОКРОКОВА ІНСТРУКЦІЯ ТА КАРТА НАТИСКАНЬ")
    r.font.name = "Times New Roman"
    r.font.size = Pt(16)
    r.bold = True
    r.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(24)
    r = p_sub.add_run("Регламент практичного виконання Лабораторної роботи №5 через графічний інтерфейс (UI)\nСтудент: Лемішка Андрій, Група: ПП-14, САПР")
    r.font.name = "Times New Roman"
    r.font.size = Pt(11.5)
    r.italic = True
    
    add_body_p(doc, "Даний регламент містить повну хронологічну послідовність дій адміністратора у графічному інтерфейсі користувача (GUI) серверної ОС Windows Server 2008 R2 та клієнта Windows 10 для успішного виконання завдань лабораторної роботи №5. Кожен крок супроводжується назвою вікна, цільовими елементами керування (кнопки, вкладки, поля вводу) та відповідним графічним підтвердженням.")
    
    steps = [
        ("Крок 1. Базове налаштування TCP/IPv4 сервера",
         "1. Відкрити «Network and Sharing Center» -> «Change adapter settings».\n"
         "2. Клацнути правою кнопкою миші на «Local Area Connection» -> «Properties».\n"
         "3. Виділити «Internet Protocol Version 4 (TCP/IPv4)» -> натиснути «Properties».\n"
         "4. Вибрати «Use the following IP address»:\n"
         "   • IP address: 192.168.1.5\n"
         "   • Subnet mask: 255.255.255.0\n"
         "   • Default gateway: 192.168.1.4\n"
         "   • Preferred DNS server: 192.168.1.5\n"
         "5. Натиснути «OK» -> «Close».",
         "screenshot_step1_net_connections.png",
         "Рис. Р1. Вікно налаштування властивостей TCP/IPv4"),
         
        ("Крок 2. Встановлення ролі Active Directory Domain Services",
         "1. Відкрити «Server Manager» (кнопка в панелі задач біля «Start»).\n"
         "2. У дереві вибрати вузол «Roles» -> у правому вікні натиснути «Add Roles».\n"
         "3. У Майстрі ролей натиснути «Next» на початковій сторінці.\n"
         "4. Встановити прапорець «Active Directory Domain Services».\n"
         "5. У вікні підтвердження залежностей натиснути «Add Required Features».\n"
         "6. Натиснути «Next» -> «Next» -> «Install».\n"
         "7. Дочекатися успішного завершення інсталяції та натиснути «Close».",
         "screenshot_step5_roles_select_adds.png",
         "Рис. Р2. Вибір ролі AD DS у Майстрі додавання ролей"),
         
        ("Крок 3. Підвищення сервера до контролера домену (DCPromo)",
         "1. Натиснути кнопку «Start» -> у полі пошуку ввести dcpromo.exe -> Enter.\n"
         "2. На вітальному екрані натиснути «Next» -> на екрані сумісності натиснути «Next».\n"
         "3. Обрати радіокнопку «Create a new domain in a new forest» -> «Next».\n"
         "4. У полі «FQDN of the forest root domain» ввести: office.com -> «Next».\n"
         "5. Встановити «Forest functional level»: Windows Server 2008 R2 -> «Next».\n"
         "6. На вкладці додаткових опцій переконатися, що прапорець «DNS server» встановлено -> «Next».\n"
         "7. Шляхи до папок NTDS та SYSVOL залишити за замовчуванням -> «Next».\n"
         "8. У полях «Password» та «Confirm password» ввести: Pa$$word -> «Next».\n"
         "9. Переглянути зведення параметрів -> натиснути «Next».\n"
         "10. Після завершення промоції та автоматичного перезавантаження увійти під доменним обліковим записом Administrator.",
         "screenshot_step16_dcpromo_fqdn_office.png",
         "Рис. Р3. Введення імені домену office.com у майстрі dcpromo"),
         
        ("Крок 4. Створення структури підрозділів (OU) в Active Directory",
         "1. Відкрити «Start» -> «Administrative Tools» -> «Active Directory Users and Computers» (або виконати dsa.msc).\n"
         "2. Розгорнути вузол домену office.com.\n"
         "3. Клацнути правою кнопкою на office.com -> «New» -> «Organizational Unit».\n"
         "4. Послідовно створити підрозділи: «Керівники», «Фінансисти», «IT-спеціалісти», «Групи», «Комп'ютери», «StudentSecurity».\n"
         "5. Для кожного OU залишити активним прапорець «Protect container from accidental deletion» -> натиснути «OK».",
         "screenshot_step27_new_ou_dialog.png",
         "Рис. Р4. Створення організаційного підрозділу через графічне меню dsa.msc"),
         
        ("Крок 5. Створення облікових записів користувачів та груп безпеки",
         "1. У підрозділі «Керівники»: правий клік -> «New» -> «User» -> створити «Директор» (director) та «Заступник» (deputy).\n"
         "2. У підрозділі «Фінансисти»: створити «Бухгалтер» (accountant), «Економіст» (economist), «Менеджер» (manager).\n"
         "3. У підрозділі «IT-спеціалісти»: створити «Адміністратор» (admin_it), «Програміст» (programmer), «Сервіс-інженер» (service_eng).\n"
         "4. У підрозділі «Групи»: правий клік -> «New» -> «Group» -> створити глобальні групи безпеки: «Керівники», «Фінансисти», «IT-спеціалісти», «AllStaff».\n"
         "5. Відкрити властивості кожної групи -> вкладка «Members» -> кнопка «Add...» -> додати відповідних користувачів.\n"
         "6. Відкрити властивості користувача admin_it -> вкладка «Member Of» -> «Add...» -> додати вбудовану групу «Domain Admins».",
         "screenshot_step42_tree_all_active.png",
         "Рис. Р5. Дерево Active Directory зі створеними підрозділами та об'єктами"),
         
        ("Крок 6. Встановлення та авторизація DHCP-сервера",
         "1. У «Server Manager» вибрати «Roles» -> «Add Roles» -> обрати «DHCP Server» -> пройти майстер інсталяції.\n"
         "2. Відкрити «Start» -> «Administrative Tools» -> «DHCP» (dhcpmgmt.msc).\n"
         "3. Клацнути правою кнопкою на кореневому вузлі «DHCP» -> «Manage authorized servers...».\n"
         "4. Натиснути кнопку «Authorize...» -> ввести Server.office.com -> натиснути «OK» -> закрити вікно.\n"
         "5. Переконатися, що піктограма сервера змінила стан на активний (зелена стрілка).",
         "screenshot_step55_dhcp_service_started.png",
         "Рис. Р6. Авторизована та запущена служба DHCP-сервера"),
         
        ("Крок 7. Створення та конфігурація нової області DHCP «Офіс»",
         "1. В оснастці dhcpmgmt.msc розгорнути вузол Server.office.com -> IPv4.\n"
         "2. Клацнути правою кнопкою на «IPv4» -> «New Scope...» -> «Next».\n"
         "3. Ввести назву області: Офіс -> «Next».\n"
         "4. Вказати діапазон IP-адрес: Start IP: 192.168.1.1, End IP: 192.168.1.200, Length: 24, Subnet mask: 255.255.255.0 -> «Next».\n"
         "5. Додати діапазони виключення: 192.168.1.1 — 192.168.1.10 та 192.168.1.150 — 192.168.1.170 -> «Add» -> «Next».\n"
         "6. Термін оренди (Lease Duration) встановити: 8 днів -> «Next».\n"
         "7. Обрати «Yes, I want to configure these options now» -> «Next».\n"
         "8. Шлюз (Router): 192.168.1.4 -> «Add» -> «Next».\n"
         "9. Доменне ім'я: office.com, DNS Server: 192.168.1.5 -> «Add» -> «Next».\n"
         "10. Активація області: обрати «Yes, I want to activate this scope now» -> «Finish».\n"
         "11. У гілці «Reservations» області «Офіс»: правий клік -> «New Reservation...» -> ввести Reservation name: Gateway, IP: 192.168.1.4, MAC: 1a2b3c4d5e6f -> «Add» -> «Close».",
         "screenshot_step70_dhcp_scope_options_final.png",
         "Рис. Р7. Підсумкові параметри області DHCP з опціями маршрутизації та DNS"),
         
        ("Крок 8. Створення об'єкта групової політики (GPO)",
         "1. Відкрити «Start» -> «Administrative Tools» -> «Group Policy Management» (gpmc.msc).\n"
         "2. Розгорнути Forest -> Domains -> office.com -> знайти підрозділ «Фінансисти».\n"
         "3. Клацнути правою кнопкою на «Фінансисти» -> обрати «Create a GPO in this domain, and Link it here...».\n"
         "4. Ввести назву GPO: «Фінансова політика безпеки» -> «OK».\n"
         "5. Клацнути правою кнопкою на новоствореній політиці -> «Edit...».\n"
         "6. У редакторі перейти за вузлом: User Configuration -> Policies -> Administrative Templates -> Control Panel -> Personalization.\n"
         "7. Відкрити параметр «Screen saver timeout» -> обрати «Enabled» -> встановити 600 секунд -> у вкладці «Explain» / «Comment» внести коментар «Фінансова політика безпеки» -> «OK».\n"
         "8. Відкрити параметр «Password protect the screen saver» -> обрати «Enabled» -> «OK».\n"
         "9. Відкрити параметр «Enable screen saver» -> обрати «Enabled» -> «OK».",
         "screenshot_step72_gpo_screensaver_timeout_dialog.png",
         "Рис. Р8. Налаштування параметрів екранної заставки у редакторі GPO"),
         
        ("Крок 9. Створення спільних папок та монтування дисків",
         "1. Відкрити «Windows Explorer» -> локальний диск C: -> створити каталог C:\\Офіс.\n"
         "2. Клацнути правою кнопкою миші на C:\\Офіс -> «Properties» -> вкладка «Sharing» -> кнопка «Advanced Sharing...».\n"
         "3. Встановити прапорець «Share this folder» -> ім'я спільного ресурсу: Офіс -> кнопка «Permissions» -> надати Domain Users права Change та Read -> «OK».\n"
         "4. Перейти на вкладку «Security» -> «Edit...» -> налаштувати права NTFS для груп підрозділів -> «OK».\n"
         "5. Створити каталог C:\\Profiles -> розшарити як \\\\SERVER\\Profiles з повним доступом для автентифікованих користувачів.\n"
         "6. В оснастці dsa.msc відкрити властивості користувача «Програміст» -> вкладка «Profile» -> у блоці «Home folder» обрати радіокнопку «Connect: P:» -> ввести To: \\\\server\\Офіс -> «OK».",
         "screenshot_step73_ofis_sharing.png",
         "Рис. Р9. Вікно налаштування мережевого доступу папки C:\\Офіс"),
         
        ("Крок 10. Приєднання робочої станції Windows 10 до домену",
         "1. Запустити клієнтську віртуальну машину Windows 10 у мережі office_net.\n"
         "2. Переконатися за допомогою команди ipconfig /all, що клієнт отримав адресу 192.168.1.1, шлюз 192.168.1.4, DNS 192.168.1.5 та доменний суфікс office.com від DHCP-сервера.\n"
         "3. Натиснути Win + R -> ввести sysdm.cpl -> Enter.\n"
         "4. На вкладці «Комп'ютерне ім'я» (Computer Name) натиснути кнопку «Змінити...» (Change...).\n"
         "5. У розділі «Членство» (Member of) встановити перемикач на «Домен» (Domain) та ввести: office.com.\n"
         "6. Натиснути «ОК» -> у вікні автентифікації ввести логін: Administrator та пароль: Pa$$word -> «ОК».\n"
         "7. Отримати вітальне вікно «Ласкаво просимо до домену office.com» -> підтвердити перезавантаження.\n"
         "8. Після рестарту увійти до системи під обліковим записом користувача Програміст (office\\programmer).",
         "screenshot_step77_win10_dhcp_ipconfig.png",
         "Рис. Р10. Підтвердження отримання параметрів від DHCP-сервера на клієнті Windows 10")
    ]
    
    for title, text, img, cap in steps:
        add_header_styled(doc, title, 2)
        add_body_p(doc, text)
        add_screenshot_figure(doc, img, cap, width=Inches(5.6))
        
    out_runbook = os.path.join(LAB_DIR, "reports", "Покрокова_інструкція_натискань_Лаб5.docx")
    doc.save(out_runbook)
    print(f"Runbook saved successfully to {out_runbook}")

if __name__ == "__main__":
    build_lab_report()
    build_runbook()
    print("ALL DOCUMENTS GENERATED SUCCESSFULLY!")

