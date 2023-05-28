import os
import numpy as np
import matplotlib.pyplot as plt

groundtruth = "testgroundtruth"
predict = "YOLODealData"


def computeIOU(box1, box2):  # box1 is the groundtruth, box2 is the predicted
    box1[2], box1[3] = box1[0] + box1[2], box1[1] + box1[3]
    box2[2], box2[3] = box2[0] + box2[2], box2[1] + box2[3]
    in_h = min(box1[2], box2[2]) - max(box1[0], box2[0])
    in_w = min(box1[3], box2[3]) - max(box1[1], box2[1])
    inter = 0 if in_h < 0 or in_w < 0 else in_h * in_w
    if all(item == 0 for item in box1) or all(item == 0 for item in box2):
        return 0
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


def compute():
    framesCount = 0
    framesExistCount = 0
    res1 = 0
    res2 = 0
    resIou = 0
    txtList = os.listdir(predict)
    for txt in txtList:
        groTxt = os.path.join(groundtruth, txt)
        preTxt = os.path.join(predict, txt)
        groIou = np.loadtxt(groTxt)[1:5]
        preIou = np.loadtxt(preTxt)
        iouAns = computeIOU(groIou, preIou)
        vt = computePT(groIou)
        pt = computePT(preIou)
        if vt == 0:
            framesExistCount += 1
        framesCount += 1
        res1 += iouAns * vt + pt * (1 - vt)
        res2 += pt * vt
        # print("why", framesCount)
    acc = res1 / framesCount - 0.2 * (res2 / framesExistCount) ** 0.3
    print(acc)


if __name__ == "__main__":
    compute()
