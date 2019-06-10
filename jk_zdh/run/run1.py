# -*- coding:utf-8 -*-
#from HTMLTestReportCN import HTMLTestRunner#导入用例生成模块
from ExtentHTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart#调用邮件发送附件的模块
from email.mime.text import MIMEText#定义邮件内容
import smtplib#发送邮件模块
from time import sleep
import unittest
import time
import sys
import re
from email.header import Header#定义邮件标题
path="D:\\jk_kj\\"
sys.path.append(path)

#pattern="taobou*.py"就是执行带有taobou名称的脚本
if __name__=="__main__":
    #存放报告的文件夹
    report_dir='../savings'
    # 定义测试用例路径
    test_dir = '../Case_TEST'  # 把我们测试的脚本路径写进去
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    # pattern="taobou*.py"就是执行带有taobou名称的脚本
    #报告命名时间格式化
    now=time.strftime("%Y-%m-%d %H_%M_%S")#这里的y是年，m是月，d是天，H是小时，M是分，S是秒
    #报告文件完整路径
    report_name=report_dir+'/'+now+'test_result.html'
    report_name1=now+'test_result.html'
    #report_dir是路径，bg是时间，result.html是后缀名，这就是生成报告的名称

    with open(report_name,'wb')as f:#这里就是通过with open打开report_name这个报告，然后使用wb方式去写测试结果，f1是变量名称
        runner=HTMLTestRunner(stream=f,title=u"薪起程自动化测试报告",description='测试结果如下')
        #title="Test Report"报告的名称，description='Test case result'报告的描述
        runner.run(discover)
    f.close()
#使用discover可以一次调用多个脚本
#test_dir被测试脚本的路径
#pattern脚本名称匹配规定
#unittest只执行test的用例，就是我们创建一个脚本，用例开头一定要test开头
    # 发送邮箱服务器
    sleep(3)
    a = open(report_name, "r", encoding='UTF-8').read()
    a1 = '<span class="test-status right error">(.*?)</span>'
    a2 = '<span class="test-status right fail">(.*?)</span>'
    a3 = '<span class="test-status right fatal">(.*?)</span>'
    c = re.findall(a1, a)
    for i in c:
        if i == "error":
            smtpserver = 'smtp.qq.com'  # smtp.qq.com是qq邮箱的smtp地址，需要qq邮箱smtp打开

            # 发送邮箱用户名密码
            user = "466279653@qq.com"
            password = "qncfpaiwieajbgcb"

            # 发送和接收邮箱
            senderr = "466279653@qq.com"  # 这个是发送邮件的邮箱
            receives = ["466279653@qq.com"]  # 这个是接收邮件的邮箱"869774679@qq.com", "893588192@qq.com", "531879834@qq.com","1204158590@qq.com"
            # 就是我们发送给多个人的邮箱，receive后面一定加

            # 发送邮件主题和内容
            lxl = "薪起程自动化测试报告"
            con = "薪启程自动化报告如此文件"

            send_file = open(report_name, 'rb').read()
            # 定义一个变量，open是打开，把附件路径复制进来，然后定义以rb的读取方式,r是转义路径

            # html邮件正文
            att = MIMEText(send_file, 'base64', 'utf-8')  # 把附件传进来con，格式是base64，编码utf-8的
            att['Content-Type'] = 'application/octet-stream'  # 文件类型，文件以r进打开的，所以也以r进定义，application/octet-stream字节流
            att['Content-Disposition'] = 'attachment;filename={}'.format(report_name1)  # 这里是定义内容的属性，attachment是附件，filename="yy.txt"就是附件的名称，把它传入到attachment里

            msgRoot = MIMEMultipart()  # 这里使用了MIMEMultipart模块，用于发送附件和周围内容的
            msgRoot.attach(MIMEText(con, 'html', 'utf-8'))  # 定义邮件的正文内容
            msgRoot['Subject'] = lxl  # 标题
            msgRoot['From'] = senderr  # 定义发送的邮箱
            msgRoot['To'] = ','.join(receives)  # 这里意思就是以','为分割，同时发送给receives里面的用户
            msgRoot.attach(att)  # attach就是把附件，周围的文字啊这些都可以写进去，进行附上到邮件里

            # SSL协议端口号要使用465
            smtp = smtplib.SMTP_SSL(smtpserver, 465)
            # 这里用发送邮件的模块调用SMTP_SSL，就是以SMTP_SSL登录，如果不是以SMTP_SSL登录是发送不了
            # （）里放入发送邮件的服务器，后面是端口
            # ssl登录方式比较安全，ssl登录端口：465

            # 向服务器标识用户身份
            smtp.help(smtpserver)
            # 服务器返回结果确认
            smtp.ehlo(smtpserver)
            # 登录邮箱服务器用户名和密码
            smtp.login(user, password)

            print("开始发送...")
            smtp.sendmail(senderr, receives, msgRoot.as_string())
            # 这里的（）里顺序是发送邮箱，接收邮箱，内容，msg.as_string()是邮箱内容调用编码
            smtp.quit()  # 退出邮箱
            print("邮件发送完成")
            break
        else:
            print("不需要发邮件")
    c1 = re.findall(a2, a)
    for i in c1:
        if(i=="fail"):
            smtpserver = 'smtp.qq.com'  # smtp.qq.com是qq邮箱的smtp地址，需要qq邮箱smtp打开

            # 发送邮箱用户名密码
            user = "466279653@qq.com"
            password = "qncfpaiwieajbgcb"

            # 发送和接收邮箱
            senderr = "466279653@qq.com"  # 这个是发送邮件的邮箱
            receives = [
                "466279653@qq.com"]  # 这个是接收邮件的邮箱"869774679@qq.com", "893588192@qq.com", "531879834@qq.com","1204158590@qq.com"
            # 就是我们发送给多个人的邮箱，receive后面一定加

            # 发送邮件主题和内容
            lxl = "薪起程自动化测试报告"
            con = "薪启程自动化报告如此文件"

            send_file = open(report_name, 'rb').read()
            # 定义一个变量，open是打开，把附件路径复制进来，然后定义以rb的读取方式,r是转义路径

            # html邮件正文
            att = MIMEText(send_file, 'base64', 'utf-8')  # 把附件传进来con，格式是base64，编码utf-8的
            att['Content-Type'] = 'application/octet-stream'  # 文件类型，文件以r进打开的，所以也以r进定义，application/octet-stream字节流
            att['Content-Disposition'] = 'attachment;filename={}'.format(
                report_name1)  # 这里是定义内容的属性，attachment是附件，filename="yy.txt"就是附件的名称，把它传入到attachment里

            msgRoot = MIMEMultipart()  # 这里使用了MIMEMultipart模块，用于发送附件和周围内容的
            msgRoot.attach(MIMEText(con, 'html', 'utf-8'))  # 定义邮件的正文内容
            msgRoot['Subject'] = lxl  # 标题
            msgRoot['From'] = senderr  # 定义发送的邮箱
            msgRoot['To'] = ','.join(receives)  # 这里意思就是以','为分割，同时发送给receives里面的用户
            msgRoot.attach(att)  # attach就是把附件，周围的文字啊这些都可以写进去，进行附上到邮件里

            # SSL协议端口号要使用465
            smtp = smtplib.SMTP_SSL(smtpserver, 465)
            # 这里用发送邮件的模块调用SMTP_SSL，就是以SMTP_SSL登录，如果不是以SMTP_SSL登录是发送不了
            # （）里放入发送邮件的服务器，后面是端口
            # ssl登录方式比较安全，ssl登录端口：465

            # 向服务器标识用户身份
            smtp.help(smtpserver)
            # 服务器返回结果确认
            smtp.ehlo(smtpserver)
            # 登录邮箱服务器用户名和密码
            smtp.login(user, password)

            print("开始发送...")
            smtp.sendmail(senderr, receives, msgRoot.as_string())
            # 这里的（）里顺序是发送邮箱，接收邮箱，内容，msg.as_string()是邮箱内容调用编码
            smtp.quit()  # 退出邮箱
            print("邮件发送完成")
            break
        else:
            print("不需要发邮件")
    c2 = re.findall(a3, a)
    for i in c2:
        if(i=="fatal"):
            smtpserver = 'smtp.qq.com'  # smtp.qq.com是qq邮箱的smtp地址，需要qq邮箱smtp打开

            # 发送邮箱用户名密码
            user = "466279653@qq.com"
            password = "qncfpaiwieajbgcb"

            # 发送和接收邮箱
            senderr = "466279653@qq.com"  # 这个是发送邮件的邮箱
            receives = [
                "466279653@qq.com"]  # 这个是接收邮件的邮箱"869774679@qq.com", "893588192@qq.com", "531879834@qq.com","1204158590@qq.com"
            # 就是我们发送给多个人的邮箱，receive后面一定加

            # 发送邮件主题和内容
            lxl = "薪起程自动化测试报告"
            con = "薪启程自动化报告如此文件"

            send_file = open(report_name, 'rb').read()
            # 定义一个变量，open是打开，把附件路径复制进来，然后定义以rb的读取方式,r是转义路径

            # html邮件正文
            att = MIMEText(send_file, 'base64', 'utf-8')  # 把附件传进来con，格式是base64，编码utf-8的
            att['Content-Type'] = 'application/octet-stream'  # 文件类型，文件以r进打开的，所以也以r进定义，application/octet-stream字节流
            att['Content-Disposition'] = 'attachment;filename={}'.format(
                report_name1)  # 这里是定义内容的属性，attachment是附件，filename="yy.txt"就是附件的名称，把它传入到attachment里

            msgRoot = MIMEMultipart()  # 这里使用了MIMEMultipart模块，用于发送附件和周围内容的
            msgRoot.attach(MIMEText(con, 'html', 'utf-8'))  # 定义邮件的正文内容
            msgRoot['Subject'] = lxl  # 标题
            msgRoot['From'] = senderr  # 定义发送的邮箱
            msgRoot['To'] = ','.join(receives)  # 这里意思就是以','为分割，同时发送给receives里面的用户
            msgRoot.attach(att)  # attach就是把附件，周围的文字啊这些都可以写进去，进行附上到邮件里

            # SSL协议端口号要使用465
            smtp = smtplib.SMTP_SSL(smtpserver, 465)
            # 这里用发送邮件的模块调用SMTP_SSL，就是以SMTP_SSL登录，如果不是以SMTP_SSL登录是发送不了
            # （）里放入发送邮件的服务器，后面是端口
            # ssl登录方式比较安全，ssl登录端口：465

            # 向服务器标识用户身份
            smtp.help(smtpserver)
            # 服务器返回结果确认
            smtp.ehlo(smtpserver)
            # 登录邮箱服务器用户名和密码
            smtp.login(user, password)

            print("开始发送...")
            smtp.sendmail(senderr, receives, msgRoot.as_string())
            # 这里的（）里顺序是发送邮箱，接收邮箱，内容，msg.as_string()是邮箱内容调用编码
            smtp.quit()  # 退出邮箱
            print("邮件发送完成")
            break
        else:
            print("不需要发邮件")
