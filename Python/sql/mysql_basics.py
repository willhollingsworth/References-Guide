
'''
mysql to python using Oracle's mysql-connector library

https://www.mysqltutorial.org/python-mysql/python-mysql-query/
https://www.w3schools.com/python/python_mysql_getstarted.asp

'''
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="mysql"
)

my_cursor = mydb.cursor()
my_cursor.execute('SHOW DATABASES;')
print(my_cursor.fetchall())
