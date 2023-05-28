#!/root/miniconda3/bin/python
import os
import os.path
import pandas
import csv
import json

root = '/root/autodl-tmp/ostrack/OSTrack-main/data/UAV/train'
path = '/root/autodl-tmp/ostrack/OSTrack-main/data/UAV/train/splitTestList.txt' # 当前UAVtrain数据所在目录 多于了

with open(path) as f:
    dir_list = list(csv.reader(f))
dir_list = [dir_name[0] for dir_name in dir_list]
print(dir_list)

for frame in dir_list:
    IR_label_file = os.path.join(root, frame, "IR_label.json")
    f = open(IR_label_file, 'r')
    tmp = f.read()
    label = json.loads(tmp)
    l = ''
    f1 = open(os.path.join(root, frame, 'groundtruth.txt'), 'w')
    for num in label["gt_rect"][0]:
        l += "{}".format(num) + ','
    l = l[0:-1]
    #print(l)
    f1.write(l)
    # print(label["res"][0])



