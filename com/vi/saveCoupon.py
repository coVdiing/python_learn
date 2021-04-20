import mysql.connector
import coupon


def connect():
    conn = mysql.connector.connect(user='root', password='root', database='test')
    return conn


def save_coupon():
    conn = connect()
    cursor = conn.cursor()
    list = coupon.generate_coupon(200)
    save_sql = 'INSERT INTO active_code(content) VALUES '
    i = 0
    for value in list:
        if i == 199:
            save_sql = save_sql + " ('{}')".format(value)
        else:
            save_sql = save_sql + (" ('{}'),".format(value))
        i += 1
    print("save_sql:{}".format(save_sql))
    cursor.execute(save_sql)
    conn.commit()
    cursor.close()
    conn.close()


# update coupon id()
def update_coupon_id():
    conn = connect()
    cursor = conn.cursor()
    select_sql = 'SELECT id,content FROM active_code'
    cursor.execute(select_sql)
    list = cursor.fetchall()
    update_sql = 'UPDATE active_code SET id = CASE id\n'
    where_sql = "END\nWHERE id in ("
    for i in range(0,len(list)):
        update_sql += 'WHEN {} THEN {} \n'.format(list[i][0],i+1)
        if i != len(list) -1:
            where_sql += '{},'.format(list[i][0])
        else:
            where_sql += '{})'.format(list[i][0])
    update_sql += where_sql
    print(update_sql)
    cursor.execute(update_sql)
    conn.commit()
    cursor.close()
    conn.close

update_coupon_id()
