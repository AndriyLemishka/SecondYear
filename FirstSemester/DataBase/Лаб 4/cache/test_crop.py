from PIL import Image

im0 = Image.open(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\lab3_imgs\img_0.png")
im0.crop((0, 0, 998, 120)).save(r"d:\Studing\SecondYear\FirstSemester\DataBase\Лаб 4\cache\crop_im0_top.png")
print("Top cropped successfully")
