from PIL import Image
import numpy as np
import sys


# --------- Note ---------
# This converter supports different image formats (png, bmp, jpg...)
# --------- Input ---------
# python3 img.py input_image_file
# --------- Output ---------
# img: .word image_height image_width pixel[0][0] pixel[0][1] ...
# add file output with same name of image file

if len(sys.argv) != 2:
    exit()

with open(f"{(sys.argv[1])[:len(sys.argv[1])-4]}.txt", "w") as file:
    im = Image.open(sys.argv[1])
    p = np.array(im)
    file.write(f"img: .word {im.size[1]} {im.size[0]}")
    flag = True
    for l in p:
        for i in l:
            if flag:
                flag = False
            else:
                file.write(",")
            file.write(" 0x" + '{:08x}'.format(i[2] + i[1] * 16**2 + i[0] * 16**4))
    file.write("")