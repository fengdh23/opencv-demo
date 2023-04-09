# demo: https://www.bilibili.com/video/BV18F411W7y2/?spm_id_from=333.337.search-card.all.click&vd_source=48ac9228f953e9e82ee581faae1b1437
import time

import cv2
import numpy as np
from PySide6 import QtGui
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap, QImage
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from ui_demo import Ui_MainWindow


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
class MainWinow(QMainWindow):  # 继承 QMainWindow
    def __init__(self):  # 初始化
        super(MainWinow, self).__init__()
        self.showImage = None
        self.frame = None
        self.camera_timer = None
        self.ui = Ui_MainWindow()  # UI 类的实例化
        self.ui.setupUi(self)  # 界面初始化
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.ui.show_camera.setScaledContents(True)  # 图片自适应
        self.ui.show_image.setScaledContents(True)

        self.band()

    def band(self):
        # 自定义信号.属性名1.connect(__FUNCTION__)
        # 自定义信号.属性名2.connect(__FUNCTION__)
        # 自定义信号.属性名3.connect(__FUNCTION__)
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.show_camera)

        # 信号与操作绑定
        self.ui.open_camera.clicked.connect(self.open_camera)  # 调用槽函数
        self.ui.close_camera.clicked.connect(self.close_camera)  # 调用槽函数
        self.ui.capture.clicked.connect(self.capture)  # 调用槽函数

        self.ui.select_file.clicked.connect(self.pickImage)  # 调用槽函数
        self.ui.checkColor.clicked.connect(self.checkColor)  # 调用槽函数

    def open_camera(self):
        self.cap = cv2.VideoCapture(0)  # 选择模式摄像头 0
        if self.cap.isOpened():
            self.camera_timer.start(40)  # 每 40 毫秒读取一次，刷新率为 1000 // 40 = 25 太大，卡
            self.show_camera()
        else:
            QMessageBox.critical(self, "Please", '摄像头未打开')
        return None

    ''' 打开摄像头 '''

    def show_camera(self):
        flag, self.frame = self.cap.read()  # 视频里读取图片

        if not flag :
            print("无法读取图片,请检查设备")

        # image_show = cv2.resize(self.frame, (1280, 720))  # 调整大小
        width, height = self.frame.shape[:2] # 480*640
        image_show = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  # TODO 为什么要转成RGB

        image_show = cv2.flip(image_show, 1)  # 水平反转(摄像头拍到的是镜像)
        #
        self.showImage = QtGui.QImage(image_show.data, height, width, QImage.Format.Format_RGB888)
        self.ui.show_camera.setPixmap(QPixmap.fromImage(self.showImage))  # 视频的 label 显示图片
        self.ui.show_camera.setScaledContents(True) # TODO 放大了？

    ''' 拍照 '''

    def capture(self):
        if self.cap.isOpened():
            FName = fr"images/cap{time.strftime('%Y%m%d%H%M%S', time.localtime())}"
            print(FName)
            self.ui.show_image.setPixmap(QPixmap.fromImage(self.showImage))  # 视频的 label 显示图片
            self.ui.show_image.setScaledContents(True)
            bool_suc = self.showImage.save(FName + ".jpg", 'JPG', 100) # 100指的是图片的质量因数，范围必须在0到100之内或-1，指定0以获取小型压缩文件，指定100表示大型未压缩文件，使用-1（默认值）使用默认设置。
            # bool_suc = self.showImage.save('./1.jpg')
            print("保存:" + str(bool_suc))
        else:
            QMessageBox.critical(self, "Please", '摄像头未打开')
            return None

    def close_camera(self):
        self.camera_timer.stop()
        self.cap.release()
        self.ui.show_camera.clear()
        self.ui.show_image.clear()
        self.ui.show_camera.setText('摄像头')

    def pickImage(self):
        # 父窗口对象 标题  起始目录
        # folder_name = QFileDialog.getExistingDirectory(self.ui, "选择文件夹", "../")
        # fname,_ = QFileDialog.getOpenFileNames(self,'Open Image','../','Image Files (*.png *.jpg *.bmp)')
        # 创建一个QFileDialog对象
        file_dialog = QFileDialog()
        # 设置文件对话框的标题和过滤器
        file_dialog.setWindowTitle("选择图片")
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.bmp)")
        # 显示文件对话框，并获取用户选择的文件路径
        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_file = file_dialog.selectedFiles()[
                0]  # selectedFiles() 方法返回一个列表，因为用户可以选择多个文件。在这个例子中，我们只获取了列表中的第一个文件路径
            print("您选择的文件路径是：", selected_file)  # C:/Users/fdh32/Pictures/1-blue.png
            self.ui.check_result.setText(selected_file)
            # 图片
            # self.ui.show_image.setPixmap(cv2.imread(selected_file))
            # self.ui.show_image.setPixmap(QtGui.QImage(selected_file)) # 大小异常?
            self.ui.show_image.setPixmap(QPixmap(selected_file))  # 窗口随图片大小变化

    def checkColor(self):
        # 检查图片 获取图片
        image_path = self.ui.check_result.text()
        img = cv2.imread(image_path)  # 读取图像格式为b,g,r

        # 获取图像的宽度和高度
        height, width = img.shape[:2]

        # 计算裁剪区域的左上角坐标和右下角坐标
        x1 = int(width / 2 - 20)
        x2 = int(width / 2 + 20)
        y1 = 0
        y2 = height

        # 使用cv2.crop函数进行裁剪
        cropped_img = img[y1:y2, x1:x2]

        ccropped_img = cropped_img.copy()  # .copy() 否则报错
        # 颜色 失真严重？？ https://blog.csdn.net/weixin_46186673/article/details/122131261
        qimage = QtGui.QImage(ccropped_img, ccropped_img.shape[1], ccropped_img.shape[0],
                              QtGui.QImage.Format.Format_BGR888)
        # 显示 裁剪后的图片
        self.ui.show_image.setPixmap(QPixmap(qimage))  # TODO 如何不放大 窗口随图片大小变化
        self.ui.show_image.setScaledContents(False)

        color_counts, colors = get_dominant_color(cropped_img)
        if color_counts >= 2:
            # 调用 opencv 颜色隔离
            self.ui.check_result.setScaledContents(True)
            self.ui.check_result.setText('分离:' + colors)
        else:
            self.ui.check_result.setText('分离:' + colors)


def get_dominant_color(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color = ("黑色", "红色", "绿色", "蓝色", "黄色", "洋红色", "青色")
    # hsv color 格式
    boundaries = [([0, 0, 0], [180, 255, 15]),  # 黑色
                  ([0, 43, 46], [10, 255, 255]),  # 红色
                  ([35, 43, 46], [77, 255, 255]),  # 绿色
                  ([110, 43, 46], [130, 255, 255]),  # 蓝色
                  ([20, 70, 50], [30, 255, 255]),  # 黄色
                  ([150, 43, 46], [170, 255, 255]),  # 洋红色
                  ([78, 43, 46], [99, 255, 255])]  # 青色
    index = -1
    count = 0
    colors = ""
    for (lower, upper) in boundaries:
        index = index + 1
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # 根据颜色范围识别颜色 0 不匹配;匹配是1 输出的二值化图像
        mask = cv2.inRange(image, lower, upper)
        # cv2.medianBlur(mask_yellow, 7)  # 中值滤波
        mask_NonZero = cv2.countNonZero(mask)
        if mask_NonZero == 0:
            print("模糊匹配--不匹配")
            continue
        else:
            count = count + 1
            colors = colors + (color[index]) + "|"
            print("模糊匹配到的颜色 1111 " + color[index] + "")
        # output = cv2.bitwise_and(image, image, mask=mask) # 函数将输入图像和二值化图像进行按位与操作，得到包含目标颜色的部分
        # TODO 统计识别到的颜色的比例 为什么要除以 3
        # ratio = mask_NonZero / (image.size / 3)
        # if ratio > 0.01:
        #     count = count + 1
        #     print("精确匹配到的颜色 2222 " + color[index] + "")
        # return count
        # return color[boundaries.index((lower, upper))]
    print("模糊匹配颜色数量", count)
    print("模糊匹配颜色", colors)
    return count, colors


if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication([])  # 启动一个应用
    window = MainWinow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序退出
