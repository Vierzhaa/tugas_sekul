import mysql.connector

try:
    db = mysql.connector.connect (
        host='localhost',
        user='root',
        password='',
        database='db_jurnal'
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")
    db = None