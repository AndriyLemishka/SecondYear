from PIL import Image
import numpy as np

im = Image.open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_4.png").convert("RGB")
arr = np.array(im)

# Search for the "Result Grid" text or horizontal dividers
# In column 50, let's see color changes
print("Column 50 color transitions:")
prev_c = arr[0, 50]
for y in range(0, im.height, 5):
    c = arr[y, 50]
    if np.max(np.abs(c.astype(int) - prev_c.astype(int))) > 30:
        print(f"y={y}: color={c}")
        prev_c = c
