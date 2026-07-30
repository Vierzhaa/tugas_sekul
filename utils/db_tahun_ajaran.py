import mysql.connector

db = mysql.connector.connect (
    host='localhost',
    user='root',
    password='',
    database='db_jurnal'
)

def insert_data_tahun(tahun: str, semester: str, status: int):
    if semester != "Ganjil" or semester != "Genap":
        print("semester harus Ganjil atau Genap")
        return
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO tbl_tahun_ajaran (tahun, semester, status) VALUES (%s,%s,%s)", (tahun, semester, status))
    db.commit()
    return cursor.lastrowid

def get_data_tahun(id_tahun_ajaran: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_tahun_ajaran WHERE id_tahun_ajaran=%s', (id_tahun_ajaran,))
    return cursor.fetchone()



def update_data_tahun(id_tahun_ajaran: int, tahun: str, semester: str, status: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE tbl_tahun_ajaran SET tahun=%s, semester=%s, status=%s WHERE id_tahun_ajaran=%s",(tahun, semester, status, id_tahun_ajaran))
    db.commit()
    return cursor.fetchone()

