import mysql.connector

from .connection import db

def insert_data_nama_mapel(nama_mapel: str):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO tbl_mapel (nama_mapel) VALUES (%s)", (nama_mapel,))
    db.commit()
    return cursor.lastrowid

def get_data_nama_mapel(id_mapel: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_mapel WHERE id_mapel=%s', (id_mapel,))
    return cursor.fetchone()

def update_data_nama_mapel(id_mapel: int,nama_mapel: str):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE tbl_mapel SET nama_mapel=%s WHERE id_mapel=%s",(nama_mapel, id_mapel))
    db.commit()
    return cursor.fetchone()

def delete_data_nama_mapel(id_mapel: int):
    try:
        cursor = db.cursor(dictionary=True)
        # cursor = db.cursor()
        sql = 'DELETE FROM tbl_mapel WHERE id_mapel= %s'
        cursor.execute(sql, (id_mapel,))
        
        db.commit()
        
        return cursor.rowcount
        
    except Exception as e:
        db.rollback()
        print(f"Terjadi error: {e}")
        return False

def get_all_data_mapel():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_mapel")
    return cursor.fetchall()

