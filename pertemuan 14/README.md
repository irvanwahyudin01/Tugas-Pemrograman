# PRAKTIKUM
tugas pertemuan 14 <br>
Nama : Irvan Wahyudin <br>
Nim : 312510359
<h2>Studi Kasus Validasi Data</h2>
<table boder="0"><tr><td valign="top">
<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%2014/img/per14.1.png" width="450" height="450">
</td></tr></table>

<h3>PENJELASAN PROGRAM</h3>
  
  1. Input Data
     Program meminta user untuk menginput :
     
     - Nama lengkap
     - Nomor Telepon
     - Email
       
  3. Memvalidasi Nama
     
     ``
     nama.replace(" ", "").isalpha()
     ``

     - replace(" ","") -> Menghapus spasi
     - isalpha() -> Memastikan hanya huruf yang diinputkan
       
  4. Memvalidasi Nomor Telepn

     ``
     telepon.isdigit()
     ``

     - isdigit() -> Untuk memastikan hanya angka yang diinputkan

  5. Memvalidasi Email

     ``
     "@" not in email or "." not in email
     ``

     - Email harus mengandung karakter @ dan .

  6. Menampilkan Hasil Error

     - Jika **tidak ada error** -> Program akan tampil **"Data Pendaftaran Valid"**
     - Jika ada kesalahan -> Program akan tampilkan **semua pesan error**
<h3>DOKUMENTASI SAAT PROGRAM DIJALANKAN</h3>


  <img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%2014/img/per14.2.png" width="250" height="150">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%2014/img/per14.3.png" width="250" height="150">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%2014/img/per14.4.png" width="250" height="150">
  
      
