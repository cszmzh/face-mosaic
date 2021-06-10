from PyQt5.QtGui import QPixmap
from window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog
from PyQt5 import QtGui, QtWidgets
import sys
import cv2
from face import FaceDetector
import time

"""
@author BA-NANA
@desc 基于Python的人脸跟踪打码程序
@date 2021/6/10
"""


def label_show(label, image):
    qt_img_buf = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    qt_img = QtGui.QImage(qt_img_buf.data, qt_img_buf.shape[1], qt_img_buf.shape[0], QtGui.QImage.Format_RGB32)
    image = QPixmap.fromImage(qt_img).scaled(label.width(), label.height())
    label.setPixmap(image)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.image_file = False
        self.setupUi(self)
        self.initUI()
        self.mosaic_level = 0.6  # 模糊程度
        self.detector = FaceDetector()
        self.videoFPS = 24
        self.image = False
        self.video = False
        self.video_name = False
        self.camera = False
        self.camera_selected = 0
        self.loop = False
        self.detect = False
        self.cap = None

    def print_log(self, log_words):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.textLog.append(current_time + ':' + log_words)  # 在指定的区域显示提示信息
        cursor = self.textLog.textCursor()
        self.textLog.moveCursor(cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()

    def initUI(self):
        self.setWindowTitle('基于Python的人脸追踪打码')
        self.actionLoadImage.triggered.connect(self.load_image)
        self.actionStart.triggered.connect(self.start_detect)
        self.actionLoadVideo.triggered.connect(self.load_video)
        self.actionVideoFPS.triggered.connect(self.change_video_fps)
        self.actionOpenCamera.triggered.connect(self.open_camera)
        self.actionCloseCamera.triggered.connect(self.close_camera)
        self.actionSelectedCamera.triggered.connect(self.select_camera)
        self.actionLoop.triggered.connect(self.loop_video)
        self.actionMosaicLevel.triggered.connect(self.change_mosaic_level)

    def load_image(self):
        image_name, image_type = QFileDialog.getOpenFileName(self, '打开图片', r'./', '图片 (*.png *.jpg *.jpeg)')
        if image_name == '':
            self.print_log(log_words=f'取消加载图片')
            return
        cv2_image = cv2.imread(image_name)
        label_show(label=self.labelImageOrVideo, image=cv2_image)
        self.image = True
        self.print_log(log_words=f'加载图片:{image_name}')
        self.image_file = cv2_image

    def load_video(self):
        video_name, video_type = QFileDialog.getOpenFileName(self, '打开视频', r'./', '视频 (*.avi *.mp4)')
        if video_name == '':
            self.print_log(log_words=f'取消加载视频')
            return
        self.cap = cv2.VideoCapture(video_name)
        self.video_name = video_name
        self.video = True
        self.print_log(log_words=f'加载视频:{video_name}')
        ret, cv2_image = self.cap.read()
        label_show(label=self.labelImageOrVideo, image=cv2_image)

    def loop_video(self):
        if self.loop:
            self.loop = False
            self.actionLoop.setText('视频循环 (关)')
        else:
            self.loop = True
            self.actionLoop.setText('视频循环 (开)')

    def start_detect(self):
        self.detect = True
        if self.image:
            rectangle, success = self.detector.rectangle(self.image_file, self.mosaic_level)
            if success:
                label_show(label=self.labelImageOrVideo, image=rectangle)
            else:
                self.print_log(log_words=f'无法定位人脸')

        if self.camera:
            self.print_log(log_words=f'正在使用摄像头检测')
            while True:
                ret, image = self.cap.read()
                if not ret:
                    break
                rectangle, success = self.detector.rectangle(image, self.mosaic_level)
                label_show(label=self.labelImageOrVideo, image=rectangle)
                cv2.waitKey(int(1000 / self.videoFPS))

        if self.video:
            self.print_log(log_words=f'正在检测视频')
            fps = int(round(self.cap.get(cv2.CAP_PROP_FPS)))
            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            # 输出打码视频
            out = cv2.VideoWriter('video_output/' + self.video_name.split('/')[-1], -1, fps, (width, height), True)
            while True:
                ret, image = self.cap.read()
                if not ret:
                    if self.loop:
                        self.cap = cv2.VideoCapture(self.video_name)
                        ret, image = self.cap.read()
                    else:
                        break
                rectangle, success = self.detector.rectangle(image, self.mosaic_level)
                out.write(rectangle)
                label_show(label=self.labelImageOrVideo, image=rectangle)
                cv2.waitKey(int(1000 / self.videoFPS))
            self.cap.release()
            out.release()
            self.print_log(log_words=f'该视频已处理完毕，请在video_output文件夹中查看！')

    def open_camera(self):
        camera = cv2.VideoCapture(self.camera_selected)
        self.cap = camera
        self.print_log(log_words=f'打开摄像头')
        while True:
            ret, cv2_image = camera.read()
            if not ret:
                break
            self.camera = True
            label_show(label=self.labelImageOrVideo, image=cv2_image)
            cv2.waitKey(int(1000 / self.videoFPS))

    def change_video_fps(self):
        number, ok = QInputDialog.getInt(self, "设置fps", "[10-60]")
        if number < 10 or number > 60:
            self.print_log(log_words=f'非法数值，设置失败')
            return
        self.videoFPS = number
        self.print_log(log_words=f'设置fps: {str(number)}')

    def close_camera(self):
        self.camera = False
        self.cap.release()
        self.print_log(log_words='摄像头已关闭')

    def select_camera(self):
        if self.camera_selected == 0:
            self.camera_selected = 1
            self.print_log(log_words='切换至摄像头: camera 1')
        else:
            self.camera_selected = 0
            self.print_log(log_words='切换至摄像头: camera 0')

    def change_mosaic_level(self):
        number, ok = QInputDialog.getDouble(self, "设置模糊程度", "[0.1-1] (默认0.6)")
        if number < 0.1 or number > 1:
            self.print_log(log_words=f'非法数值，设置失败')
            return
        self.mosaic_level = number
        self.print_log(log_words=f'设置模糊程度: {str(number)}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
