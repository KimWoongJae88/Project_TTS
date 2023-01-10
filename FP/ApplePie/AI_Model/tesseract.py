import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os
import config


class OCR():
    def __init__(self, file_name):
        pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
        
        self.path = config.IMAGE_PATH
        self.file_name = file_name
        
    def ImgToText(self):
        imga = cv2.imread(self.path + self.file_name)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(image, lang='kor')
        
        return text

