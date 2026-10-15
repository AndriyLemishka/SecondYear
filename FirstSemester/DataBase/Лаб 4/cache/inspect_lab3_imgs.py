from PIL import Image
import numpy as np

for name in ['img_0.png', 'img_1.png', 'img_3.png', 'img_4.png']:
    im = Image.open(f'd:/Studing/SecondYear/FirstSemester/DataBase/Лаб 4/cache/lab3_imgs/{name}')
    arr = np.array(im)
    print(name, im.size, 'Top left pixel:', arr[10, 10][:3], 'Center pixel:', arr[im.size[1]//2, im.size[0]//2][:3])
