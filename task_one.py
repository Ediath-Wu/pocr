import numpy as np
import os
import sys
import xml.dom.minidom
import cv2 as cv
from cnocr import CnOcr
from cnstd import CnStd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class task_one():
    def __init__(self) -> None:
        self.filepath='E:\\Work Place\\pocr\\pic\\3.jpg'
        
    def get_list(self):
        std=CnStd()
        
        ocr=CnOcr()
        ocr._model_name='conv-lite-fc'
        print(ocr._model_name)
        ocr_res2=ocr.ocr(img_fp=self.filepath)
        box_info_list=std.detect(self.filepath,pse_threshold=0.7,pse_min_area=150,context='gpu',height_border=0.10)
        image=Image.open(self.filepath)
        fontstyle=ImageFont.truetype('./simhei.ttf',13,encoding='utf-8')
        draw=ImageDraw.Draw(image)
        for box_info in box_info_list:
            print('a')
            print('a')
            print(box_info)
            info_box=box_info['box']
            crp_img=box_info['cropped_img']
            ocr_res1=ocr.ocr_for_single_line(crp_img)
            
            print('result: %s' % ''.join(str(ocr_res1)))
            x1,y1=info_box[0,0],info_box[0,1]
            x2,y2=info_box[1,0],info_box[1,1]
            x3,y3=info_box[2,0],info_box[2,1]
            x4,y4=info_box[3,0],info_box[3,1]
            

            draw.polygon([(x1,y1),(x4,y4),(x3,y3),(x2,y2)],outline=(255,0,0))
            draw.text((x4,y4),str(ocr_res1),(200,0,0),font=fontstyle)
        image.show()
        print(ocr_res2)
        return box_info_list

    def cut_image(image):
        width,height=image.size
        item_width=int(width/3)
        
    def get_single_file(file_name,file_path):
        with open(file_name+file_path) as file:
            pass
    
task=task_one()
task.get_list()
