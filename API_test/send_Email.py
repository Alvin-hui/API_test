#coding=utf-8

from email.mime.text import MIMEText
import smtplib
import email

msg = MIMEText('hello', _subtype='plain', _charset='utf-8')
msg['Subject'] = u'刘经辉'
from_addr = '15814431642@163.com'
password = '1990526good'

smtp_server = 'smtp.163.com'

to_addr = '764862864@qq.com'


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
