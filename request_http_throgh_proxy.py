import urllib.request
import time
import http

proxy_support = urllib.request.ProxyHandler({'http': '192.168.41.120:8899'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
try:
    a = urllib.request.urlopen("http://192.168.41.20:8080/demo/cn/demo.html").read().decode("utf8")
    print(a)
except http.client.HTTPException as e:
    print(e)
# print(a)
