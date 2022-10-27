import cv2
from pyzbar.pyzbar import decode
import os
import time

chuj = './coupons/couponTest.jpg'

img = cv2.imread(chuj)

# print(decode(img))
''' finding barcode  '''
# for code in decode(img):
#     # print(code.type)

#     print("found code: ", code.data.decode('utf-8'))

''' listing all files from a folder '''
basepath = 'coupons/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)
        fileName = str(entry)
        imgTest = cv2.imread(fileName)

''' itereate for all files'''
# Folder Path
# path = "coupons"
  
# # Change the directory
# os.chdir(path)

# # read coupon functon
# def read_code(file_path):
#     img = cv2.imread(file_path)
#     for code in decode(img):
#         print("found code: ", code.data.decode('utf-8'))
# #         # time.sleep(3)

# # iterate through all file
# for file in os.listdir():
#     # Check whether file is in text format or not
#     if file.endswith(".jpg"):
#         file_path = f"{path}/{file}"
#         imgPath = "./"+file_path
#         print(imgPath)
#         img = cv2.imread(imgPath)

     
  
        # call  function
        # read_code(file_path)




