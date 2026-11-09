const API_URL = 'http://127.0.0.1:5000/api';
let currentTipe = 'siswa';
let isEditMode = false;
let allData = [];

//load data dari py
async function loadData(tipe, event = null) {
    currentTipe = tipe;
    const titleCap = tipe.charAt(0).toUpperCase() + tipe.slice(1);
    document.getElementById('page-title').innerText = `Manajemen Data ${titleCap}`;

    if (event) {
        document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
        event.target.classList.add('active');
    }

    const tableHead = document.getElementById('table-head');
    const tableBody = document.getElementById('table-body');

    tableHead.innerHTML = `<th>Memuat kolom...</th>`;
    tableBody.innerHTML = `<tr><td class="text-center">Mengambil data...</td></tr>`;

    try {
        const response = await fetch(`${API_URL}/${tipe}`);
        if (!response.ok) throw new Error('Network response error');
        allData = await response.json(); // Simpan ke variabel global
        renderTable(allData, tipe, tableHead, tableBody);
    } catch (error) {
        tableBody.innerHTML = `<tr><td class="text-center" style="color:red;">Gagal mengambil data.</td></tr>`;
    }
}

//tabel
function renderTable(data, tipe, headElem, bodyElem) {
    headElem.innerHTML = '';
    bodyElem.innerHTML = '';
    let headers = [];

    if (tipe === 'siswa') headers = ['ID', 'Nama Siswa', 'ID Kelas', 'NISN', 'NIS', 'Aksi'];
    else if (tipe === 'guru') headers = ['ID', 'Nama Guru', 'NIP', 'Aksi'];
    else if (tipe === 'kelas') headers = ['ID', 'Nama Kelas', 'Aksi'];
    else if (tipe === 'rombel') headers = ['ID Rombel', 'ID Siswa', 'ID Kelas', 'Wali Kelas', 'Ketua Kelas', 'Aksi'];
    else if (tipe === 'jadwal') headers = ['ID Jadwal', 'ID tahun ajaran', 'ID guru','ID kelas','ID mapel','hari','jam ke', 'Aksi'];
    else if (tipe === 'absensi') headers = ['ID absensi', 'ID jurnal', 'ID siswa', 'ID JA', 'keterangan', 'Aksi'];

    headers.forEach(h => {
        headElem.innerHTML += `<th>${h}</th>`;
    });

    if (data.length === 0) {
        bodyElem.innerHTML = `<tr><td colspan="${headers.length}" class="text-center">Belum ada data.</td></tr>`;
        return;
    }

    data.forEach((item, index) => {
        let row = '<tr>';
        
        if (tipe === 'siswa') {
            row += `<td>${item.id_siswa}</td><td>${item.nama_siswa}</td><td>${item.id_kelas}</td><td>${item.nisn}</td><td>${item.nis}</td>`;
        } else if (tipe === 'guru') {
            row += `<td>${item.id_guru}</td><td>${item.nama_guru}</td><td>${item.nip}</td>`;
        } else if (tipe === 'kelas') {
            row += `<td>${item.id_kelas}</td><td>${item.kelas}</td>`;
        } else if (tipe === 'rombel') {
            row += `<td>${item.id_rombel}</td><td>${item.id_siswa}</td><td>${item.id_kelas}</td><td>${item.id_wali_kelas}</td><td>${item.id_ketua_kelas}</td>`;
        } else if (tipe === 'jadwal') {
            row += `<td>${item.id_jadwal}</td><td>${item.id_tahun_ajaran}</td><td>${item.id_guru}</td><td>${item.id_kelas}</td><td>${item.id_mapel}</td><td>${item.hari}</td><td>${item.jam_ke}</td>`;
        } else if (tipe === 'absensi') {
            row += `<td>${item.id_absensi}</td><td>${item.id_jurnal}</td><td>${item.id_siswa}</td><td>${item.id_ja}</td><td>${item.keterangan}</td>`;
        }

        row += `
            <td>
                <button onclick="siapkanEdit(${index})" style="background:#f39c12; color:white; border:none; padding:5px 10px; border-radius:3px; cursor:pointer;">Edit</button>
                <button style="background:#e74c3c; color:white; border:none; padding:5px 10px; border-radius:3px; cursor:pointer;">Hapus</button>
            </td>
        </tr>`;
        bodyElem.innerHTML += row;
    });
}

//form
function openModal() {
    isEditMode = false;
    document.getElementById('modal-title').innerText = "Tambah Data Baru";
    document.getElementById('input_id').value = '';
    buildFormFields(null); // Build form kosong
    document.getElementById('dataModal').style.display = 'flex';
}

function siapkanEdit(index) {
    isEditMode = true;
    document.getElementById('modal-title').innerText = "Edit Data";
    const item = allData[index];
    document.getElementById('input_id').value = item[`id_${currentTipe}`];
    buildFormFields(item); // Build form dengan isi data lama
    document.getElementById('dataModal').style.display = 'flex';
}

function buildFormFields(data) {
    const container = document.getElementById('form-fields-container');
    container.innerHTML = ''; // Bersihkan form lama
    let fields = [];

    if (currentTipe === 'siswa') fields = ['nama_siswa', 'id_kelas', 'nisn', 'nis'];
    else if (currentTipe === 'guru') fields = ['nama_guru', 'nip'];
    else if (currentTipe === 'kelas') fields = ['kelas'];
    else if (currentTipe === 'rombel') fields = ['id_siswa', 'id_kelas', 'id_wali_kelas', 'id_ketua_kelas'];
    else if (currentTipe === 'jadwal') fields = ['id_tahun_ajaran', 'id_guru', 'id_kelas', 'id_mapel', 'hari', 'jam_ke'];
    else if (currentTipe === 'absensi') fields = ['id_jurnal', 'id_siswa', 'id_ja', 'keterangan'];

    fields.forEach(f => {
        let val = data ? data[f] : '';
        let labelCap = f.replace(/_/g, ' ').toUpperCase();
        
        let inputType = (f.startsWith('id_') || f === 'nisn' || f === 'nis' || f === 'jam_ke' || f === 'nip') ? 'number' : 'text';

        container.innerHTML += `
            <div class="form-group">
                <label>${labelCap}</label>
                <input type="${inputType}" id="${f}" value="${val}" required>
            </div>
        `;
    });
}

async function submitForm(event) {
    event.preventDefault();
    let payload = {};
    const inputs = document.querySelectorAll('#form-fields-container input');
    
    inputs.forEach(input => {
        if (input.type === 'number') {
            payload[input.id] = parseInt(input.value, 10);
        } else {
            payload[input.id] = input.value;
        }
    });

    const id = document.getElementById('input_id').value;
    const method = isEditMode ? 'PUT' : 'POST';
    const url = isEditMode ? `${API_URL}/${currentTipe}/${id}` : `${API_URL}/${currentTipe}`;

    try {
        const response = await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            closeModal();
            loadData(currentTipe); // Refresh tabel
        } else {
            const errData = await response.json();
            alert("Terjadi kesalahan di server: " + (errData.error || ""));
        }
    } catch (error) {
        alert("Gagal menghubungi server.");
    }
}

function closeModal() {
    document.getElementById('dataModal').style.display = 'none';
}

window.onload = () => {
    loadData('siswa');
};
