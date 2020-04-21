import urllib
import requests
import re
import time


#http://www.htqyy.com/top/hot
#http://f2.htqyy.com/play7/33/mp3/4
songID=[]
songName=[]
for i in range(1):
    url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"

    #获取网页信息
    html=requests.get(url)
    strr=html.text
    #网页中关键字
    pat1=r'title="(.*?)" sid'
    pat2=r'sid="(.*?)"'
    #正则表达式数据清洗
    idlist=re.findall(pat2,strr)
    tlist=re.findall(pat1,strr)

    songID.extend(idlist)
    songName.extend(tlist)
    time.sleep(0.5)

for i in range(len(songID)):
    songurl="http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/4"
    songname=songName[i]
    date=requests.get(songurl).content

    if len(date) < 1200:
        songurl = "http://f2.htqyy.com/play7/" + str(songID[i]) + "/m4a/4"
        date = requests.get(songurl).content
    print("正在下载第",i+1,"首："+songname)
    print(len(date))
    #写到本地
    with open("G:\\music\\{}.mp3".format(songname),"wb") as f:
        f.write(date)

    time.sleep(0.5)