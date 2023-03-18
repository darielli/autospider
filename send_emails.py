import os
import smtplib
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from datetime import datetime


def message(message_info):
    msg = """
    【新发布通知】<br />
    南大青年发布新通知：<br />
    <strong>{}.</strong><br /><br /><br />
    点击链接查看详情：<br />
    {}
    <br />
    <br />
    {}
    """.format(message_info[0], message_info[2], message_info[1])
    return msg


def send_mail(sender, receiver, information):
    print('infomation:')
    print(information)
    msg = MIMEMultipart('related')
    msg["Subject"] = Header("南大青年新公告：" + information[0], 'utf-8').encode()  # 设置邮件标题

    msg['From'] = formataddr((Header(sender[0], 'utf-8').encode(), sender[1]))  # 发件人信息

    msg["To"] = formataddr((Header(receiver[0], 'utf-8').encode(), receiver[1]))  # just for single user

    content = MIMEText(message(information), "html", 'utf-8')  # 设置邮件内容 'plain' for txt and 'html' for html codes
    msg.attach(content)

    server = smtplib.SMTP_SSL('smtp.exmail.qq.com',
                              465)  # 'smtp.qq.com' for qq Mail,and 'smtp.exmail.qq.com' for tencent enterprise email
    server.login(sender[1], sender[2])
    # server.set_debuglevel(2)
    server.sendmail(sender[1], receiver[1], msg.as_string())
    #
    server.quit()
    print("[" + str(datetime.now()) + "] 已向 " + receiver[0] + " 的邮箱 " + receiver[1] + " 成功发送邮件.")

