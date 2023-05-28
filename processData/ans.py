import os
import json
import numpy as np
from PIL import Image as PILImage

ImagePath = "test"
TxtPath = "lastAns"
targetPath = "ansJson"

videos = os.listdir(ImagePath)
for video in videos:
    frames = os.listdir(os.path.join(ImagePath, video))
    ans = dict()
    ans["res"] = []
    for frame in frames:
        if frame[-1] == "g":
            txtName = frame.split(".")[0] + ".txt"
            txtName = video + txtName
            iou = np.loadtxt(os.path.join(TxtPath, txtName))[1:5]
            image = PILImage.open(os.path.join(ImagePath, video, frame))
            width, heigth = image.size
            x = iou[0]
            y = iou[1]
            width_x = iou[2]
            height_y = iou[3]
            x -= width_x / 2
            y -= height_y / 2
            x *= width
            y *= heigth
            width_x *= width
            height_y *= heigth
            ans["res"].append([x, y, width_x, height_y])
    jsonName = video + ".json"
    json_object = json.dumps(ans)

    with open(os.path.join(targetPath, jsonName), "w") as outfile:
        outfile.write(json_object)

    # picName = video + frame
    # picLabelName = picName.split("/")[-1]
    # picLabelName = picLabelName.split(".")[0] + ".txt"
