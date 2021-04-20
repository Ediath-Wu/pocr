import tkinter as tk
from tkinter import Entry, OptionMenu, StringVar, filedialog
from tkinter.constants import ANCHOR, CENTER, DISABLED, E, HIDDEN, W
import os
import ope

from PIL import Image as imim
from PIL.ImageTk import PhotoImage as PII




from tkinter.filedialog import askdirectory

from tkinter.dialog import *


class Bond_Img(tk.Frame):
    # 第1步，实例化object，建立窗口master
    def __init__(self,master=None) -> None:
        
        super().__init__(master)
        self.master=master
        self.master.title('债券文本识别工具')
        self.master.geometry('800x600')
        # 提供ocr和std功能
        self.opt=ope.Bond_Ope()
        self.pack()
        # 存放图片的文件夹的路径
        self.dirpath=StringVar()
        # 存放图片识别的结果
        self.context=StringVar()
        # 存放单张图片的地址
        self.img_file_path=StringVar()
        
        self.create_widgets()
        
        # self.func1=func1
        # self.func2=func2

    # # 第4步，在图形界面上设定标签
    # l = tk.Label(master, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
    # # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    # # 第5步，放置标签
    # l.pack()    # Label内容content区域放置位置，自动调节尺寸
    # # 放置lable的方法有：1）l.pack(); 2)l.place();
    
    def put_label(self):
        # self.label1=tk.Label(text='更改路径')
        # self.label1.grid(row=0,column=0,columnspan=9)
        # self.label2=tk.Label(text='文本识别')
        # self.label2.grid(row=0,column=9,columnspan=2)
        # self.label3=tk.Label(text='文本区域检测')
        # self.label3.grid(row=0,column=11,columnspan=2)
        pass



    
    def get_dirpath(self):
        try:
            self.lb1.delete(tk.FIRST,tk.END)
        except:
            pass
        dirpath=filedialog.askdirectory()
        self.dirpath.set(dirpath)
        temp=[]
        temp=self.opt.get_single_img_path(dirpath)
        for item in temp:
            self.lb1.insert(tk.END,item)
        
    def ocr(self):
        # 用于识别单个文件的内容
        # print(self.lb1.get(self.lb1.curselection()[0]))
        # print(self.dirpath.get())
        # print(type(self.lb1.get(self.lb1.curselection()[0])))
        self.img_file_path.set(self.dirpath.get()+'/'+self.lb1.get(self.lb1.curselection()[0]))
        # print(self.img_file_path.get())
        # print(self.opt.get_context(self.img_file_path.get())[0])
        temp_context=self.opt.get_context(self.img_file_path.get())
        self.context.set(temp_context)
        # print(self.lb1.get(self.lb1.curselection()[0]))
        # print(self.img_file_path.get())
        # print(type(self.img_file_path.get()))
        img_open=imim.open(self.img_file_path.get())

        img_png=PII(image=img_open)
        print(type(img_png))
        
        self.label3=tk.Label(self,background='red')
        self.label3.grid(row=2,column=3,rowspan=9,columnspan=15,sticky='wsen')

        # self.label3=tk.Label(self,image=img_png)
        # self.label3.grid(row=2,column=3,rowspan=9,columnspan=15,sticky='wsen')
        

        # self.context=self.opt.get_context(imgfile_path)


    def std(self):
        # 用于识别单个图片文件中的bbox
        # 调用ope中的std
        
        pass
    def ocrs_and_stds(self):
        pass


        # 注意，loop因为是循环的意思，master.mainloop就会让master不断的刷新，
        # 如果没有mainloop,就是一个静态的master,传入进去的值就不会有循环，
        # mainloop就相当于一个很大的while循环，有个while，
        # 每点击一次就会更新一次，所以我们必须要有循环
        # 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
    def get_filename(self):
        filename=filedialog.askopenfilename()
        # print(type(dirname))
        filename_=StringVar()
        filename_.set(filename)
        self.filepath_Entry['textvariable']=filename_

    def create_widgets(self):
        
        # self.fm1=tk.Frame(self)
        # self.fm1.grid()
        # self.fm2=tk.Frame(self)
        # self.fm2_left=tk.Frame(self.fm2)
        # self.fm2_right=tk.Frame(self.fm2)
        # self.fm2_right_top=tk.Frame(self.fm2_right)
        # self.fm2_right_bottom=tk.Frame(self.fm2_right)
        
        # 放置所有的按钮
        self.btn1=tk.Button(self,text='选择路径',width=10,height=1,command=self.get_dirpath)
        self.btn1.grid(row=0,column=9,columnspan=2,sticky='wsen')
        self.btn2=tk.Button(self,text='文本检测',width=10,height=1,command=self.std)
        self.btn2.grid(row=0,column=11,columnspan=2,sticky='wsen')
        self.btn3=tk.Button(self,text='文字识别',width=10,height=1,command=self.ocr)
        self.btn3.grid(row=0,column=13,columnspan=2,sticky='wsen')
        self.btn3=tk.Button(self,text='批量处理',width=10,height=1,command=self.ocrs_and_stds)
        self.btn3.grid(row=0,column=15,columnspan=2,sticky='wsen')
        
        
        
        # 放置标签
        self.label1=tk.Label(self,text='文件列表')
        self.label1.grid(row=1,column=0,rowspan=1,columnspan=2,sticky='wsen')
        self.label2=tk.Label(self,text='识别结果')
        self.label2.grid(row=1,column=2,rowspan=1,columnspan=2,sticky='wsen')
        # self.label3=tk.Label(self)
        # self.label3.grid(row=2,column=3,rowspan=9,columnspan=15,sticky='wsen')
        
        # 放置输入路径的文本框
        self.entry1=tk.Entry(self,textvariable=self.dirpath,state='readonly')
        self.entry1.grid(row=0,column=0,rowspan=1,columnspan=9,sticky='wsen')
        self.entry2=tk.Entry(self,textvariable=self.context,state='readonly')
        self.entry2.grid(row=1,column=5,rowspan=1,columnspan=12,sticky='wsen')
        
        self.sb=tk.Scrollbar(self)
        self.sb.grid(row=2,column=2,rowspan=9,columnspan=1,sticky='wsen')
        
        
        # 放置 列表 用于显示文件
        self.lb1=tk.Listbox(self,yscrollcommand=self.sb.set)
        self.lb1.grid(row=2,column=0,rowspan=9,columnspan=2,sticky='wsen')
        self.sb.config(command=self.lb1.yview)
        
        
    
    def no():
        pass


root=tk.Tk()
app=Bond_Img(master=root)
app.mainloop()

