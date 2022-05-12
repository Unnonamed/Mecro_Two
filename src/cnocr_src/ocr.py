import numpy as np 
from cnocr import CnOcr
from typing import Union
import numpy as np 
import random 
import cv2 
import PIL 

class ocr():
    def __init__(self) -> None:
        pass

    def img_ocr(path: Union[str, None])-> None:
            
        img = cv2.imread(path)  
        # region CV2 배경 제거 관련
        # #image_gray = cv2.imread('saveImage.jpg' , cv2.IMREAD_GRAYSCALE)
        # # 변환 graky
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # # 임계값 조절
        # mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]
        # # mask
        # mask = 255 - mask
        # # morphology 적용
        # # borderconstant 사용
        # kernel = np.ones((3,3), np.uint8)
        # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # # # anti-alias the mask
        # # # blur alpha channel
        # mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2, borderType = cv2.BORDER_DEFAULT)

        # # # linear stretch so that 127.5 goes to 0, but 255 stays 255
        # mask = (2*(mask.astype(np.float32))-255.0).clip(0,255).astype(np.uint8)

        # # # put mask into alpha channel
        # result = img.copy()
        # result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
        # result[:, :, 3] = mask

        # #저장
        # cv2.imwrite('translated.png', result)
        # endregion


        
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #회색 이미지 처리
        # blur = cv2.medianBlur(gray, 7) #블러링 필터
        # threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] #검은색 흰색의 이진처리 (배경과 영역 구분)
        # canny = cv2.Canny(threshold, 100, 150) #에지 처리 (윤곽선 구분)
        # kernel = np.ones((3, 3), np.uint8)
        # dilate = cv2.dilate(canny, kernel, iterations=5) #가장자리 확장
        
        
        ocr = CnOcr()
        res = ocr.ocr(img)
        #res = ocr.ocr_for_single_line('saveImage.jpg')

        #print("Predicted Chars:", res)
        result = print_preds(res)

        # cv2.imshow("test",img) 
        # cv2.waitKey(0)
        return result
        
def print_preds(pred):
    pred = [''.join(line_p) for line_p, _ in pred] # _(언더스코어) https://mingrammer.com/underscore-in-python/
    #print("Predicted Chars:", pred)
    return pred

if __name__ == "__main__":
    x=ocr.img_ocr('saveImage.jpg')
    #x=ocr.img_ocr()
    pass





