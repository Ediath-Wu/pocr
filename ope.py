from os.path import join
from cnocr import CnOcr
from cnstd import CnStd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os



# for box_info in box_info_list:
#     crp_img=box_info['cropped_img']
#     ocr_res=ocr.ocr_for_single_line(crp_img)
#     print('result: %s' % ''.join(ocr_res))
    


"""
class task_one():
    def __init__(self) -> None:
        self.filepath='E:\\Work Place\\pocr\\pic\\3.jpg'
        
    def get_list(self):
        ocr._model_name='conv-lite-fc'
        print(ocr._model_name)
        ocr_res2=ocr.ocr(img_fp=self.filepath)
        box_info_list=std.detect(self.filepath,pse_threshold=0.7,pse_min_area=150,context='gpu',height_border=0.10)
        image=Image.open(self.filepath)
        fontstyle=ImageFont.truetype('./simhei.ttf',13,encoding='utf-8')
        draw=ImageDraw.Draw(image)
        for box_info in box_info_list:
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
"""

class Bond_Ope():
    def __init__(self) -> None:
        self.STD=CnStd()
        self.OCR=CnOcr()
        
        """
        包括函数:
            get_bbox: 获取文本框的范围
            get_context: 从给定的范围中进行文字识别
        """
    def get_single_img_path(self,dirpath):
        return os.listdir(dirpath)
        
    def get_bbox(self,imagepath):
        bbox=[]
        box_info_list=self.STD.detect(imagepath,pse_threshold=0.50,pse_min_area=150,height_border=0.10)
        for box_info in box_info_list:
            info_box=box_info['box']
            # print(info_box)
            x1,y1=info_box[0,0],info_box[0,1]
            x2,y2=info_box[1,0],info_box[1,1]
            x3,y3=info_box[2,0],info_box[2,1]
            x4,y4=info_box[3,0],info_box[3,1]
            bbox.append([x1,y1,x2,y2,x3,y3,x4,y4])
        # return box_info_list['cropped_img']
        # return [x1,y1,x2,y2,x3,y3,x4,y4]
        return box_info_list


    def get_context(self,imagepath,mode='default'):
        self.OCR._model_name='conv-lite-fc'
        print('-'*10+'开始识别 {}'.format(imagepath)+'-'*10)
        try:
            res=self.OCR.ocr(img_fp=imagepath)[0]
            a="".join(res)
            print(a)
            # print('-'*10+'识别完毕'+'-'*10)
            return a
        except:
            if mode=='default':
                pass
            elif mode =='by_hand':
                return 'by_hand'
            
        



