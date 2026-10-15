from PIL import Image
import numpy as np

im0 = Image.open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_0.png").convert("RGB")
arr0 = np.array(im0)

# Check at x=200 where white editor ends (around y=75..300)
for y in range(75, 350):
    c = arr0[y, 200]
    if tuple(c) != (255, 255, 255) and tuple(c) != (239, 239, 239):
        print(f"x=200 at y={y}: {c}")
