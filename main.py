import matplotlib.pyplot as plt
# 设置字体格式
from matplotlib import rcParams
from matplotlib.ticker import MultipleLocator

# 全局字体大小
size = 14

# 设置英文字体
config = {
    "font.family": 'serif',
    "font.size": size,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}

# 过rc参数可以修改默认的属性，包括窗体大小、每英寸的点数、线条宽度、颜色、样式、坐标轴、坐标和网络属性、文本、字体等。
rcParams.update(config)

# 设置中文宋体
fontcn = {'family': 'SimSun', 'size': 10}
label_size = size
text_size = size

# YOLOv4数据
YOLOv4_mAP = [41.2,43.0,43.5]
YOLOv4_FPS = [54.2,50.5,46.1]

# EfficientDet数据
EfﬁcientDet_mAP = [33.8,39.6,43.0,45.8]
EfﬁcientDet_FPS = [98.0,74.1,56.5,34.5]

# YOLOv5数据
YOLOv5_mAP = [44.5,48.2,50.4]
YOLOv5_FPS = [90.1,73.0,62.5]

# PPYOLOE数据
PPYOLOE_mAP = [43.1,48.9,51.4,52.2]
PPYOLOE_FPS = [208.3,123.4,78.1,45.0]

# YOLOX数据
YOLOX_mAP = [46.4,50.0,51.2]
YOLOX_FPS = [81.3,69.0,57.8]

# Demo数据
Demo_mAP = [46.8,51.0,53.8]
Demo_FPS = [81.7,69.6,58.1]

# 自定义一些参数值
lw = 2
ms = 8
my_text = ['N', 'S', 'M', 'L', 'X']

# 绘制 mAP-Param
plt.figure(figsize=(6.4, 4.8))
# 绘制YOLOv4曲线图
plt.plot(
         YOLOv4_FPS, # 横坐标数据
         YOLOv4_mAP, # 纵坐标数据
         label='YOLO4', # label为图例名称
         c='b', # 线条以及坐标点图形的颜色
         linewidth=lw,
         marker='^', # 坐标点处图形的形状
         markersize=ms, # 图形的尺寸（大小）
         ls='-' # 线条的样式
         )

# 绘制EfﬁcientDet曲线图
plt.plot(EfﬁcientDet_FPS, 
         EfﬁcientDet_mAP, 
         label='EfﬁcientDet', 
         c='r',
         linewidth=lw,
         marker='o',
         markersize=ms,
         ls='-')

# 绘制YOLOv5曲线图
plt.plot(YOLOv5_FPS, 
         YOLOv5_mAP, 
         label='YOLOv5', 
         c='gray',
         linewidth=lw,
         marker='X',
         markersize=ms,
         ls='-')

# 绘制PPYOLOE曲线图
plt.plot(PPYOLOE_FPS, 
         PPYOLOE_mAP, 
         label='PPYOLOE', 
         c='purple',
         linewidth=lw,
         marker='x',
         markersize=ms,
         ls='-')

# 绘制YOLOX曲线图
plt.plot(YOLOX_FPS, 
         YOLOX_mAP, 
         label='YOLOX', 
         c='brown',
         linewidth=lw,
         marker='D',
         markersize=ms,
         ls='-')

# 绘制Demo曲线图
plt.plot(Demo_FPS, 
         Demo_mAP,
         label='Demo', 
         c='g',
         linewidth=lw,
         marker='*',
         markersize=10,
         ls='-')

plt.legend(loc='lower left', prop=fontcn)

# 横纵坐标名称
plt.ylabel('$\mathrm{AP}$', fontsize=label_size)
plt.xlabel('$\mathrm{FPS}$', fontsize=label_size)

# 设置坐标轴间隔
x_major_locator = MultipleLocator(10)
y_major_locator = MultipleLocator(5)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
# 设置横坐标范围
plt.xlim([30, 130])
# 设置纵坐标范围
plt.ylim([30, 55])

# 坐标点标记文字
# plt.text(my_param[0] - 3.5, my_mAP[0] + 0.8, my_text[0], color="k", fontsize=text_size)
# plt.text(my_param[1] - 2, my_mAP[1] + 0.8, my_text[1], color="k", fontsize=text_size)
# plt.text(my_param[2] - 2, my_mAP[2] + 0.8, my_text[2], color="k", fontsize=text_size)
# plt.text(my_param[3] - 3, my_mAP[3] + 1.0, my_text[3], color="k", fontsize=text_size)
# plt.text(my_param[4] - 2, my_mAP[4] + 0.8, my_text[4], color="k", fontsize=text_size)

# 设置网格线的风格：
  # -:实线
  # --:虚线
plt.grid(linestyle='-')

# 设置标题
plt.title(label = "MS COCO Object Detection")

# 保存高清图片
plt.savefig("./test.png",dpi=300)
# 在窗口中展示绘图
plt.show()
# 释放系统资源
plt.close()