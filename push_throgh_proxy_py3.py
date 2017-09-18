# -*- coding:utf-8 -*-
#http://localhost:9665/weixinApi/cm?mainProtocol=1&subProtocol=1&pictureInfo=dfdfdff
import urllib
# import urllib2

#http://192.168.41.20:9665/api/cm?mainProtocol=3&subProtocol=1&pictureInfo=
import os
import base64
import requests
import time
import cv2
# from urllib2 import urlopen
import urllib.request
proxy_support = urllib.request.ProxyHandler({'http': '192.168.41.120:8899'})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

imgdir="/home/tenghui/PycharmProjects/testlabelmap/images/"
# url = "http://192.168.41.20:8080/demo/cn/demo.html"
# url = "http://192.168.41.20:8080/weixinApi/cm?mainProtocol=1&subProtocol=1"
url = "http://192.168.41.100:9665/smart/cm?mainProtocol=10&subProtocol=1&projectNo=1&type=safetyHelmet&deviceNo=1"
for frame in os.listdir(imgdir):
    frame_full_path = imgdir+frame
#     image = cv2.imread(frame_full_path)
#     image = cv2.resize(image,(300,300))
# #     print frame_full_path
# # # while success :
# #     cv2.imshow("Oto Video", image) #显示
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
#     # videoWriter.write(frame) #写视频帧
#     cv2.imwrite(tmp_path, image)
    frame = open(frame_full_path, 'rb').read()
    encoded_img=base64.b64encode(frame)
    print(encoded_img)
    # postdata=urllib.urlencode({'image':encoded_img})
    # filehandle = urllib.urlopen(url,postdata,proxies=proxies)
    # a = urllib.request.urlopen(url,postdata).read().decode("utf8")
    # print (filehandle.read())
    r = requests.post(url,data={"image":encoded_img});
    print("Send request at : %s" % time.ctime())
    print(r.status_code)
    print(r.text)
    break


    time.sleep(4)

# url = "http://192.168.41.20:8080/api/cm?mainProtocol=1&subProtocol=1"
# count = 1
# while True:
#     try:
#         while True:
#             for img in os.listdir(imgdir):
#                 imgpath = imgdir+img
#                 img=open(imgpath).read();
#                 encoded_img=base64.b64encode(img)
#                 r = requests.post(url,data={"pictureInfo":encoded_img});
#                 print "Send request at : %s" % time.ctime()
#                 print(r.status_code)
#                 print r.text
#                 time.sleep(4)
#                 print count
#                 count+=1
#             time.sleep(14)
#     except Exception, e:
#         print e
#         time.sleep(60)

