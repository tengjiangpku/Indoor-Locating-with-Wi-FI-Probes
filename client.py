import requests
import json
headers = {'content-type':'application/json'}
url="http://127.0.0.1:8888/"   #IP和端口号，注意register后要加/
# data = {"id":"0029c591","mmac":"5e:cf:7f:29:c5:91","rate":"1","time":"Tue Feb 21 08:13:31 2017","lat":"30.747988","lon":"103.973152" ,"data": [{"mac":"a4:56:02:61:7f:57","rssi":"-91","range":"91.5"},{"mac":"8c:a6:df:62:2d:3d","rssi":"-93","range":"108.5"},{"mac":"a4:56:02:71:be:b3 ","rssi":"-96","range":"140.1"},{"mac":"cc:34:29:97:4d:0d","rssi":"-95","range":"128.6"},{"mac":"44:33:4c:aa:71:82","rssi":"-94","range":"11 8.1"},{"mac":"b0:48:7a:5a:10:f8","rssi":"-86","range":"59.7"},{"mac":"a8:57:4e:9d:ca:d8","rssi":"-96","range":"140.1"},{"mac":"5e:cf:7f:93:3 d:0e","rssi":"-56","range":"4.6"},{"mac":"5e:cf:7f:93:3d:0f","rssi":"-58","range":"5.5"},{"mac":"5e:cf:7f:93:3d:10","rssi":"-63","range":"8. 4"},{"mac":"5e:cf:7f:93:3d:0b","rssi":"-68","range":"12.9"},{"mac":"5e:cf:7f:93:3d:0c","rssi":"-53","range":"3.5"},{"mac":"5e:cf:7f:93:3d:0d ","rssi":"-69","range":"14.0"},{"mac":"e4:f3:f5:24:2c:d8","rssi":"-89","range":"77.1"},{"mac":"14:cf:92:8a:8f:f0","rssi":"-96","range":"140. 1"}]}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)
