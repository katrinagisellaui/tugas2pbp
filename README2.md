# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

## 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!
![Bagan](user.jpg)

## 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan untuk memudahkan pengerjaan proyek Django, terutama jika proyek merupakan proyek berkelompok. Jika versi django yang digunakan oleh proyek berbeda dengan versi django yang ada di komputer kita, kita akan sangat kesulitan berkontribusi pada proyek. Namun, jika kita mengubah versi django kita untuk mengikuti versi django proyek, bisa saja ada proyek pribadi kita yang tidak dapat dikerjakan lagi karena mengikuti versi django kita yang lama. Maka dari itu, virtual environment digunakan untuk memudahkan pengerjaan berbagai proyek yang membutuhkan requirements yang berbeda-beda. Walaupun sebenarnya bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, kelebihan yang ditawarkan oleh kehadiran virtual environment menyebabkan tidak adanya alasan untuk tidak menggunakan virtual environment.

## 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Berikut adalah implementasi poin 1 sampai 4 yang saya lakukan dengan memanfaatkan source code yang disediakan

### 1. Membuat function show_katalog pada views.py. 
Pada fungsi ini, data_barang_katalog akan diisi oleh CatalogItem, yaitu semua barang yang ada pada katalog yang ingin kita tampilkan. 
Kode:
```
from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Katrina Gisella Sembiring',
        'npm':'2106707826'
    }
    return render(request, "katalog.html", context)
```

### 2. Mengimplementasi routing pada urls.py
Pertama, saya mengimplementasi routing pada urls.py yang berada pada file katalog.
Kode:
```
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```

Lalu, saya juga mengimplementasikan routing pada urls.py yang berada pada file project_django. 
kode:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
]
```

### 3. Pemetaan dan Migrasi
Selanjutnya, saya akan memetakan data yang sudah didapatkan ke HTML dengan sintaks dari Django untuk pemetaan data template. Untuk melakukan bagian ini, saya mengikuti perintah yang terdapat pada tutorial Lab 1. Saya melakukan python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal. Saya juga menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

### 4. Deployment ke Heroku
Karena file-file yang diperlukan untuk deployment sudah disediakan, maka saya hanya menambahkan secrets pada repository github saya dan melakukan add, push, dan commit. Setelah itu, aplikasi dapat langsung di deploy.






