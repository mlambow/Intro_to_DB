import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'mydb'
)

print(mydb.get_server_info())