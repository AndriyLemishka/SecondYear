from PIL import Image
import numpy as np

im0 = Image.open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_0.png").convert("RGB")
arr0 = np.array(im0)

# Find where white editor starts and ends in im0 at x=400
for y in range(im0.height):
    c = arr0[y, 400]
    if y < 100 and tuple(c) == (255, 255, 255):
        print(f"im0 editor top at y={y}")
        break

# Find where editor ends (around y=200..300)
for y in range(100, 350):
    c = arr0[y, 400]
    if tuple(c) != (255, 255, 255) and tuple(c) != (239, 239, 239):
        print(f"im0 editor non-white at y={y}: {c}")
