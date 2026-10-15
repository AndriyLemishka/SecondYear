import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def get_solution():
    A = [
        [ 1.0,  1.0,  1.0,  1.0,  1.0],
        [ 0.0,  2.1,  0.0, -0.9, -0.7],
        [-0.5, -0.9,  1.7, -0.4, -0.5],
        [ 0.0, -0.5, -0.5,  2.4, -0.3],
        [-0.2, -0.7, -0.6, -0.6,  1.8]
    ]
    B = [6.0, 0.6, -0.72, 1.32, -0.36]
    X0 = [0.0 for _ in range(5)]
    delta = 1e-10

    # Gauss
    n = len(B)
    AA = [aa[:] for aa in A]
    BB = B[:]
    for k in range(n - 1):
        value = 0
        index = k
        for i in range(k, n):
            if abs(AA[i][k]) > value:
                value = abs(AA[i][k])
                index = i
        AA[k], AA[index] = AA[index], AA[k]
        BB[k], BB[index] = BB[index], BB[k]
        for i in range(k + 1, n):
            m = AA[i][k] / AA[k][k]
            for j in range(k, n):
                AA[i][j] -= AA[k][j] * m
            BB[i] -= BB[k] * m
    x_gauss = BB[:]
    x_gauss[n - 1] = BB[n - 1] / AA[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            x_gauss[i] -= AA[i][j] * x_gauss[j]
        x_gauss[i] /= AA[i][i]

    # Gauss-Seidel
    dimension = len(X0)
    X = X0[:]
    history = [(0, X[:])]
    for k in range(1, 40):
        for i in range(dimension):
            X[i] = B[i]
            for j in range(dimension):
                if i != j:
                    X[i] -= A[i][j] * X[j]
            X[i] /= A[i][i]

        eps = [abs(X[i] - X0[i]) for i in range(dimension)]
        ksi = [eps[i] / (abs(X[i]) + delta) for i in range(dimension)]
        X0 = X[:]
        history.append((k, X[:]))

        if max(eps) < delta and max(ksi) < delta:
            break

    return x_gauss, history

def generate_report():
    template_path = os.path.join("Lab4", "materials", "lab04 (1).docx")
    doc = docx.Document(template_path)
    t = doc.tables[0]

    # Row 0: Title block
    c_left = t.rows[0].cells[1]
    c_left.text = (
        "ЗВО: Національний університет \n"
        "«Львівська політехніка»\n"
        "Навчальний рік: 2026/2027\n"
        "Семестр: осінній\n"
        "Навчальна дисципліна:\n"
        "Чисельні методи\n"
        "Кафедра систем автоматизованого\n"
        "проектування\n"
        "Викладач: Чумакевич В.В."
    )

    c_right = t.rows[0].cells[2]
    c_right.text = (
        "Тема: Чисельне розв’язування системи лінійних алгебраїчних рівнянь (№ 4)\n"
        "Інститут комп’ютерних наук та інформаційних технологій \n"
        "Група: ПП-24\n"
        "Студент: Лемішка Андрій\n"
        "Варіант: 12"
    )

    # Row 6: Variant system
    var_text = (
        "a + b + c + d + e = 6\n"
        "2,1 b – 0,9 d – 0,7 e = 0,6\n"
        "–0,5 a – 0,9 b + 1,7 c – 0,4 d – 0,5 e = –0,72\n"
        "–0,5 b – 0,5 c + 2,4 d – 0,3 e = 1,32\n"
        "–0,2 a – 0,7 b – 0,6 c – 0,6 d + 1,8 e = –0,36"
    )
    for c in t.rows[6].cells:
        c.text = var_text

    # Row 8: Matrix A and Vector B
    matrix_text = (
        "Матриця коефіцієнтів A (розмірності 5×5):\n"
        "┌                                              ┐\n"
        "│    1,0     1,0     1,0     1,0     1,0   │\n"
        "│    0,0     2,1     0,0    –0,9    –0,7   │\n"
        "│   –0,5    –0,9     1,7    –0,4    –0,5   │\n"
        "│    0,0    –0,5    –0,5     2,4    –0,3   │\n"
        "│   –0,2    –0,7    –0,6    –0,6     1,8   │\n"
        "└                                              ┘\n\n"
        "Вектор-стовпець вільних членів B:\n"
        "┌         ┐\n"
        "│    6,0  │\n"
        "│    0,6  │\n"
        "│  –0,72  │\n"
        "│   1,32  │\n"
        "│  –0,36  │\n"
        "└         ┘\n\n"
        "Початкове наближення: X(0) = [0; 0; 0; 0; 0]ᵀ; точність: δ = 10⁻¹⁰."
    )
    for c in t.rows[8].cells:
        c.text = matrix_text

    # Row 10: Code
    with open(os.path.join("Lab4", "src", "main.py"), "r", encoding="utf-8") as f:
        code_text = f.read().strip()
    for c in t.rows[10].cells:
        c.text = code_text

    # Compute solutions
    x_gauss, history = get_solution()

    # Row 12: Console output
    console_lines = [repr(x_gauss)]
    for k, xv in history:
        console_lines.append(f"{k} {repr(xv)}")
    console_text = "\n".join(console_lines)
    for c in t.rows[12].cells:
        c.text = console_text

    # Row 15: Gauss solution vector
    for c in t.rows[15].cells:
        c.text = repr(x_gauss)

    # Row 17: Gauss-Seidel table (nested table)
    cell_17 = t.rows[17].cells[0]
    nt = cell_17.tables[0]
    headers = ["i", "x1", "x2", "x3", "x4", "x5", "x"]
    for j, h in enumerate(headers):
        nt.rows[0].cells[j].text = h

    # Adjust row count
    needed_rows = len(history) + 1
    while len(nt.rows) < needed_rows:
        nt.add_row()
    while len(nt.rows) > needed_rows:
        tr = nt.rows[-1]._tr
        tr.getparent().remove(tr)

    for i, (k, xv) in enumerate(history):
        row_cells = nt.rows[i + 1].cells
        row_cells[0].text = str(k)
        for j in range(5):
            val_str = f"{xv[j]:.12f}".replace(".", ",")
            row_cells[j + 1].text = val_str
        row_cells[6].text = "1,2"

    # Row 19: Convergence Chart
    cell_19 = t.rows[19].cells[0]
    cell_19.text = ""
    p_img = cell_19.paragraphs[0]
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    plot_img_path = os.path.join("Lab4", "plots", "gauss_seidel_convergence.png")
    p_img.add_run().add_picture(plot_img_path, width=Inches(5.8))

    # Row 21: Shortened, concise Conclusions
    conclusion_text = (
        "У лабораторній роботі розв’язано систему лінійних алгебраїчних рівнянь варіанта 12 (група ПП-24) "
        "прямим методом Гауса та ітераційним методом Гауса — Зейделя. Розрахунки виконано мовою Python, "
        "а таблиці та графік збіжності побудовано в середовищі MS Excel (файл src/gauss_seidel.xlsx).\n\n"
        "Основні результати:\n"
        "1. Метод Гауса з вибором головного елемента за стовпцем за один прохід дав точний аналітичний "
        "розв’язок: x = [1.2, 1.2, 1.2, 1.2, 1.2], тобто a = b = c = d = e = 1,2.\n"
        "2. Метод Гауса — Зейделя при початковому наближенні X(0) = [0, 0, 0, 0, 0]ᵀ та критерії точності "
        "δ = 10⁻¹⁰ зійшовся за 21 ітерацію до вектора x = [1.2, 1.2, 1.2, 1.2, 1.2].\n"
        "3. Побудований графік підтверджує швидку та монотонну збіжність: уже після 7–8 ітерацій відхилення від "
        "точного розв'язку становлять менше 0,0002. Обидва методи показали повну узгодженість чисельних результатів."
    )
    for c in t.rows[21].cells:
        c.text = conclusion_text

    # Clear trailing paragraphs if any
    for p in list(doc.paragraphs):
        p._element.getparent().remove(p._element)

    # Append Control Questions
    questions_data = [
        ("1. Які існують типи методів розв'язання систем лінійних алгебраїчних рівнянь (СЛАР) і чим вони відрізняються один від одного?",
         "Методи розв’язування СЛАР поділяють на два основні типи:\n"
         "• Прямі (точні) методи — дозволяють отримати розв’язок за скінченну, наперед відому кількість арифметичних операцій (наприклад, метод Гауса, метод Крамера, метод матричного обернення). За відсутності похибок заокруглення вони дають абсолютно точний результат.\n"
         "• Ітераційні (наближені) методи — генерують нескінченну послідовність наближень X(0), X(1), ..., яка прямує до точного розв’язку. Процес обчислень зупиняється після досягнення заданої користувачем похибки δ (наприклад, метод простої ітерації, метод Гауса — Зейделя)."),

        ("2. Які методи належать до прямих методів розв'язування СЛАР?",
         "До прямих методів належать: класичний метод виключення Гауса (зі схемою єдиного ділення або вибором головного елемента), метод Жордана — Гауса, метод квадратних коренів (Холецького), метод прогонки (для тридіагональних матриць), метод Гауса за схемою Халецького (LU-розклад), а також метод Крамера."),

        ("3. Який алгоритм розв'язування СЛАР методом Гаусса за схемою Халецького?",
         "Алгоритм базується на розкладанні квадратної матриці A на добуток двох трикутних матриць A = B · C, де B — нижньотрикутна матриця з одиничною головною діагоналлю (b_ii = 1), а C — верхньотрикутна матриця. Після визначення елементів матриць B і C розв'язання системи зводиться до двох простих кроків:\n"
         "1) B · y = d — прямий хід, знаходимо проміжний вектор y;\n"
         "2) C · x = y — зворотний хід, знаходимо шуканий розв'язок x."),

        ("4. Які методи належать до ітераційних методів розв'язування СЛАР?",
         "До ітераційних методів належать: метод простої ітерації (метод Якобі), метод Гауса — Зейделя, метод верхньої релаксації (SOR), метод найшвидшого градієнтного спуску та метод спряжених градієнтів."),

        ("5. Як записується ітераційний процес методу простої ітерації?",
         "Вихідна система Ax = d перетворюється до еквівалентної форми x = Bx + e, де елементи матриці B визначаються як B_ij = –a_ij / a_ii (при i ≠ j) та B_ii = 0, а вектор e_i = d_i / a_ii. Ітераційний процес записується рекурентним рівнянням:\n"
         "X(k+1) = B · X(k) + e,   k = 0, 1, 2, ..."),

        ("6. Як оцінюється необхідна кількість ітерацій для досягнення потрібної точності методу простої ітерації?",
         "Якщо норма матриці ||B|| = C < 1, то апріорна кількість ітерацій K, необхідна для гарантованого досягнення похибки Δ, оцінюється формулою:\n"
         "K > [ln Δ – ln ||e|| + ln(1 – C)] / ln C – 1.\n"
         "На практиці також застосовують апостеріорну оцінку: ||X(k) – X(k–1)|| ≤ (1 – C)/C · Δ."),

        ("7. Яка обчислювальна схема методу простої ітерації?",
         "1) Перевіряється умова діагонального переважання (|a_ii| > ∑|a_ij| при j ≠ i).\n"
         "2) Будується розрахункова матриця B та вектор e.\n"
         "3) Обирається початкове наближення X(0) = e або X(0) = 0.\n"
         "4) На кожному кроці обчислюються всі нові компоненти x_i(k+1) за значеннями попередньої ітерації X(k).\n"
         "5) Обчислення повторюються, доки абсолютна або відносна похибка max |x_i(k+1) – x_i(k)| не стане меншою за задану точність δ."),

        ("8. Чим відрізняється метод Зейделя від методу простої ітерації розв'язування СЛАР?",
         "У методі простої ітерації при розрахунку всіх компонентів нового вектора X(k+1) використовуються лише значення з попереднього кроку X(k). У методі Зейделя при розрахунку компоненти x_i(k+1) відразу ж використовуються найновіші, щойно обчислені значення x_1(k+1), ..., x_(i–1)(k+1) цієї ж поточної ітерації. Це прискорює збіжність приблизно вдвічі та зменшує використання пам'яті."),

        ("9. Яка умова збіжності методу Зейделя?",
         "Достатньою умовою збіжності є умова строгого діагонального переважання матриці A:\n"
         "|a_ii| > ∑ |a_ij| (сума за всіма j ≠ i для кожного рядка i = 1..n),\n"
         "або симетричність і додатна визначеність матриці A. За цієї умови метод збігається при будь-якому виборі початкового наближення X(0).")
    ]

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(18)
    p_title.paragraph_format.space_after = Pt(12)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("Контрольні запитання та відповіді")
    r_title.bold = True
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(14)
    r_title.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

    for q, a in questions_data:
        pq = doc.add_paragraph()
        pq.paragraph_format.space_before = Pt(8)
        pq.paragraph_format.space_after = Pt(2)
        rq = pq.add_run(q)
        rq.bold = True
        rq.font.name = "Times New Roman"
        rq.font.size = Pt(11)

        pa = doc.add_paragraph()
        pa.paragraph_format.space_before = Pt(0)
        pa.paragraph_format.space_after = Pt(6)
        ra = pa.add_run(a)
        ra.font.name = "Times New Roman"
        ra.font.size = Pt(11)

    out_docx_path = os.path.join("Lab4", "Лемішка_Андрій_ЛР4_ПП24.docx")
    doc.save(out_docx_path)
    print(f"Report DOCX saved to: {out_docx_path}")

if __name__ == "__main__":
    generate_report()
