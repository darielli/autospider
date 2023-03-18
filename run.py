from database_utils import mysql_query, mysql_insert
import os

from send_emails import send_mail
from spider.tuanwei import parse_tuanwei

host = os.getenv('HOST')
port = os.getenv('PORT')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')

sender_name = os.getenv('SENDER_NAME')
address = os.getenv('ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

receiver_name = os.getenv('RECEIVER_NAME')
receiver_address = os.getenv('RECEIVER_ADDRESS')

sender = [sender_name, address, email_password]
receiver = [receiver_name, receiver_address]
c = {
    "host": host,
    "port": port,
    "user": user,
    "password": password,
    "database": database
}


def send_and_store(sender_info, receiver_info, info, web):
    send_mail(sender_info, receiver_info, info)
    mysql_insert(c, info, web)


def main():
    url, notice_list = parse_tuanwei()

    data = mysql_query(c, url)
    if data is None:
        send_and_store(sender, receiver, notice_list[0], url)
    else:
        index = -1
        for i in range(len(notice_list)):
            if data[1] == notice_list[i][1]:
                index = i
                break
        if index == -1:
            send_and_store(sender, receiver, notice_list[0], url)
        else:
            for i in reversed(range(index)):
                send_and_store(sender, receiver, notice_list[i], url)


if __name__ == "__main__":
    main()



