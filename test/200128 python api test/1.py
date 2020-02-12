import os
import sys
import requests
client_id = "cbxhzui4en"
client_secret = "m7YcN6l15L4l4hSgVRTfAiArIHbEK8S384Q55fIX"
url = "https://naveropenapi.apigw.ntruss.com/vision-obj/v1/detect"
files = {'image': open('1.jpeg', 'rb')}
headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)


import matplotlib.pyplot as plt
from matplotlib.image import imread
 
img = imread('1.jpeg') # 이미지 읽어오기
 
plt.imshow(img)
plt.show()
