import mysql.connector

db = mysql.connector.connect (
    host='localhost',
    user='root',
    password='',
    database='db_jurnal'
)

def insert_data_kelas(kelas: str):
    cursor=db.cursor(dictionary=True)
    cursor.execute("INSERT INTO tbl_kelas (kelas) VALUES (%s)", (kelas,))
    db.commit()
    return cursor.lastrowid

def get_data_kelas(id_kelas: int):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_kelas WHERE id_kelas=%s', (id_kelas,))
    return cursor.fetchone()

def update_data_kelas(id_kelas: int,kelas: str):
    cursor = db.cursor(dictionary=True)
    # cursor = db.cursor()
    cursor.execute("UPDATE tbl_kelas SET kelas=%s WHERE id_kelas=%s",(kelas, id_kelas))
    db.commit()
    return cursor.fetchone()

def delete_data_kelas(id_kelas: int):
    try:
        cursor = db.cursor(dictionary=True)
        # cursor = db.cursor()
        sql = 'DELETE FROM tbl_kelas WHERE id_kelas= %s'
        cursor.execute(sql, (id_kelas,))
        
        db.commit()
        
        return cursor.rowcount
        
    except Exception as e:
        db.rollback()
        print(f"Terjadi error: {e}")
        return False

def get_all_data_kelas():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_kelas")
    return cursor.fetchall()