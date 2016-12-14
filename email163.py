#/usr/bin/python
#encoding:utf-8
import smtplib
import sys
import os
import datetime
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailto_list = ["1102128368@qq.com"]  #目标邮箱
mail_host = "smtp.163.com"
mail_user = "ciqingkedai10000@163.com"
mail_pass = "chengyuan123"  #163邮箱smtp生成的密码


def send_mail(to_list, sub, content):
    me = "LogServer"+"<"+mail_user+">"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
        send_mail(mailto_list, 'submit', 'content')
