'''
https://pythonspot.com/sqlite-database-with-pandas/
https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
https://datagy.io/python-sqlite-tutorial/
'''
import sqlite3
from pathlib import Path

home_path = str(Path.home())
db_path_relative = r'\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db'
db_path =  home_path + db_path_relative

def sql_print_command(command):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    result = cursor.execute(command)
    for row in result.fetchall():
        parse_row = [str(item) for item in row]
        print(' '.join(parse_row))             
    cursor.close()

if __name__ == '__main__':
    command = "SELECT * FROM Genre LIMIT 3"
    sql_print_command(command)               
          