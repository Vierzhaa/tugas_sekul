-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 28, 2026 at 04:58 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_jurnal`
--

-- --------------------------------------------------------

--
-- Table structure for table `detail_jurnal_mapel`
--

CREATE TABLE `detail_jurnal_mapel` (
  `id_detail` int(11) NOT NULL,
  `id_jurnal` int(11) NOT NULL,
  `materi_pembahasan` text NOT NULL,
  `catatan_kbm` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `detail_jurnal_mapel`
--

-- INSERT INTO `detail_jurnal_mapel` (`id_detail`, `id_jurnal`, `materi_pembahasan`, `catatan_kbm`) VALUES
-- (1, 2, 'Linear Equations', 'Siswa bisa memahami konsep dasar Linear Equation'),
-- (2, 3, 'Simple Past tense', 'Memahamai aturan dasar penggunanan simple past tense'),
-- (3, 2, 'Pengenalan Verba', 'Siswa dapat mengidentifikasi verba dalam kalimat.');

-- --------------------------------------------------------

--
-- Table structure for table `jurnal_kbm`
--

CREATE TABLE `jurnal_kbm` (
  `id_jurnal` int(11) NOT NULL,
  `id_jadwal` int(11) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jurnal_kbm`
--

-- INSERT INTO `jurnal_kbm` (`id_jurnal`, `id_jadwal`, `tanggal`) VALUES
-- (3, 2, '2026-07-24'),
-- (1, 3, '2026-07-24'),
-- (2, 5, '2026-07-24');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_absensi`
--

CREATE TABLE `tbl_absensi` (
  `id_absensi` int(11) NOT NULL,
  `id_jurnal` int(11) NOT NULL,
  `id_siswa` int(11) NOT NULL,
  `id_ja` int(11) NOT NULL,
  `keterangan` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_absensi`
--

-- INSERT INTO `tbl_absensi` (`id_absensi`, `id_jurnal`, `id_siswa`, `id_ja`, `keterangan`) VALUES
-- (1, 2, 1, 1, 'Hadir'),
-- (4, 2, 2, 3, 'Sakit'),
-- (5, 1, 3, 2, 'Sakit'),
-- (8, 3, 4, 1, 'Hadir'),
-- (15, 3, 3, 1, 'kurang tau');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_guru`
--

CREATE TABLE `tbl_guru` (
  `id_guru` int(11) NOT NULL,
  `nama_guru` varchar(255) NOT NULL,
  `nip` char(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_guru`
--

-- INSERT INTO `tbl_guru` (`id_guru`, `nama_guru`, `nip`) VALUES
-- (1, 'Budi Santoso', '1234567890'),
-- (2, 'John Doe', '123456'),
-- (3, 'JOHN WICK', '123456182738446'),
-- (4, 'SATRIA UTAMA', '012367481792758324'),
-- (5, 'EVI MUAFIA', '012367481792758325'),
-- (6, 'NOVA', '012367481792758326'),
-- (7, 'SITI ROHANA', '012367481792758327'),
-- (8, 'DIAN WIBOWO', '012367481792758328');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_ja`
--

CREATE TABLE `tbl_ja` (
  `id_ja` int(11) NOT NULL,
  `jenis_absensi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_ja`
--

-- INSERT INTO `tbl_ja` (`id_ja`, `jenis_absensi`) VALUES
-- (1, 'Hadir'),
-- (2, 'Sakit'),
-- (3, 'Alpha'),
-- (4, 'Izin');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_jadwal`
--

CREATE TABLE `tbl_jadwal` (
  `id_jadwal` int(11) NOT NULL,
  `id_tahun_ajaran` int(11) NOT NULL,
  `id_guru` int(11) NOT NULL,
  `id_kelas` int(11) NOT NULL,
  `id_mapel` int(11) NOT NULL,
  `hari` varchar(10) NOT NULL,
  `jam_ke` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_jadwal`
--

-- INSERT INTO `tbl_jadwal` (`id_jadwal`, `id_tahun_ajaran`, `id_guru`, `id_kelas`, `id_mapel`, `hari`, `jam_ke`) VALUES
-- (1, 1, 7, 2, 2, 'Selasa', 2),
-- (2, 1, 8, 2, 8, 'Senin', 4),
-- (3, 1, 5, 1, 6, 'Selesa', 9),
-- (4, 1, 4, 2, 7, 'Senin', 3),
-- (5, 1, 6, 1, 3, 'Rabu', 1),
-- (6, 1, 7, 2, 5, 'Kamis', 7);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_kelas`
--

CREATE TABLE `tbl_kelas` (
  `id_kelas` int(11) NOT NULL,
  `kelas` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_kelas`
--

-- INSERT INTO `tbl_kelas` (`id_kelas`, `kelas`) VALUES
-- (1, 'X RPL'),
-- (2, 'XI RPL'),
-- (3, 'XII RPL');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_mapel`
--

CREATE TABLE `tbl_mapel` (
  `id_mapel` int(11) NOT NULL,
  `nama_mapel` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_mapel`
--

-- INSERT INTO `tbl_mapel` (`id_mapel`, `nama_mapel`) VALUES
-- (4, 'Bahasa Indonesia'),
-- (3, 'Bahasa Inggris'),
-- (7, 'KIK'),
-- (1, 'Matematika'),
-- (8, 'MK RPL'),
-- (6, 'PAIBP'),
-- (5, 'PKN'),
-- (2, 'Sejarah'),
-- (9, 'Seni Tari');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_rombel`
--

CREATE TABLE `tbl_rombel` (
  `id_rombel` int(11) NOT NULL,
  `id_siswa` int(11) NOT NULL,
  `id_kelas` int(11) NOT NULL,
  `id_wali_kelas` int(11) NOT NULL,
  `id_ketua_kelas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_rombel`
--

-- INSERT INTO `tbl_rombel` (`id_rombel`, `id_siswa`, `id_kelas`, `id_wali_kelas`, `id_ketua_kelas`) VALUES
-- (1, 1, 2, 5, 3);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_siswa`
--

CREATE TABLE `tbl_siswa` (
  `id_siswa` int(11) NOT NULL,
  `nama_siswa` varchar(255) NOT NULL,
  `id_kelas` int(11) NOT NULL,
  `nisn` varchar(10) NOT NULL,
  `nis` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_siswa`
--

-- INSERT INTO `tbl_siswa` (`id_siswa`, `nama_siswa`, `id_kelas`, `nisn`, `nis`) VALUES
-- (1, 'Muhammad Kevin Maulana', 2, '0103346424', '0281748264'),
-- (2, 'Budi', 3, '12345', '67890'),
-- (3, 'Rizky', 1, '1234567890', '0987654321'),
-- (4, 'Dimas Satria', 3, '0101123081', '2734682'),
-- (5, 'Galang', 1, '6576547564', '2373259590'),
-- (6, 'RAFA MAULANA ', 1, '0104336615', '65789'),
-- (7, 'Hermione', 2, '103050709', '13579');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_tahun_ajaran`
--

CREATE TABLE `tbl_tahun_ajaran` (
  `id_tahun_ajaran` int(11) NOT NULL,
  `tahun` varchar(9) NOT NULL,
  `semester` enum('Ganjil','Genap') NOT NULL,
  `status` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_tahun_ajaran`
--

-- INSERT INTO `tbl_tahun_ajaran` (`id_tahun_ajaran`, `tahun`, `semester`, `status`) VALUES
-- (1, '2026/2027', 'Ganjil', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `detail_jurnal_mapel`
--
ALTER TABLE `detail_jurnal_mapel`
  ADD PRIMARY KEY (`id_detail`),
  ADD KEY `id_jurnal` (`id_jurnal`);

--
-- Indexes for table `jurnal_kbm`
--
ALTER TABLE `jurnal_kbm`
  ADD PRIMARY KEY (`id_jurnal`),
  ADD UNIQUE KEY `uq_jadwal_tanggal` (`id_jadwal`,`tanggal`);

--
-- Indexes for table `tbl_absensi`
--
ALTER TABLE `tbl_absensi`
  ADD PRIMARY KEY (`id_absensi`),
  ADD UNIQUE KEY `uq_absensi_jurnal_siswa` (`id_jurnal`,`id_siswa`),
  ADD KEY `id_ja` (`id_ja`) USING BTREE;

--
-- Indexes for table `tbl_guru`
--
ALTER TABLE `tbl_guru`
  ADD PRIMARY KEY (`id_guru`),
  ADD UNIQUE KEY `nip` (`nip`);

--
-- Indexes for table `tbl_ja`
--
ALTER TABLE `tbl_ja`
  ADD PRIMARY KEY (`id_ja`);

--
-- Indexes for table `tbl_jadwal`
--
ALTER TABLE `tbl_jadwal`
  ADD PRIMARY KEY (`id_jadwal`),
  ADD UNIQUE KEY `uq_jadwal` (`id_tahun_ajaran`,`id_guru`,`id_kelas`,`hari`,`jam_ke`),
  ADD UNIQUE KEY `uq_kelas_jadwal` (`id_tahun_ajaran`,`id_kelas`,`hari`,`jam_ke`),
  ADD UNIQUE KEY `uq_guru_jadwal` (`id_tahun_ajaran`,`id_guru`,`hari`,`jam_ke`),
  ADD KEY `id_guru` (`id_guru`),
  ADD KEY `id_kelas` (`id_kelas`),
  ADD KEY `id_mapel` (`id_mapel`);

--
-- Indexes for table `tbl_kelas`
--
ALTER TABLE `tbl_kelas`
  ADD PRIMARY KEY (`id_kelas`),
  ADD UNIQUE KEY `kelas` (`kelas`);

--
-- Indexes for table `tbl_mapel`
--
ALTER TABLE `tbl_mapel`
  ADD PRIMARY KEY (`id_mapel`),
  ADD UNIQUE KEY `nama_mapel` (`nama_mapel`);

--
-- Indexes for table `tbl_rombel`
--
ALTER TABLE `tbl_rombel`
  ADD PRIMARY KEY (`id_rombel`),
  ADD KEY `id_siswa` (`id_siswa`),
  ADD KEY `id_kelas` (`id_kelas`),
  ADD KEY `id_wali_kelas` (`id_wali_kelas`),
  ADD KEY `id_ketua_kelas` (`id_ketua_kelas`);

--
-- Indexes for table `tbl_siswa`
--
ALTER TABLE `tbl_siswa`
  ADD PRIMARY KEY (`id_siswa`),
  ADD UNIQUE KEY `nisn` (`nisn`,`nis`),
  ADD UNIQUE KEY `uq_siswa_nisn` (`nisn`),
  ADD UNIQUE KEY `uq_siswa_nis` (`nis`),
  ADD KEY `id_kelas` (`id_kelas`);

--
-- Indexes for table `tbl_tahun_ajaran`
--
ALTER TABLE `tbl_tahun_ajaran`
  ADD PRIMARY KEY (`id_tahun_ajaran`),
  ADD UNIQUE KEY `uq_tahun_semester` (`tahun`,`semester`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `detail_jurnal_mapel`
--
ALTER TABLE `detail_jurnal_mapel`
  MODIFY `id_detail` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `jurnal_kbm`
--
ALTER TABLE `jurnal_kbm`
  MODIFY `id_jurnal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_absensi`
--
ALTER TABLE `tbl_absensi`
  MODIFY `id_absensi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `tbl_guru`
--
ALTER TABLE `tbl_guru`
  MODIFY `id_guru` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tbl_ja`
--
ALTER TABLE `tbl_ja`
  MODIFY `id_ja` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_jadwal`
--
ALTER TABLE `tbl_jadwal`
  MODIFY `id_jadwal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_kelas`
--
ALTER TABLE `tbl_kelas`
  MODIFY `id_kelas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tbl_mapel`
--
ALTER TABLE `tbl_mapel`
  MODIFY `id_mapel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tbl_rombel`
--
ALTER TABLE `tbl_rombel`
  MODIFY `id_rombel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_siswa`
--
ALTER TABLE `tbl_siswa`
  MODIFY `id_siswa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tbl_tahun_ajaran`
--
ALTER TABLE `tbl_tahun_ajaran`
  MODIFY `id_tahun_ajaran` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `detail_jurnal_mapel`
--
ALTER TABLE `detail_jurnal_mapel`
  ADD CONSTRAINT `detail_jurnal_mapel_ibfk_1` FOREIGN KEY (`id_jurnal`) REFERENCES `jurnal_kbm` (`id_jurnal`);

--
-- Constraints for table `jurnal_kbm`
--
ALTER TABLE `jurnal_kbm`
  ADD CONSTRAINT `jurnal_kbm_ibfk_1` FOREIGN KEY (`id_jadwal`) REFERENCES `tbl_jadwal` (`id_jadwal`);

--
-- Constraints for table `tbl_absensi`
--
ALTER TABLE `tbl_absensi`
  ADD CONSTRAINT `tbl_absensi_ibfk_1` FOREIGN KEY (`id_siswa`) REFERENCES `tbl_siswa` (`id_siswa`),
  ADD CONSTRAINT `tbl_absensi_ibfk_2` FOREIGN KEY (`id_ja`) REFERENCES `tbl_ja` (`id_ja`),
  ADD CONSTRAINT `tbl_absensi_ibfk_3` FOREIGN KEY (`id_jurnal`) REFERENCES `jurnal_kbm` (`id_jurnal`);

--
-- Constraints for table `tbl_jadwal`
--
ALTER TABLE `tbl_jadwal`
  ADD CONSTRAINT `tbl_jadwal_ibfk_1` FOREIGN KEY (`id_guru`) REFERENCES `tbl_guru` (`id_guru`),
  ADD CONSTRAINT `tbl_jadwal_ibfk_2` FOREIGN KEY (`id_kelas`) REFERENCES `tbl_kelas` (`id_kelas`),
  ADD CONSTRAINT `tbl_jadwal_ibfk_3` FOREIGN KEY (`id_mapel`) REFERENCES `tbl_mapel` (`id_mapel`),
  ADD CONSTRAINT `tbl_jadwal_ibfk_4` FOREIGN KEY (`id_tahun_ajaran`) REFERENCES `tbl_tahun_ajaran` (`id_tahun_ajaran`);

--
-- Constraints for table `tbl_rombel`
--
ALTER TABLE `tbl_rombel`
  ADD CONSTRAINT `tbl_rombel_ibfk_1` FOREIGN KEY (`id_siswa`) REFERENCES `tbl_siswa` (`id_siswa`),
  ADD CONSTRAINT `tbl_rombel_ibfk_2` FOREIGN KEY (`id_kelas`) REFERENCES `tbl_kelas` (`id_kelas`),
  ADD CONSTRAINT `tbl_rombel_ibfk_3` FOREIGN KEY (`id_wali_kelas`) REFERENCES `tbl_guru` (`id_guru`),
  ADD CONSTRAINT `tbl_rombel_ibfk_4` FOREIGN KEY (`id_ketua_kelas`) REFERENCES `tbl_siswa` (`id_siswa`);

--
-- Constraints for table `tbl_siswa`
--
ALTER TABLE `tbl_siswa`
  ADD CONSTRAINT `tbl_siswa_ibfk_1` FOREIGN KEY (`id_kelas`) REFERENCES `tbl_kelas` (`id_kelas`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
