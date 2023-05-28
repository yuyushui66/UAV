import os
dirct = 'train'
dirct1 = 'test'
dirList=[]
fileList=[]
saveDirTrain = 'list_train.txt'
saveDirTest = 'list_test.txt'
files=os.listdir(dirct)  #文件夹下所有目录的列表
files1 = os.listdir(dirct1)
print('files:',files)


# fileForWriteTrain = open(saveDirTrain, 'w')

# for name in files:
#     fileForWriteTrain.write(str(name) + '\n')

# fileForWriteTrain.close()

fileForWriteTest = open(saveDirTest, 'w')
for name in files1:
    fileForWriteTest.write(str(name) + '\n')
fileForWriteTest.close()