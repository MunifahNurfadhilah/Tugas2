# Tugas 4 Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

[link heroku munifah nurfadhilah - 2106654851](http://tugas2pudil.herokuapp.com/todolist/)

### **Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?**
{% csrf_token %} dapat mencegah serangan Cross-site Request Forgery (CSRF). csrf token akan membandingkan dua token yang ditemukan pada user dan request. jika token yang dibandingkan tidak cocok, maka permintaan pada form akan ditolak. jika token yang dibandingkan cocok, maka form akan merespon OK.
jika tidak terdapat potongan kode {% csrf_token %}, form yang ada tetap dapat berjalan. akan tetapi beberapa route link bisa saja diakses oleh orang lain. akun yang kita miliki bisa saja hilang/dihapus diluar kuasa kita, jika seseorang memiliki akses ke href link tersebut.

### **Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.**
kita dapat membuat form secara manual tanpa memanfaatkan generator. Kita dapat memanfaatkan method POST dan {% csrf_token %}. Kita juga perlu membuat tag table dan di dalamnya terdapat tr yang digunakan untuk membuat tag input text beserta input type submit. Setelah user menekan tombol submit, maka input text yang telah diisi oleh user akan disubmit ke server.

### **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**
user memasukkan data pada form HTML yang sudah dirender dan disubmit setelah menekan tombol submit. kemudian, views.py akan mengakses dan mengolah data tersebut. apabila kita memasukkan data yang belum ada di database, maka akan dibuat objek baru di database. jika hanya mengubah bagian dari data yang sudah ada, maka data di database juga hanya dirubah. kemudian, data yang dibutuhkan pada HTML dapat diakses setelah proses rendering selesai.  

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
- membuat aplikasi todolist, menjalankan perintah python manage.py startapp todolist, dan menambahkan aplikasi todolist pada installed apps di settings.py project django
- menambahkan path todolist ke urls.py di project django agar dapat routing todolist dan dapat mengakses http://localhost:8000/todolist
- membuat class bernama Task pada models.py dan membuat field user, date, title, description, dan is_finished beserta tipe field nya
- membuat fungsi-fungsi di views.py yaitu, register, login, logout. kita juga menambahkan @login_required(login_url='/todolist/login/') agar user perlu untuk login terlebih dahulu. kita juga perlu membuat register.html dan login.html
- membuat todolist.html agar nama user dapat ditampilkan dengan sesuai. kita dapat menggunakan {{username}}. kita jga membuat 2 button yaitu, create task untuk menambah task dan logout. kita juga perlu membuat tabel untuk menampilkan task tersebut.
- membuat create_task html untuk ditampilkan ke user ketika akan membuat task baru. pada views.py juga ditambahkan fungction create_task untuk menghandle logic task yang baru.
- membuat bonus, yaitu atribut is_finished untuk merubah status task dan button status untuk menghapus data yang ada pada database.
- deploy ke heroku berjalan secara otomatis dengan push ke repo github. kemudian register 2 akun di herokuapp dengan masing-masing akun membuat 3 task. 