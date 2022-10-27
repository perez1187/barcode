import cv2
import numpy as np
from pyzbar.pyzbar import decode
import os

paths = r'./coupons/2022_10_27'

for filename in os.listdir(paths):
    img_path = os.path.join(paths, filename)
    img = cv2.imread(img_path)

    print("\n",filename)
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
