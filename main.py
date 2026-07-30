from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import *

app = Flask(__name__,)
CORS(app) 


@app.route('/api/siswa', methods=['GET', 'POST'])
def api_siswa():
    if request.method == 'GET':
        try:
            data = get_all_data_siswa() 
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    elif request.method == 'POST':
        try:
            data = request.json
            new_id = insert_data_siswa(data['nama_siswa'], data['id_kelas'], data['nisn'], data['nis'])
            return jsonify({"message": "Data berhasil ditambahkan", "id_siswa": new_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500



@app.route('/api/guru', methods=['GET', 'POST'])
def api_guru():
    if request.method == 'GET':
        try:
            data = get_all_data_guru() 
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    elif request.method == 'POST':
        try:
            data = request.json
            new_id = insert_data_guru(data['nama_guru'], data['nip'])
            return jsonify({"message": "Data berhasil ditambahkan", "id_guru": new_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500



@app.route('/api/kelas', methods=['GET', 'POST'])
def api_kelas():
    if request.method == 'GET':
        try:
            data = get_all_data_kelas()
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    elif request.method == 'POST':
        try:
            data = request.json
            new_id = insert_data_kelas(data['kelas'])
            return jsonify({"message": "Data berhasil ditambahkan", "id_kelas": new_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.route('/api/rombel', methods=['GET', 'POST'])
def api_rombel():
    if request.method == 'GET':
        try:
            data = get_all_data_rombel()
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    elif request.method == 'POST':
        try:
            data = request.json
            new_id = insert_data_rombel(data['id_siswa'], data['id_kelas'], data['id_wali_kelas'], data['id_ketua_kelas'])
            return jsonify({"message": "Data berhasil ditambahkan", "id_rombel": new_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500



@app.route('/api/jadwal', methods=['GET', 'POST'])
def api_jadwal():
    if request.method == 'GET':
        try:
            data = get_all_data_jadwal()
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    elif request.method == 'POST':
        try:
            data = request.json
            new_id = insert_data_jadwal(data['id_tahun_ajaran'], data['id_guru'], data['id_kelas'], data['id_mapel'], data['hari'], data['jam_ke'])
            return jsonify({"message": "Data berhasil ditambahkan", "id_jadwal": new_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.route('/api/absensi', methods=['GET', 'POST'])
def api_absensi():
    if request.method == 'GET':
        try:
            data = get_all_data_absensi()
            return jsonify(data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    elif request.method == 'POST':
        try:
            data = request.json
            new_id = insert_data_absensi(data['id_jurnal'],data['id_siswa'],data['id_ja'],data['keterangan'])
            print("hai")
            return jsonify({"message": "Data berhasil ditambahkan","id_absensi": new_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500






@app.route('/api/jadwal/<int:id>', methods=['PUT'])
def update_jadwal(id):
    try:
        data = request.json
        update_data_jadwal(id, data['id_tahun_ajaran'], data['id_guru'], data['id_kelas'], data['id_mapel'], data['hari'], data['jam_ke'])
        return jsonify({"message": "data jadwal berhasil diupdate"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/siswa/<int:id>', methods=['PUT'])
def update_siswa(id):
    try:
        data = request.json
        update_data_siswa(id, data['nama_siswa'], data['id_kelas'], data['nisn'], data['nis'])
        return jsonify({"message": "Data siswa berhasil diupdate"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/guru/<int:id>', methods=['PUT'])
def update_guru(id):
    try:
        data = request.json
        update_data_guru(id, data['nama_guru'], data['nip'])
        return jsonify({"message": "Data guru berhasil diupdate"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/kelas/<int:id>', methods=['PUT'])
def update_kelas(id):
    try:
        data = request.json
        update_data_kelas(id, data['kelas'])
        return jsonify({"message": "Data kelas berhasil diupdate"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/rombel/<int:id>', methods=['PUT'])
def update_rombel(id):
    try:
        data = request.json
        update_data_rombel(id, data['id_siswa'], data['id_kelas'], data['id_wali_kelas'], data['id_ketua_kelas'])
        return jsonify({"message": "Data rombel berhasil diupdate"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/absensi/<int:id>', methods=['PUT'])
def update_absensi(id):
    try:
        data = request.json
        update_data_absensi(id, data['id_jurnal'], data['id_siswa'], data['id_ja'], data['keterangan'])
        print("hai")
        return jsonify({"message": "Data absensi berhasil diupdate"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)