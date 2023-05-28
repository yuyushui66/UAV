import os
import shutil
import json


from PIL import Image as PILImage

count = 0
f = open("splitTestList.txt")
listTrain = []
for line in f:
    listTrain.append(line.strip())
f.close()


def moveFiles(path, disdir):  # path为原始路径，disdir是移动的目标目录
    # dirlist = os.listdir(path)
    for video in listTrain:
        frames = os.path.join(path, video)
        listFrames = os.listdir(frames)
        framesLabel = os.path.join(frames, "IR_label.json")
        data = []
        with open(framesLabel, "r") as file:
            data = json.load(file)
        # print(data)
        # tmp = 0  # 当做一个计数
        for frame in listFrames:
            if frame[-1] == "g":
                picName = video + frame
                shutil.copy(
                    os.path.join(path, video, frame), os.path.join(disdir, picName)
                )
                # picLabelName = picName.split("/")[-1]
                # picLabelName = picLabelName.split(".")[0] + ".txt"

                # image = PILImage.open(os.path.join(path, video, frame))

                # width, heigth = image.size
                # exist = data["exist"][tmp]
                # if exist == 1:
                #     gt_rect = data["gt_rect"][tmp]
                #     x = gt_rect[0]
                #     y = gt_rect[1]
                #     width_x = gt_rect[2]
                #     height_y = gt_rect[3]
                #     center_x = x + width_x / 2.0
                #     center_y = y + height_y / 2.0
                #     center_x = center_x / width
                #     center_y = center_y / heigth
                #     width_x = width_x / width
                #     height_y = height_y / heigth
                # else:
                #     center_x, center_y, width_x, height_y = 0, 0, 0, 0
                # with open(os.path.join(disdir, picLabelName), "w") as f:
                #     f.write(
                #         "{0} {1} {2} {3} {4}".format(
                #             exist, center_x, center_y, width_x, height_y
                #         )
                #     )
                # print(
                #     "{0} {1} {2} {3} {4}".format(
                #         exist, center_x, center_y, width_x, height_y
                #     )
                # )

                # tmp += 1

                # print(picName)

    # print(dirlist)
    # for i in dirlist:
    #     child = os.path.join('%s/%s' % (path, i))
    #     if os.path.isfile(child):

    #         imagename, jpg = os.path.splitext(i)	# 分开文件名和后缀
    #         shutil.copy(child, os.path.join(disdir, imagename + ".jpg"))
    #         # 复制后改为原来图片名称
    #         # 也可以用shutil.move()
    #         continue
    #     moveFiles(child, disdir)


if __name__ == "__main__":
    rootImage = "train"  # 原始图片文件父目录
    disdir = "splitTest"  # 移动到目标文件夹

    moveFiles(rootImage, disdir)
