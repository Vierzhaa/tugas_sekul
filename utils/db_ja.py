import mysql.connector

db = mysql.connector.connect (
    host='localhost',
    user='root',
    password='',
    database='db_jurnal'
)

def insert_data_ja(jenis_absensi: str):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO tbl_ja (jenis_absensi) VALUES (%s)", (jenis_absensi,))
    db.commit()
    return cursor.lastrowid

def get_data_ja(id_ja: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_ja WHERE id_ja=%s', (id_ja,))
    return cursor.fetchone()

def update_data_ja(id_ja: int,jenis_absensi: str):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE tbl_ja SET jenis_absensi=%s WHERE id_ja=%s",(jenis_absensi, id_ja))
    db.commit()
    return cursor.fetchone()

def get_all_data_ja():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_ja")
    return cursor.fetchall()
