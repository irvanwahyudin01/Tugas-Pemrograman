# UJIAN AKHIR SEMESTER
<br>
Nama : Irvan Wahyudin <br>
Nim : 312510359
<h2>Program Rating</h2>
<table boder="0"><tr>
<td valign="top"><h3>CODE PYHTON</h3>
<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/file%20uas/img/uas1.png" width="450" height="450"><br>
<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/file%20uas/img/uas2.png" width="450" height="450"><br>
<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/file%20uas/img/uas3.png" width="450" height="450"></td></tr></table>
<h2>PENJELASAN SETIAP CODE</h2><ol>

## Struktur Program

Program ini terdiri dari beberapa class

### 1. Feedback
Berfungsi sebagai simpan data feedback yang diinputkan user

**Atribut**
- nama >> Nama pelanggan
- rating >> Nilai rating

### 2. FeedbackService
Berfungsi untuk mengolah data dan logika pada program

**Method**
- tambah_feedback() >> Menambahkan feedback ke dalam list
- rata_rata_rating() >> Menghitung rata-rata rating
- kategori_kepuasan() >> Menentukan Kategori kepuasan

**Kategori Kepuasan**
| Rating | Kategori |
|------|----------|
| ≥ 4 | Sangat Puas |
| ≥ 3 | Puas |
| ≥ 2 | Cukup |
| < 2 | Tidak Puas |

### 3. FeedbackView
Berfungsi untuk menampilkan atau berinteraksi dengan user

**Method**
- input_feedback() >> Input nama dan rating dengan validasi ('try-except')
- tampilkan_tabel() >> Menampilkan tabel kepuasan pelangan

### 4. main()
mengatur alur utama program
1. Input data feedback secara berulang dikarenakan kita memberi perulangan for true
2. Dia mengatur untuk menyimpat data ke dalam list
3. Dan menampilkan tabel dan rata-rata rating
   
<h3>Dokumentasi Saat Program Dijalankan</h3>
<P><img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/file%20uas/img/uas4.png" width="250" height="150">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/file%20uas/img/uas5.png" width="250" height="150">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/file%20uas/img/uas6.png" width="250" height="150">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/file%20uas/img/uas7.png" width="250" height="150"></P>

