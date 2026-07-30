import mysql.connector

db = mysql.connector.connect (
    host='localhost',
    user='root',
    password='',
    database='db_jurnal'
)

def insert_data_absensi(id_jurnal: int,id_siswa: int, id_ja: int, keterangan: str):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO tbl_absensi (id_jurnal, id_siswa, id_ja, keterangan) VALUES (%s,%s,%s,%s)", (id_jurnal,id_siswa,id_ja,keterangan))
    db.commit()
    return cursor.lastrowid

def get_data_absensi(id_absensi: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_absensi WHERE id_absensi=%s', (id_absensi,))
    return cursor.fetchone()

def get_all_data_absensi():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_absensi")
    return cursor.fetchall()

def update_data_absensi(id_absensi: int,id_jurnal: int, id_siswa: int,id_ja, keterangan: str):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE tbl_absensi SET id_jurnal=%s, id_siswa=%s, id_ja=%s, keterangan=%s WHERE id_absensi=%s",(id_jurnal,id_siswa,id_ja ,keterangan, id_absensi))
    db.commit()
    return cursor.fetchone()
