import os
import shutil

count = 0
f = open("list_test.txt")
listTest = []
for line in f:
    listTest.append(line.strip())
f.close()

for video in listTest:
    frames = os.listdir(os.path.join("test", video))
    for frame in frames:
        if frame[-1] == "g":
            frameName = video + frame
            shutil.copy(
                os.path.join("test", video, frame), os.path.join("testDeal", frameName)
            )
