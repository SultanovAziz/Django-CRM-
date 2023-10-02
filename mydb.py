


import mysql.connector as mysql

dataBases = mysql.connect(
    host = 'localhost',
    user = 'root',
    passwd  = 'aziz0102',
    auth_plugin='mysql_native_password'
)

#prepare cursor object
cursorObject = dataBases.cursor()

cursorObject.execute("CREATE DATABASE test")
print('ALL DONE!')
