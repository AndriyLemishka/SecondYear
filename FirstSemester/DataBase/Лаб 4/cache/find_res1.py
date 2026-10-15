from PIL import Image
import numpy as np

im4 = Image.open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_4.png").convert("RGB")
arr4 = np.array(im4)

for y in range(635, 665):
    blues = [x for x in range(10, 100) if arr4[y, x, 2] > 180 and arr4[y, x, 0] < 50]
    if blues:
        print(f"Result 1 text at y={y}, x={min(blues)}..{max(blues)}")
