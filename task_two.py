from cnocr import CnOcr
import cnocr
from cnstd import CnStd

std=CnStd()
ocr=CnOcr()
box_info_list=std.detect('E:\\Work Place\\pocr\\pic\\2.png')
res=ocr.ocr('E:\\Work Place\\pocr\\pic\\1.png')
for box_info in box_info_list:
    crp_img=box_info['cropped_img']
    ocr_res=ocr.ocr_for_single_line(crp_img)
    print('result: %s' % ''.join(ocr_res))