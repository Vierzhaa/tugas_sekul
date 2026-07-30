import mysql.connector

db = mysql.connector.connect (
    host='localhost',
    user='root',
    password='',
    database='db_jurnal'
)

def insert_data_detail(id_jurnal: str, materi_pembahasan: str, catatan_kbm: int):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO detail_jurnal_mapel (id_jurnal, materi_pembahasan, catatan_kbm) VALUES (%s,%s,%s)", (id_jurnal, materi_pembahasan, catatan_kbm))
    db.commit()
    return cursor.lastrowid

def get_data_detail(id_detail: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM detail_jurnal_mapel WHERE id_detail=%s', (id_detail,))
    return cursor.fetchone()

def update_data_detail(id_detail: int, id_jurnal: str, materi_pembahasan: str, catatan_kbm: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE detail_jurnal_mapel SET id_jurnal=%s, materi_pembahasan=%s, catatan_kbm=%s WHERE id_detail=%s",(id_jurnal, materi_pembahasan, catatan_kbm, id_detail))
    db.commit()
    return cursor.fetchone()

def get_all_data_detail():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM detail_jurnal_mapel")
    return cursor.fetchall()