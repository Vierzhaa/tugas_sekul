import mysql.connector

from .connection import db

def insert_data_jadwal(id_tahun_ajaran: int,id_guru: int, id_kelas: int, id_mapel: int, hari: str, jam_ke: int):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO tbl_jadwal (id_tahun_ajaran, id_guru, id_kelas, id_mapel, hari, jam_ke) VALUES (%s,%s,%s,%s,%s,%s)", (id_tahun_ajaran,id_guru,id_kelas,id_mapel, hari, jam_ke))
    db.commit()
    return cursor.lastrowid

def get_data_jadwal(id_jadwal: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_jadwal WHERE id_jadwal=%s', (id_jadwal,))
    return cursor.fetchone()

def update_data_jadwal(id_jadwal: int, id_tahun_ajaran: int, id_guru: int,id_kelas: int, id_mapel: int, hari: str, jam_ke: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE tbl_jadwal SET id_tahun_ajaran=%s, id_guru=%s, id_kelas=%s, id_mapel=%s, hari=%s, jam_ke=%s WHERE id_jadwal=%s",(id_tahun_ajaran,id_guru,id_kelas ,id_mapel, hari, jam_ke, id_jadwal))
    db.commit()
    return cursor.fetchone()

def get_all_data_jadwal():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_jadwal")
    return cursor.fetchall()