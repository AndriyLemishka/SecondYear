from PIL import Image
import numpy as np

im0 = Image.open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_0.png").convert("RGB")
arr0 = np.array(im0)

# Find the NULL badge in row 0 (y=317..338, x=350..420)
for y in range(317, 338):
    row_vals = [arr0[y, x] for x in range(350, 410)]
    dark = [x for x in range(350, 410) if arr0[y, x, 0] < 160]
    if dark:
        print(f"y={y}: dark x={min(dark)}..{max(dark)}")

# Find the blue dot in the SQL editor of im0 (y=75..230, x=60..80)
for y in range(75, 230):
    blues = [x for x in range(60, 80) if arr0[y, x, 2] > 180 and arr0[y, x, 0] < 50]
    if blues:
        print(f"Blue dot at y={y}, x={min(blues)}..{max(blues)}")
