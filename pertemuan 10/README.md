# PRAKTIKUM
tugas pertemuan 10 <br>
Nama : Irvan Wahyudin <br>
Nim : 312510359
<h2>penggunaan list</h2>
<table boder="0"><tr><td valign="top"><h3>DALAM FLOWCHART</h3>
<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%2010/img/per10fc.png?raw=true" width="650" height="750">
<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%2010/img/per10fc1.png?raw=true" width="650" height="750"></td>
<td valign="top"><h3>DALAM PYHTON</h3>
<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%2010/img/per10.1.png?raw=true" width="450" height="450">
<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%2010/img/per10.2.png?raw=true" width="450" height="450">
<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%2010/img/per10.3.png?raw=true" width="450" height="450"></td></tr></table>
<h3>PENJELASAN SETIAP CODE</h3><ol>
<p><li>data_mahasiswa={}, ini adalah tempat untuk menyimpan data mahasiswa dengan KEY : NIM mahasiswa dan VALUE : Nama,Nilai tugas,Nilai UTS, Nilai UAS, Nilai Akhir.</li></p>

**contoh isi data**
  ```
{ 
  "2501232" : {
    "nama" : "why"
    "tugas" : 80,
    "uts" : 85,
    "uas" : 90,
    "akhir" : 86
  }
}
```

<p><li>Ada beberapa menu program</li></p>

```
(L)ihat  → Menampilkan data mahasiswa
(T)ambah → Menambahkan data mahasiswa
(U)bah   → Mengubah data mahasiswa berdasarkan NIM
(H)apus  → Menghapus data mahasiswa berdasarkan NIM
(C)ari   → Mencari data mahasiswa berdasarkan NIM
(K)eluar → Menghentikan program
```
<li>Menu Tambah Data (T).</li>

  - User memasukan NIM, Nama, Nilai Tugas, UTS, dan UAS
  - Program menghitung nilai akhir dengan rumus
    ```
    Nilai Akhir = (Tugas × 30%) + (UTS × 35%) + (UAS × 35%)
    ```
  - data akan disimpan ke dalam directory **data mahasiswa**

<br><li>Menu Lihat Data (L).</li>

  - Menampilkan seluruh data mahasiswa dalam bentuk tabel
  - Jika data kosong, akan muncul pesan "TIDAK ADA DATA MAHASISWA"
  - Penomoran data dilakukan secara otomatis

<br><li>Menu Ubah Data (U).</li>

  - User memasukan NIM Mahasiswa
  - Jika NIM ditemukan, program akan meminta data baru untuk diganti
  - Jika NIM tidak ditemukan, program akan menampilkan pesan kesalahan

<br><li>Menu Cari Data (C).</li>

  - User memasukan NIM Mahasiswa
  - Program akan menampilkan detail lengkap mahasiswa yang dicari
  - Jika NIM tidak ada, program akan menampilkan pesan bahwa data tersebut tidak ditemukan

<br><li>Menu Hapus Data (H).</li>

  - User memasukan NIM Mahasiswa
  - Data mahasiswa akan dihapus jika NIM ditemukan

<br><li>Menu Keluar (K).</li>
  Untuk perulangan sehingga program berakhir 

<h3>Dokumentasi Saat Program Dijalankan</h3>
<P><img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%209/img/img6.jpg" width="250" height="150">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/irvanwahyudin01/Tugas-Pemrograman/blob/main/pertemuan%209/img/img7.jpg" width="250" height="150"></P>

