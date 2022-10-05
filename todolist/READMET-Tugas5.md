# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

[Link Heroku Munifah Nurfadhilah - 2106654851](http://tugas2pudil.herokuapp.com/todolist/)

### *Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?*
- Inline CSS --> Kode CSS yang ditulis langsung pada atribut elemen HTML. Kelebihan inline CSS yaitu, proses request HTTP lebih kecil sehingga proses load website akan lebih cepat, dapat memperbaiki kode dengan cepat, dan membantu ketika developer ingin menguji perubahan pada satu elemen. Kekurangan inline CSS yaitu, tidak efisien karena inline CSS hanya dapat diterapkan pada satu elemen HTML.

- Internal CSS --> Kode CSS yang di dalam tag *style* dan kode HTML ditulis di header file HTML. Internal CSS cocok untuk membuat tampilan unik pada setiap page website karena memiliki tampilan yang berbeda-beda. Kelebihan internal CSS yaitu, tidak perlu upload beberapa file karena HTML dan CSS berada di dalam satu file dan perubahan pada internal CSS berlaku pada satu halaman saja. Kekurangan internal CSS yaitu. membuat performa website lebih lambat karena CSS yang berbeda-beda pada setiap halaman akan membuat loading ulang setiap user mengganti halaman website.

- Eksternal CSS --> Kode CSS yang ditulis terpisah dengan kode HTML. Eksternal CSS ditulis di file khusus (.css) dan diletakkan setelah bagian *head* halaman. Kelebihan external CSS yaitu, ukuran file HTML lebih kecil, struktur kode HTML lebih rapih, loading website lebih cepat, dan file CSS dapat digunakan di beberapa halaman sekaligus. Kekurangan eksternal CSS yaitu, halaman bisa saja berantakan akibat file CSS gagal dipanggil oleh file HTML. Biasanya kegagalan tersebut disebabkan oleh koneksi internet yang kurang bagus.

### *Jelaskan tag HTML5 yang kamu ketahui.*
- `<p>` --> tag merepresentasikan paragraf
- `<div>` --> tag merepresentasikan section/container
- `<link>` --> tag menginclude path/link 
- `<title>` --> tag mengatur title tab browser
- `<a>` --> tag menambah link pada dokumen
- `<body>` --> tag mendefinisikan body dokumen
- `<head>` --> tag mendefinisikan head dokumen, bisa berisi title
- `<h1>` to `<h6>` --> tag mendefinisikan html headings

### *Jelaskan tipe-tipe CSS selector yang kamu ketahui.*
- selector tag `<p>` --> selector ini akan memilih elemen berdasarkan nama tag untuk menambahkan style. misalnya `div {`
- selector class --> selector ini akan memilih elemen berdasarkan nama class yang diberikan untuk menambahkan style. selector class dibuat dengan tanda titik di depannya.
- selector id --> selector ini mirip dengan selector class, tetapi id bersifat unik sehingga dapat digunakan oleh satu elemen saja untuk menambahkan style. selector ini ditandai dengan `#` di depannya. 
- selector atribut --> selector ini mirip dengan selector tag, tetapi selector akan memilih elemen berdasarkan atribut untuk menambahkan style. 
- selector universal --> selector ini digunakan untuk menyeleksi semua elemen pada scope tertentu. selector ini biasanya digunakan untuk me-reset CSS. 
- selector pseudo --> selector ini akan memilih elemen semu seperti state pada elemen, elemen befor dan after, elemen ganjil, etc. terdapat dua macam selector pseudo, yaitu pseudo-class dan pseudo-element. 

### *Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.*
- pertama, saya melakukan import bootstrap pada setiap halaman html yang ingin dikostumisasi https://getbootstrap.com/docs/5.2/getting-started/introduction/
- kedua, saya melakukan kostumisasi pada halaman login, resgister, dan create_task dengan mengubah font, menambah emojis, dan memasukkan elemen tersebut ke dalam cards https://getbootstrap.com/docs/5.2/components/card/ 
- ketiga, saya melakukan kostumisasi pada halaman todolist.setiap task saya masukkan ke dalam cards beserta dengan elemen yang sebelumnya telah dibuat pada tugas 4. 
- keempat, seluruh halaman tersebut saya cek apakah sudah responsive atau belum, dengan me-inspect pada website
- kelima, saya mengerjakan bonus dengan membuat folder css pada tugas2/static dan membuat file style.css dalam folder tersebut. di dalam file saya mengisi kode css agar terdapat efek saat di hover ke cards. efek hover ini berlaku pada seluruh class cards yang ada di html.