# UAV
# 目录文件说明
OStrack是OStrack的源码
yolov5是yolov5的源码
processData是我进行数据处理的代码，当然有部分数据处理代码也在OStrack与YOLOv5文件夹里面

由于上传至github的速度过慢，因此在训练过程中的过程文件都没有保留，至保留了源码和和部分训练日志文件

processData/ans.py 将最后的结果转化为老师作业要求的json形式
  
processData/computeAcc.py 计算OStrack的准确度

processData/computeAccYolo.py 计算机YOLO的准确度

processData/dealTest.py 生成YOLO的test的数据

processData/getyolodata.py 将数据处理成YOLO需要的数据

processData/getYoloTestdata.py 将训练集中的部分数据转化YOLO的测试数据

processData/labels.py 得到YOLO训练需要的labels

processData/splitDataset.py 分割训练集

processData/YOLOResData.py 处理YOLO的结果文件

OStrack/experiments OStrack的参数设置

OStrack/lib OStrack 的主要代码

OStrack/output OStrack 训练与测试输出文件，但是由于其中文件比较大，被删除，只保留了训练日志

OStrack/pretrained_models 预训练参数放置的位置

OStrack/tensorboard tensorboard文件

OStrack/tracking OStrack的主要启动代码

yolov5/models YOLO主要的参数配置

yolov5/runs 放置运行结果，但是由于文件过大，被删除

yolov5/train.py 训练部分主要程序

yolov5/detect.py 检测部分主要程序





