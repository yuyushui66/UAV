import os
import shutil
import json

path = "splitTest"
disdir = "labelsTest"
dirlist = os.listdir(path)
for f in dirlist:
    if f[-1] == "t":
        shutil.move(os.path.join(path, f), os.path.join(disdir, f))

        # shutil.copy(f, os.path.join(disdir, picLabelName))
