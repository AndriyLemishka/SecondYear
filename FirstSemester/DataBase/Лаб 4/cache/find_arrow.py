from PIL import Image
import numpy as np

im0 = Image.open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_0.png").convert("RGB")
arr0 = np.array(im0)

for y in range(317, 338):
    darks = [x for x in range(18, 45) if arr0[y, x, 0] < 100]
    if darks:
        print(f"Arrow at y={y}, x={min(darks)}..{max(darks)}")
