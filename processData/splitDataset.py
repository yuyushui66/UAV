import random
f=open('list_train.txt')
list1=[]
for line in f:
    list1.append(line.strip())
print(list1)
f.close()

listSplitForTrain = random.sample(list1, 125)
# print(len(listSplitForTrain))
# print(listSplitForTrain)
listSplitForTest = list(set(list1) - set(listSplitForTrain))
# print(len(listSplitForTest))
# print(listSplitForTest)


fileForWriteTest = open('splitTestList.txt', 'w')
for name in listSplitForTest:
    fileForWriteTest.write(str(name) + '\n')
fileForWriteTest.close()

fileForWriteTest = open('splitTrainList.txt', 'w')
for name in listSplitForTrain:
    fileForWriteTest.write(str(name) + '\n')
fileForWriteTest.close()