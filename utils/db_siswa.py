import mysql.connector

from .connection import db

def insert_data_siswa(nama_siswa: str, id_kelas: int, nisn: str, nis: str):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO tbl_siswa (nama_siswa, id_kelas, nisn, nis) VALUES (%s,%s,%s,%s)", (nama_siswa, id_kelas, nisn, nis))
    db.commit()
    return cursor.lastrowid

def get_data_siswa(id_siswa: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_siswa WHERE id_siswa=%s', (id_siswa,))
    return cursor.fetchone()


def update_data_siswa(id_siswa: int,nama_siswa: str,id_kelas: int, nisn: str,nis: str):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE tbl_siswa SET nama_siswa=%s,id_kelas=%s, nisn=%s,nis=%s WHERE id_siswa=%s",(nama_siswa,id_kelas,nisn,nis,id_siswa))
    db.commit()
    return cursor.fetchone()

def get_all_data_siswa():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_siswa")
    return cursor.fetchall()
