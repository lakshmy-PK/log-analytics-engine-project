import mysql.connector
from mysql.connector import error

def database_connection():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database_name="",
            port=""
        )
        if connection.is_connected():
            print("database connected")
            return connection
        else:
            print("connection failed")
    except Error as e:
        print("connection error",e)

database_connection()