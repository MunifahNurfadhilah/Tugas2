# Tugas 3 Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

link heroku :
https://tugas2pudil.herokuapp.com/mywatchlist/

### **Jelaskan perbedaan antara JSON, XML, dan HTML!**
- HTMl (Hypertext Markup Language) adalah markup language yang merepresentasikan data dalam element tree untuk ditampilkan dalam bentuk web dan dapat di-kostumisasi cara penyajiannya

- JSON (JavaScript Object Notation) adalah format dalam bentuk JavaScript untuk merepresentasikan data dengan bentuk yang efisien yang terdiri dari key dan value. JSON lebih cepat pengaksesannya dan lebih mudah dibaca mesin. Akan tetapi, file JSON ini kurang rapih untuk dilihat secara visual karena tidak menggunakan tag seperti xml dan html. 

- XML (Extensive Markup Language) adalah salah satu bahasa yang dapat digunakan untuk menyimpan dan mengantarkan data. Penyimpanan file yang dilakukan XML mirip seperti HTML yang lebih mudah dibaca dengan menggunakan tags. 

### **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery berarti terjadi pertukaran data user dengan data yang ada di server. Data delivery mempermudah kita untuk melakukan pengiriman data. Data delivery biasanya menggunakan format HTML, XML, dan JSON agar data yang dikirim dapat diterima dengan baik oleh user dan mudah dipahami serta di-develop oleh berbagai programming language. 

### **Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.**
- Membuat aplikasi 'mywatchlist' dengan menjalankan perintah *python manage.py startapp mywatchlist* di folder main pada cmd

- Route url dengan menambahkan *path('mywatchlist/', include('mywatchlist.urls'))* untuk menghubungkan urlpatterns yang ada pada project_django dengan mywatchlist

- Menambahkan *mywatchlist* pada installed_app di settings.py kemudian melakukan path route dalam mywatchlist/urls.py agar terhubung dengan function yang dijalankan pada mywatchlist/views.py

- Membuat model data pada mywatchlist/models.py dengan fields  *watched_film, title_film, rating_film = model, release_date, review_film*. 

- Migrasi dengan melakukan *python manage.py makemigrations* dan *python manage.py migrate*


### **Postman unit test --> respon HTTP 200 OK**

**HTML**
![pics](./html%20postman.png?raw=true)

**XML**
![pics](xml%20postman.png?raw=true)

**JSON**
![pics](json%20postman.png?raw=true)
