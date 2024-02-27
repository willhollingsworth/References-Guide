
'''
mysql to python using Oracle's mysql-connector library

https://medium.com/analytics-vidhya/importing-data-from-a-mysql-database-into-pandas-data-frame-a06e392d27d7
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html
'''
import mysql.connector
import pandas as pd


mydb = mysql.connector.connect(
host="localhost",
user="root",
password="mysql"
)
query = 'SELECT * FROM test3.test4;'
result_dataFrame = pd.read_sql(query,mydb)
mydb.close() #close the connection
print(result_dataFrame)