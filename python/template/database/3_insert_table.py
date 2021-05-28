""" insert into table """

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

""" insert into table using variables """

import mysql.connector

def insert_varibles_into_table(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='pynative',
                                             password='pynative@#29')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

        record = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


insert_varibles_into_table(2, 'Area 51M', 6999, '2019-04-14')
insert_varibles_into_table(3, 'MacBook Pro', 2499, '2019-06-20')


""" insert multiple rows """

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES (%s, %s, %s, %s) """

    records_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
                         (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                         (6, 'Microsoft Surface', 2330, '2019-07-23')]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


""" insert timestamp & datetime """

from datetime import datetime

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                            VALUES (%s, %s, %s, %s) """

    cursor = connection.cursor()
    current_Date = datetime.now()
    # convert date in the format you want
    formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')
    insert_tuple = (7, 'Acer Predator Triton', 2435, current_Date)

    result = cursor.execute(mySql_insert_query, insert_tuple)
    connection.commit()
    print("Date Record inserted successfully")

except mysql.connector.Error as error:
    connection.rollback()
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
