'''
https://pythonspot.com/sqlite-database-with-pandas/
https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
https://datagy.io/python-sqlite-tutorial/
'''
import sqlite3
from pathlib import Path
import pandas as pd
from IPython.display import HTML

home_path = str(Path.home())
db_path_relative = r'\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db'
db_path =  home_path + db_path_relative

connection = sqlite3.connect(db_path)

def sql_run_query(query):
    cursor = connection.cursor()
    result = cursor.execute(query).fetchall()
    cursor.close()
    return result

def sql_print_command(query):
    result = sql_run_query(query)
    for row in result:
        parse_row = [str(item) for item in row]
        print(' '.join(parse_row))   

def sql_return_df(query):
    df = pd.read_sql_query(query,connection)
    return df

def sql_return_html(query):
    df = sql_return_df(query)
    html = HTML(df.to_html(index=False))
    return html

if __name__ == '__main__':
    command = "SELECT * FROM Genre LIMIT 3"
    # sql_print_command(command)               
    # sql_return_df(command)
    print(sql_return_df(command))