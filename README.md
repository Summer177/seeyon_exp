![image.png](https://cdn.nlark.com/yuque/0/2021/png/603531/1622620222886-f40c9762-35e8-4547-9004-ecd3d8e52294.png#align=left&display=inline&height=178&margin=%5Bobject%20Object%5D&name=image.png&originHeight=356&originWidth=907&size=18656&status=done&style=none&width=453.5)
# 工具介绍
**致远OA漏洞检查与利用工具，收录漏洞如下：**
```
信息泄露：
致远OA A8 状态监控页面信息泄露
致远OA A6 initDataAssess.jsp 用户敏感信息泄露
致远OA A6 createMysql.jsp 数据库敏感信息泄露
致远OA A6 DownExcelBeanServlet 用户敏感信息泄露
致远OA getSessionList.jsp Session泄漏漏洞

SQL注入：
致远OA A6 setextno.jsp SQL注入漏洞
致远OA A6 test.jsp SQL注入漏洞

文件上传：
致远OA ajax.do 登录绕过&任意文件上传
致远OA Session泄露 任意文件上传漏洞

任意文件下载：
致远OA webmail.do任意文件下载
```
**使用方法：**
```
Usage:
python3 seeyon_exp.py -u url              #漏洞检测
python3 seeyon_exp.py -u url --att				#漏洞检测+getshell
python3 seeyon_exp.py -f url.txt          #批量漏洞检查
python3 seeyon_exp.py -f url.txt --att		#批量漏洞检测+getshell

Options:
  -h, --help            show this help message and exit
  -u URL, --url=URL     target url
  -f FILE, --file=FILE  url file
  --att                 getshell
```
```
python3 seeyon_exp.py -u url
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/603531/1622621523227-5ef552da-4bf2-4a98-ba4c-0c16292dcc8d.png#align=left&display=inline&height=463&margin=%5Bobject%20Object%5D&name=image.png&originHeight=925&originWidth=1219&size=140406&status=done&style=none&width=609.5)
```
python3 seeyon_exp.py -u url  --att
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/603531/1622625176126-20a05004-b3e4-4188-acbf-c307f661fff5.png#align=left&display=inline&height=462&margin=%5Bobject%20Object%5D&name=image.png&originHeight=924&originWidth=1218&size=138710&status=done&style=none&width=609)
</br>
</br>
**默认使用冰蝎3的webshell，密码为rebeyond**
</br>
</br>
**扫码结果保存为result.txt，使用批量扫描时，建议先筛选出存活url**
</br>
</br>
**仅用于授权测试，违者后果自负**
</br>
</br>
参考链接：
```
https://github.com/PeiQi0/PeiQi-WIKI-POC/tree/PeiQi/PeiQi_Wiki/OA%E4%BA%A7%E5%93%81%E6%BC%8F%E6%B4%9E/%E8%87%B4%E8%BF%9COA
```

