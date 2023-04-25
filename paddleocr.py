# installation
#pip install paddleocr paddlepaddle
# import
from paddleocr import PaddleOCR
# inference
img_path = "RECEIPT_IMAGE.jpg"
ocr = PaddleOCR(use_angle_cls=True, lang='en')
result = ocr.ocr(img_path, cls=True)
print(result)
