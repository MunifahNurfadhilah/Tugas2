# Tugas 2 Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

**Bagan request client ke web aplikasi berbasis Django**
![Gambar]('../../pbp.jpg?raw=true')

https://tugas2pudil.herokuapp.com/katalog

Penjelasan : 
User memberikan request akan diterima oleh urls.py dan diarahkan ke halaman views.py yang bersangkutan. Setelah diterima oleh views.py, fungsi yang berada pada views.py akan dijalankan dan mengquery data dengan models.py sebagai penghubung. Jika request dari user sudah selesai di proses, hasil data akan di return sebagai response dan hasilnya akan di render oleh template untuk diperlihatkan ke user. 

**Kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Penjelasan : 
Virtual environment digunakan agar tidak terjadi crash dengan versi lain yang ada pada device kita. Virtual environment akan mengisolasi package dan dependecies dari aplikasi. Jika kita tidak menggunakan virtual environment dalam membuat aplikasi web berbasis Django, maka update packages dan dependancies dari aplikasi akan otomatis mengubah data pada local storage dan akan terjadi perbedaan versi dari data-data tersebut. 

**Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

Penjelasan : 
Views.py --> Mengambil seluruh data yang ada pada database, memambahkan variabel seperti nama dan npm yang akan disimpan dalam variabel context dan akan ikut di render dengan memanggil fungsi show_katalog, sehingga data tersebut muncul pada halaman HTML. 

Urls.py --> Routing terhadap fungsi show_katalog sehingga halaman HTLM dapat ditampilkan melalui browser. Pada urls.py, saya menambahkan path aplikasi katalog ke dalam urs.py yang terdapat pada folder project_django.

Katalog.py --> For loop digunakan untuk mengambil data pada database yang akan disimpan ke dalam variabel list_barang.

Deploy --> Mehubungkan repo github saya ke heroku app dan melakukan deploy. Proses ini memerlukan HEROKU_APP_NAME beserta nama app yang saya buat dan HEROKU_API_KEY di github secret action. 
