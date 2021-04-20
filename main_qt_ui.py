from PIL import Image as PIm
from PIL import ImageDraw as PID
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QMetaObject, QModelIndex, QStringListModel
from PyQt5.QtWidgets import QBoxLayout, QFileDialog, QFrame, QGraphicsPixmapItem, QGraphicsScene, QGraphicsView, QLabel, QLayout, QLineEdit, QListView, QListWidget, QMessageBox, QPushButton, QApplication, QHBoxLayout, QMainWindow, QPushButton, QStatusBar, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QImage, QPixmap
import os
import cv2
import ope
import sys
import time


class Ui_Form(QFrame):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.py_path=os.path.dirname(os.path.abspath(sys.argv[0]))

        self.opt = ope.Bond_Ope()
        
        self.method='ocr'

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 720)
        # -----------------------------------------------------------------------
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_top = QHBoxLayout()
        self.layout_top.setObjectName(u"layout_top")
        self.lineEdit_filepath = QLineEdit(Form)
        self.lineEdit_filepath.setObjectName(u"lineEdit_filepath")

        self.layout_top.addWidget(self.lineEdit_filepath)

        self.btn_path = QPushButton(Form)
        self.btn_path.setObjectName(u"btn_path")

        self.layout_top.addWidget(self.btn_path)

        self.btn_std = QPushButton(Form)
        self.btn_std.setObjectName(u"btn_std")

        self.layout_top.addWidget(self.btn_std)

        self.btn_ocr = QPushButton(Form)
        self.btn_ocr.setObjectName(u"btn_ocr")

        self.layout_top.addWidget(self.btn_ocr)

        self.btn_bat = QPushButton(Form)
        self.btn_bat.setObjectName(u"btn_bat")

        self.layout_top.addWidget(self.btn_bat)

        self.verticalLayout.addLayout(self.layout_top)

        self.layout_bottom = QHBoxLayout()
        self.layout_bottom.setObjectName(u"layout_bottom")
        self.layout_bottom_left = QVBoxLayout()
        self.layout_bottom_left.setObjectName(u"layout_bottom_left")
        self.label_filelist = QLabel(Form)
        self.label_filelist.setObjectName(u"label_filelist")

        self.layout_bottom_left.addWidget(self.label_filelist)

        self.listWidget_file = QListWidget(Form)
        self.listWidget_file.setObjectName(u"listWidget_file")

        self.layout_bottom_left.addWidget(self.listWidget_file)

        self.layout_bottom.addLayout(self.layout_bottom_left)

        self.layout_bottom_right = QVBoxLayout()
        self.layout_bottom_right.setObjectName(u"layout_bottom_right")
        self.label_result = QLabel(Form)
        self.label_result.setObjectName(u"label_result")

        self.layout_bottom_right.addWidget(self.label_result)

        self.lineEdit_result = QLineEdit(Form)
        self.lineEdit_result.setObjectName(u"lineEdit_result")

        self.layout_bottom_right.addWidget(self.lineEdit_result)

        self.graphicsView_pic = QGraphicsView(Form)
        self.graphicsView_pic.setObjectName(u"graphicsView_pic")

        self.layout_bottom_right.addWidget(self.graphicsView_pic)

        self.layout_bottom.addLayout(self.layout_bottom_right)

        self.verticalLayout.addLayout(self.layout_bottom)

        # -------------------------------------------------------------------------------

        self.dir_path = ''

        self.retranslateUi(Form)

        self.bindFunc(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate(
                "Form", u"\u503a\u5238\u6587\u672c\u8bc6\u522b", None))
        self.btn_path.setText(
            QCoreApplication.translate("Form", u"\u9009\u62e9\u8def\u5f84",
                                       None))
        self.btn_ocr.setText(
            QCoreApplication.translate("Form", u"\u6587\u672c\u8bc6\u522b",
                                       None))
        self.btn_std.setText(
            QCoreApplication.translate("Form", u"\u6587\u672c\u68c0\u6d4b",
                                       None))
        self.btn_bat.setText(
            QCoreApplication.translate("Form", u"\u6279\u91cf\u5904\u7406",
                                       None))
        self.label_filelist.setText(
            QCoreApplication.translate("Form", u"\u6587\u4ef6\u5217\u8868",
                                       None))
        self.label_result.setText(
            QCoreApplication.translate("Form", u"\u8bc6\u522b\u7ed3\u679c",
                                       None))

    def bindFunc(self, Form):
        self.btn_path.clicked.connect(self.get_filepath)
        self.btn_ocr.clicked.connect(self.ocr)
        self.btn_std.clicked.connect(self.std)
        self.btn_bat.clicked.connect(self.bat)

    # retranslateUi

    def AddListitem(self, item):
        # self.check()
        self.listWidget_file.addItem(item)
    
    def show_result_in_lineEdit(self,context):
        self.lineEdit_result.setText(context)

    def show_pic_in_gra(self,  img_filepath):
        img = cv2.imread(img_filepath)                             #读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                 #转换图像通道
        x = img.shape[1]                                           #获取图像大小
        y = img.shape[0]                                           #图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)                       #创建像素图元
        self.scene = QGraphicsScene()                              #创建场景
        self.scene.addItem(self.item)
        self.graphicsView_pic.setScene(self.scene)

    def ocr(self, Form):
        text_list = self.listWidget_file.selectedItems()
        for text in list(text_list):
            # print(text.text())
            # print(self.dir_path+'/'+text.text())
            open_file_path=self.dir_path + '/' + text.text()
            self.show_pic_in_gra(img_filepath=open_file_path)
            # img = cv2.imread(self.dir_path + '/' + text.text())     #读取图像
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)              #转换图像通道
            # x = img.shape[1]                                        #获取图像大小
            # y = img.shape[0]
            # self.zoomscale = 1                                      #图片放缩尺度
            # frame = QImage(img, x, y, QImage.Format_RGB888)
            # pix = QPixmap.fromImage(frame)
            # self.item = QGraphicsPixmapItem(pix)                    #创建像素图元
            # #self.item.setScale(self.zoomscale)
            # self.scene = QGraphicsScene()                           #创建场景
            # self.scene.addItem(self.item)
            # self.graphicsView_pic.setScene(self.scene)

            self.show_result_in_lineEdit(
                self.opt.get_context(imagepath=self.dir_path + '/' +
                                     text.text()))

    def std(self, Form):
        self.method='std'
        # 获取当前选中
        text_list = self.listWidget_file.selectedItems()
        for text in list(text_list):
            # 检测bbox
            bbox_info_list = self.opt.get_bbox(self.dir_path + '/' +
                                               text.text())
            # print(self.opt.get_bbox(self.dir_path+'/'+text.text()))
            # self.lineEdit_result.setText(''.join(bbox[0]))

            # 生成一个可以用来画画的背景
            self.image = PIm.open(self.dir_path + '/' + text.text())
            draw = PID.Draw(self.image)
            for box_info in bbox_info_list:
                info_box = box_info['box']
                # crp_img = box_info['cropped_img']
                # 获取一系列的坐标
                x1, y1 = info_box[0, 0], info_box[0, 1]
                x2, y2 = info_box[1, 0], info_box[1, 1]
                x3, y3 = info_box[2, 0], info_box[2, 1]
                x4, y4 = info_box[3, 0], info_box[3, 1]
                draw.polygon([(x1, y1), (x4, y4), (x3, y3), (x2, y2)],
                             outline=(255, 0, 0))
            self.image.save('./temp.jpg')
            open_file_path =  self.py_path+ '\\temp.jpg'
            
            self.show_pic_in_gra(img_filepath=open_file_path)

    def bat(self, Form):
        if self.method == 'ocr':
            # 一条一条的操作
            for item in self.opt.get_single_img_path(dirpath=self.dir_path):
                # 识别
                context=self.opt.get_context(self.dir_path+'/'+item)
                if context=='by_hand':
                    pass
                else:
                    with open('result.txt',mode='a',encoding='utf-8') as f:
                        # 写入
                        f.write(item+',  {}'.format(context)+'\n')
            QMessageBox.information(self,"提示",self.tr("处理完成!!!"))
            
            
        elif self.method == 'std':
            for item in self.opt.get_single_img_path(dirpath=self.dir_path):
                self.show_result_in_lineEdit('正在处理: {}'.format(item))
                print('正在处理: {}'.format(item))
                # time.sleep(2)
                bbox_info_list=self.opt.get_bbox(self.dir_path+'/'+item)
                # print(bbox_list)
                if not os.path.exists('./result'):
                    os.mkdir('./result')
                for box_info in bbox_info_list:
                    info_box=box_info['box']
                    x1, y1 = info_box[0, 0], info_box[0, 1]
                    x2, y2 = info_box[1, 0], info_box[1, 1]
                    x3, y3 = info_box[2, 0], info_box[2, 1]
                    x4, y4 = info_box[3, 0], info_box[3, 1]
                    # print([x1,y1,x2,y2,x3,y3,x4,y4])
                    with open('./result/{}.txt'.format(item.split('.')[0]),mode='a',encoding='utf-8') as f:
                        f.write('{}, {}, {}, {}, {}, {}, {}, {}'.format(x1,y1,x2,y2,x3,y3,x4,y4)+'\n')
            QMessageBox.information(self,"提示",self.tr("处理完成!!!"))
        else:
            self.show_result_in_lineEdit('模式错误')

    def get_filepath(self, Form):
        try:
            self.listWidget_file.clear()
            # self.listWidget_file.maximumSize(w=200,h=200)
            self.dir_path = QFileDialog.getExistingDirectory(self, "选择路径")
            print('选择路径: '+self.dir_path)
            self.lineEdit_filepath.setText(self.dir_path)
            # print(self.opt.get_single_img_path(dirpath=self.dir_path))
            for item in self.opt.get_single_img_path(dirpath=self.dir_path):
                self.AddListitem(item=item)
                print('Add from this dirpath : ',item)
        except:
            print("请选择路径!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 导入图标

    main = Ui_Form()
    # 显示窗口
    main.show()
    # 建立循环
    sys.exit(app.exec_())