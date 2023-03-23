from database_utils import *
import os

import time
from send_emails import send_mail
from spider.qi_ming import parse_xuegong
from spider.tuanwei import parse_tuanwei

host = os.getenv('HOST')
port = int(os.getenv('PORT'))
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')

sender_name = os.getenv('SENDER_NAME')
sender_address = os.getenv('ADDRESS')
sender_email_password = os.getenv('EMAIL_PASSWORD')

sender = [sender_name, sender_address, sender_email_password]

c = {
    "host": host,
    "port": port,
    "user": user,
    "password": password,
    "database": database
}

website_dict = {
    "https://tuanwei.nju.edu.cn/ggtz/list1.htm": "南大青年",
    "https://xgc.nju.edu.cn/1537/list.htm": "启明网-网上公示",
    "https://xgc.nju.edu.cn/1538/list.htm": "启明网-下载专区"
}

receiver_list = get_receivers(c)


def send_and_store(info, web):
    for i in receiver_list:
        send_mail(sender, i, info, website_dict[web])
        print("已向" + i[0] + " " + i[1] + "发送邮件" + str(info))
    mysql_insert(c, info, web)
    print("已存入数据库" + str(info))


def tuanwei():
    url, notice_list = parse_tuanwei()

    data = mysql_query(c, url)
    if data is None:
        print("数据库为空，返回第一条")
        send_and_store(notice_list[0], url)
    else:
        index = -1
        for i in range(len(notice_list)):
            if data[1] == notice_list[i][1]:
                index = i
                break
        if index == -1:
            print("数据库中第一条不存在于第一页，返回第一条")
            send_and_store(notice_list[0], url)
        else:
            print("数据库中第一条存在于第一页，返回前面n条")
            print("index:" + str(index))
            for i in reversed(range(index)):
                send_and_store(notice_list[i], url)


def xuegong():
    url, notice_list = parse_xuegong()
    if notice_list is None:
        return

    data = mysql_query(c, url)
    if data is None:
        print("数据库为空，返回第一条")
        index = len(notice_list)
        for i in reversed(range(index)):
            send_and_store(notice_list[i], url)
    else:
        index = -1
        for i in range(len(notice_list)):
            if data[1] == notice_list[i][1]:
                index = i
                break
        if index == -1:
            print("数据库中第一条不存在于第一页，返回第一条")
            send_and_store(notice_list[0], url)
        else:
            print("数据库中第一条存在于第一页，返回前面n条")
            print("index:" + str(index))
            for i in reversed(range(index)):
                send_and_store(notice_list[i], url)


def run_spider():
    print("启动爬虫:" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    xuegong()
    tuanwei()
    print("运行结束:" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


if __name__ == "__main__":
    run_spider()



