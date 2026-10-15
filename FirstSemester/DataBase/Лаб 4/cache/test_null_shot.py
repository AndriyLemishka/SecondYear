import json
from test_wb_generator import generate_workbench_image
from PIL import ImageDraw

with open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\query_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Task 1 query 1.4 (NULL description)
t1_4 = data[0]["items"][3]
print(t1_4)

img_1_4 = generate_workbench_image(
    sql_text=f"USE marketplace_3d;\n-- Запит 1.4: Пошук моделей без опису (IS NULL)\n{t1_4['sql']}",
    columns=list(t1_4["rows"][0].keys()),
    rows=t1_4["rows"],
    start_line_num=18
)
img_1_4.save(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\test_shot_1_4.png")
print("Saved test_shot_1_4.png")
