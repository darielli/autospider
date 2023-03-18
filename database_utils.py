import pymysql.cursors


def mysql_query(connection, web):

    # 数据库链接信息
    db = pymysql.connect(host='47.96.238.162',
    # db = pymysql.connect(host=connection['host'],
                         port=connection['port'],
                         user=connection['user'],
                         password=connection['password'],
                         database=connection['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句，查询user表
    sql = 'SELECT title, detail, publish_time from posts where web = \'{}\' order by publish_time desc '.format(web)
    # 执行sql语句查询
    cursor.execute(sql)
    # 这是获取表中第一个数据
    rest = cursor.fetchone()
    db.close()
    return rest
    # 关闭数据库连接


def mysql_insert(connection: dict, post: list, web):
    # 数据库链接信息
    db = pymysql.connect(host=connection['host'],
                         port=connection['port'],
                         user=connection['user'],
                         password=connection['password'],
                         database=connection['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句，查询user表
    sql = 'insert into posts(publish_time, web, title, detail, content) values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'\
        .format(post[2],web, post[0], post[1], "content")
    # 执行sql语句查询
    cursor.execute(sql)
    # 这是获取表中第一个数据
    db.commit()
    # 关闭数据库连接
    cursor.close()
    db.close()
