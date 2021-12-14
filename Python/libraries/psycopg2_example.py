# example script for running a query on a postgres db
# https://pynative.com/python-postgresql-select-data-from-table/



import psycopg2
try:
    connection = psycopg2.connect(user="xxxx",
                                password="xxxx",
                                host="127.0.0.1",
                                port="5000",
                                database="postgres_db")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from mobile"
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall() 

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
