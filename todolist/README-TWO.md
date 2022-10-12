# Tugas 6 Javascript dan AJAX

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

[link heroku munifah nurfadhilah - 2106654851](http://tugas2pudil.herokuapp.com/todolist/)

### **Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
- Asynchronous programming: Program bisa menjalankan beberapa tugas secara bersamaan. Ketika terjadi pemanggilan sebuah function asynchronous, baris code selanjutnya dapat dijalankan tanpa perlu menunggu function tersebut selesai.  (concurrent)

- Synchronous programming: Program berjalan secara berurutan. Saat satu tugas dilaksanakan, instruksi untuk menjalankan tugas lain diblokir. Tugas pertama harus selesai untuk menjalankan tugas selanjutnya. (sequential)

### **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Event-Driven Programming adalah ketika suatu program dieksekusi berdasarkan event yang ada. Event-Driven Programming bergantung pada event, sehingga alur program dapat dijalankan secara tidak terurut dengan menerapkan konsep asynchronous programming. Pada tugas ini, salah satu penerapan Event-Driven Programming adalah ketika button create di click, maka akan dijalankan suatu fungsi untuk membuat create task. Fungsi ini akan selalu dijalankan jika terdapat event yaitu click. 

### **Jelaskan penerapan asynchronous programming pada AJAX.**
Asynchronus programming pada AJAX adalah ketika sebuah event terjadi, event tersebut akan menjalankan fungsionalitas AJAX. Misalnya pada tugas 6 ini ketika mengklik button create pada form untuk membuat task baru, akan dilakukan AJAX POST untuk mengirim data ke server. Setelah server selesai mengolah data tersebut, akan dijalankan callback function yang telah dibuat sebelumnya. Data yang ditangkap akan dikirimkan ke server tanpa melalui browser reload sehingga memberikan pengalaman browsing lebih baik.

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
AJAX GET 
- Pada views.py, ditambahkan function untuk mengambil task yang sesuai dengan user login saat itu dalam bentuk JSON. Views akan terhubung setelah kita menambahkan routing path pada urls.py. Ketika website selesai load, AJAX GET terpanggil untuk mendapatkan task dalam bentuk JSON yang dimasukkan ke dalam masing-masing cards.
##
AJAX POST
- Button create yang sebelumnya redirect ke todolist/create_task, kita ubah agar dapat memunculkan modal. Implementasinya, pada views.py ditambahkan function create_task_modal dan views akan terhubung setelah kita menambahkan routing path pada urls.py. Pada function diterapkan asynchronous programming sehingga task akan terupdate tanpa reload website. 