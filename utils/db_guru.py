import mysql.connector

from .connection import db

def insert_data_guru(nama_guru: str, nip: str):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO tbl_guru (nama_guru, nip) VALUES (%s,%s)", (nama_guru, nip))
    db.commit()
    return cursor.lastrowid

def get_data_guru(id_guru: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_guru WHERE id_guru=%s', (id_guru,))
    return cursor.fetchone()

def get_all_data_guru():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_guru")
    return cursor.fetchall()

def update_data_guru(id_guru: int,nama_guru: str, nip: str):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE tbl_guru SET nama_guru=%s, nip=%s WHERE id_guru=%s",(nama_guru,nip, id_guru))
    db.commit()
    return cursor.fetchone()
