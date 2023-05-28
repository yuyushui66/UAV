import os
import numpy as np


from PIL import Image as PILImage

imageRoot = "splitTest"
YOLORes = "YOLORes"
dirRoot = "YOLODealData"

ansList = os.listdir(YOLORes)
for ans in ansList:
    imageName = ans.split(".")[0] + ".jpg"
    image = PILImage.open(os.path.join(imageRoot, imageName))
    width, heigth = image.size
    ansList = np.loadtxt(os.path.join(YOLORes, ans))
    x = ansList[1]
    y = ansList[2]
    width_x = ansList[3]
    height_y = ansList[4]
    x -= width_x / 2
    y -= height_y / 2
    x *= width
    y *= heigth
    width_x *= width
    height_y *= heigth
    with open(os.path.join(dirRoot, ans), "w") as f:
        f.write("{0} {1} {2} {3}".format(x, y, width_x, height_y))
