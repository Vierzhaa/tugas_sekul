import mysql.connector
from datetime import date

tanggal_sekarang = date.today()

from .connection import db

def insert_data_jurnal_kbm(id_jadwal: int, tanggal: date.today()):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO jurnal_kbm (id_jadwal, tanggal) VALUES (%s,%s)", (id_jadwal, tanggal))
    db.commit()
    return cursor.lastrowid

def get_data_jurnal_kbm(id_jurnal: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM jurnal_kbm WHERE id_jurnal=%s', (id_jurnal,))
    return cursor.fetchone()


def update_data_jurnal_kbm(id_jurnal: int,id_jadwal: int, tanggal: date.today()):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE jurnal_kbm SET id_jadwal=%s, tanggal=%s WHERE id_jurnal=%s",(id_jadwal,tanggal, id_jurnal))
    db.commit()
    return cursor.fetchone()

def get_all_data_jurnal_kbm():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jurnal_kbm")
    return cursor.fetchall()
