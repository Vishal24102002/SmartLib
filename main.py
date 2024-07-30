import cv2,device,requests,pandas as pd
from qrtools import QR 


def get_data(img):
  my_QR = QR(filename = address) 
  # decodes the QR code and returns True if successful 
  my_QR.decode() 
  
  print(my_QR.data)

def get_list_camera():

  List_cam={}
  
  # Get camera list
  device_list = device.getDeviceList()
  index = 0

  for camera in device_list:
      List_cam[index]=camera
      index += 1
  return List_cam

def creating_QR(data):
  my_QR = QR(data) 
  # encodes the QR code and returns True if successful 
  my_QR.encode() 

  

def check_record(api_link):
  data_req=request(api_link).get()
  return pd.Dataframe(data_req)
