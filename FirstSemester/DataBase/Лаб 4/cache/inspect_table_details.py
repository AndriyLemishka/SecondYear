from PIL import Image, ImageDraw, ImageFont
import numpy as np
import re

im0_path = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_0.png"
im4_path = r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_4.png"

im0 = Image.open(im0_path).convert("RGB")
im4 = Image.open(im4_path).convert("RGB")

# Let's extract the exact NULL badge and row arrow from im0!
# In im0:
# First row is y=317..338. The triangle arrow '>' is in x=18..47, y=317..338.
# And NULL badge is in the 'Default' column of row 0 (y=317..338).
# Let's save a crop of the table area of im0 (x=15..600, y=290..400) to inspect exact pixel coords.
im0.crop((15, 290, 600, 400)).save(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\crop_im0_table.png")

# Also let's check the bottom-left Result tab in im4 (Result 1 x)
im4.crop((0, 630, 300, 675)).save(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\crop_im4_res1.png")
print("Saved table and tab crops")
