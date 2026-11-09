import mysql.connector

from .connection import db

def insert_data_rombel(id_siswa: int,id_kelas: int, id_wali_kelas: int, id_ketua_kelas: str):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO tbl_rombel (id_siswa, id_kelas, id_wali_kelas, id_ketua_kelas) VALUES (%s,%s,%s,%s)", (id_siswa,id_kelas,id_wali_kelas,id_ketua_kelas))
    db.commit()
    return cursor.lastrowid

def get_data_rombel(id_rombel: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_rombel WHERE id_rombel=%s', (id_rombel,))
    return cursor.fetchone()

def get_all_data_rombel():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_rombel")
    return cursor.fetchall()

def update_data_rombel(id_rombel: int,id_siswa: int, id_kelas: int,id_wali_kelas, id_ketua_kelas: str):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE tbl_rombel SET id_siswa=%s, id_kelas=%s, id_wali_kelas=%s, id_ketua_kelas=%s WHERE id_rombel=%s",(id_siswa,id_kelas,id_wali_kelas ,id_ketua_kelas, id_rombel))
    db.commit()
    return cursor.fetchone()
