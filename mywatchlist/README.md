# My Watchlist


Klik [disini](https://tugas2pbpkatalog.herokuapp.com/mywatchlist/) untuk menuju aplikasi Heroku saya :D

## Jelaskan perbedaan antara JSON, XML, dan HTML!
### JSON
JSON merupakan bahasa yang biasa digunakan untuk penyimpanan dan transfer data. JSON sendiri memiliki fleksibilitas yang lebih tinggi dari HTML, tetapi JSON lebih sulit untuk dipelajari. JSON merupakan cara untuk merepresentasikan objek.

### HTML
HTML merupakan bahasa untuk menciptakan struktur dan konten laman web. HTML merupakan bahasa yang banyak diketahui. HTML juga mudah dimengerti dan relatif lebih mudah dipelajari, walaupun terdapat beberapa limitasi tentang hal yang bisa dilakukan dengan HTML.

### XML
XML merupakan bahasa yang didesain untuk meng-carry data dan bukan untuk menampilkannya. XML merupakan bahasa yang menyediakan encoding yang dapat dicaba oleh manusia dan oleh komputer.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Saat kita membangun sebuah platform, pasti terdapat data yang ingin kita sampaikan ke user atau data yang kita harapkan dapat diberikan oleh user kepada kita. Adanya kebutuhan untuk bertukar informasi ini lah yang biasanya mendorong agar platform diciptakan. Karena tujuan dibangunnya platform adalah untuk bertukar informasi antara server dan user, pastilah data delivery penting dalam pengimplementasian sebuah platform.

## Implementasi

### Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
Saya membuat aplikasi dengan perintah berikut.
```
python manage.py startapp mywatchlist
```

### Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
Menambahkan path
```
...
path('mywatchlist/', include('mywatchlist.urls')),
...
```
pada urls.py dalam folder project_django.

### Membuat sebuah model MyWatchList yang memiliki atribut watched, title, rating, release date, dan review
Saya membuat class MyWatchList pada models.py dengan isi sebagai berikut
```
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
```
untuk mengimplementasikan step ini. Setelah itu, menjalankan 
```
python manage.py makemigrations
```
dan
```
python manage.py migrate
```

### Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format HTML, XML, dan JSON
Saya membuat function pada views.py dan juga menambahkan
```
...
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('', show_mainpage, name='show_mainpage'),
...
```
pada urls.py untuk mengimplementasikan step ini.

### Melakukan deployment ke Heroku

## Postman
### HTML
![HTML](https://github.com/katrinagisellaui/tugas2pbp/blob/main/mywatchlist/Postman/Screen%20Shot%202022-09-22%20at%2000.42.02.png)

### XML
![XML](https://github.com/katrinagisellaui/tugas2pbp/blob/main/mywatchlist/Postman/Screen%20Shot%202022-09-22%20at%2000.42.15.png)

### JSON
![JSON](https://github.com/katrinagisellaui/tugas2pbp/blob/main/mywatchlist/Postman/Screen%20Shot%202022-09-22%20at%2000.43.04.png)