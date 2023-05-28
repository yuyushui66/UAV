import os
import json
import pandas as pd
import matplotlib.pyplot as plt


groundtruth = "train"
predict = "ans3"


def computeIOU(box1, box2):  # box1 is the groundtruth, box2 is the predicted
    box1[2], box1[3] = box1[0] + box1[2], box1[1] + box1[3]
    box2[2], box2[3] = box2[0] + box2[2], box2[1] + box2[3]
    in_h = min(box1[2], box2[2]) - max(box1[0], box2[0])
    in_w = min(box1[3], box2[3]) - max(box1[1], box2[1])
    inter = 0 if in_h < 0 or in_w < 0 else in_h * in_w
    union = (
        (box1[2] - box1[0]) * (box1[3] - box1[1])
        + (box2[2] - box2[0]) * (box2[3] - box2[1])
        - inter
    )
    iou = inter / union
    return iou


def computePT(iou):
    if all(item == 0 for item in iou):
        return 1
    else:
        return 0


def getans():
    anslist = os.listdir(predict)
    ans = []
    for txt in anslist:
        if txt[-8:-4] != "time":
            ans.append(txt)
    return ans


def getDirName(tmp):
    pass


def compute():
    ans = getans()
    framesCount = 0
    framesExistCount = 0
    res1 = 0
    res2 = 0
    resIou = 0
    for pre in ans:
        groundtruthDir = os.path.join(groundtruth, pre.split(".")[0])
        preDir = os.path.join(predict, pre)
        groundtruthjson = os.path.join(groundtruthDir, "IR_label.json")
        groundTruthData = []
        with open(groundtruthjson, "r") as file:
            groundTruthData = json.load(file)
        groundTruthIOU = groundTruthData["gt_rect"]
        groundTruthLabels = groundTruthData["exist"]
        count = 0  # the count of the current frames

        df = pd.read_csv(preDir, sep="\t")
        iouList = []
        tmp = 0
        framesIOU = 0
        for iou in df.values:
            iouAns = computeIOU(groundTruthIOU[count], iou)
            tmp += 1
            iouList.append(iouAns)
            print(iouAns)
            resIou += iouAns
            framesIOU += iouAns
            vt = int(groundTruthLabels[count])
            pt = computePT(iou)
            if vt == 1:
                framesExistCount += 1
            framesCount += 1
            res1 += iouAns * vt + pt * (1 - vt)
            res2 += pt * vt
        x = [i for i in range(1, len(iouList) + 1)]
        framesIOU /= tmp
        plt.plot(x, iouList)
        plt.title(str(framesIOU))
        plt.savefig("ansPic/" + str(framesIOU) + ".jpg")

    acc = res1 / framesCount - 0.2 * (res2 / framesExistCount) ** 0.3
    print(iouAns / framesCount)
    return acc


if __name__ == "__main__":
    print(compute())
    # print(compute())
