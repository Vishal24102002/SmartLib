import cv2
from qrtools import QR 

address=input("Enter location of qr image")

my_QR = QR(filename = address) 
  
# decodes the QR code and returns True if successful 
my_QR.decode() 
  
print(my_QR.data)
