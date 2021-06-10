# face-mosaic
## 一. 项目说明

基于Python3.6+mediapipe的人脸追踪马赛克程序，支持导入图片/视频或使用摄像头，界面使用PyQt5开发。

mediapipe官方文档：https://google.github.io/mediapipe/

你可以对该项目进行魔改，例如更换马赛克图片，或者加入批量处理视频功能等，发挥你的想象力和创造力！

## 二. 使用

1. 运行`main.py`文件。

2. 点击`文件->导入`，导入图片/视频，或点击`摄像头->打开`。

3. 点击`操作->开始打码`，可以在界面上实时查看打码情况。设置选项可以调节模糊程度。

   注意：支持图片/视频或摄像头追踪打码。处理视频时要选择压缩程序，处理完毕后新视频会导出到`video_output`目录下，新图片会生成在`middle_pic`文件夹中。

## 三. 界面展示

**主界面**

<img src="https://yun.515code.com/ipic/5f05884e.png" alt="主界面" style="zoom:67%;" />

**处理图片**

<img src="https://yun.515code.com/ipic/48d6917d.png" alt="处理图片效果" style="zoom:67%;" />

**处理视频**

<img src="https://yun.515code.com/ipic/64bc56db.png" alt="处理视频效果" style="zoom:67%;" />

## 四. 关于

我的博客：https://www.515code.com/