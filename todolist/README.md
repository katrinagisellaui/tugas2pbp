# Tugas 4 PBP

Klik [disini](https://tugas2pbpkatalog.herokuapp.com/todolist/) untuk menuju aplikasi Heroku saya :D
Nama Akun 1: katrinagisella
Password 1: pbpkatrina
Nama Akun 2: katrinagisella2
Password 2: pbpgisella
### Apa kegunaan ```{% csrf_token %}``` pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Serangan CSRF (Cross-Site Request Forgery) merupakan serangan yang memaksa end-user untuk mengeksekusi action pada aplikasi web dimana seorang user sudah mengautentikasi dirinya. Attacker memanfaatkan keadaan dimana user sudah terautentikasi untuk mengubah request yang dikirim oleh user. Untuk menghindari serangan ini, Django memiliki tag {% csrf_token %}. {% csrf_token %} akan men-generate token pada server-side saat me-render halaman dan akan memeriksa kembali token ini untuk setiap request yang datang. Jika request tidak memiliki token ini, request tidak akan dieksekusi.

### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }}```)? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Kita bisa membuat elemen <form> secara manual tanpa menggunakan generator seperti {{ form.as_table }}.

Secara garis besar, kita akan membuat forms.py sebagai tempat kita membuat semua form. Syntax membuat form dalam forms.py adalah sebagai berikut
```
Field_name = forms.FieldType(attributes)
````
Lalu, untuk me-render forms.py ke dalam views, kita akan membuat views. Dalam views.py, kita akan membuat view yang kita butuhkan. Setelah itu, kita dapat menuju file html kita dan me-render semua field secara manual menggunakan template 
```
{{ form.non_field_errors }}
<div class="fieldWrapper">
    {{ form.subject.errors }}
    <label for="{{ form.subject.id_for_label }}">Email subject:</label>
    {{ form.subject }}
</div>
```

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Setelah user menekan tombol submit yang biasanya ada pada setiap html form, data akan dikumpulkan dan dikirim ke program lain untuk diproses. Element ```form``` memiliki dua atribut yang mengontrol aktivitas setelah form di-submit. Atribut yang pertama adalah atirbut ```action```, yang mengontrol ke program apa data akan dikirimkan (biasanya dalam bentuk URL). Atribut kedua adalah atribut ```method```, yang memiliki dua value, yaitu ```GET``` dan ```POST```. ```GET``` akan mengumpulkan data yang sudah dikumpulkan menjadi sebuah string, dan menggunakan string ini untuk membuat sebuah URL yang berisi informasi tentang alamat dimana data akan dikirimkan serta data keys dan values.  Jika login form di-return menggunakan ```POST```, browser akan mengumpulkan data, meng-encodenya untuk transmisi, mengirimkannya kepada server, dan menerima respons kembali.

###  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

* Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
Mengetikkan ```python manage.py startapp todolist``` pada terminal. 

* Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
Lalu, saya menambahkan aplikasi todolist pada URL patterns pada folder project_django sebagai berikut.
```
...
    path('todolist/', include('todolist.urls')),
...
```

* Membuat sebuah model Task yang memiliki atribut sebagai berikut: user, date, title, description

Lalu, saya membuat class Task pada models.py dengan atribut sesuai dengan ketentuan soal sebagai berikut.

```
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    date = models.DateField()
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default = False)
```

* Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.

Membuat function pada views.py untuk registrasi, login, dan logout yang bertujuan untuk mengambil data yang diperlukan dari user. Function register dan login akan me-return render menuju file html yang akan menampilkan data yang kita ambil tadi.

views.py.
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
```

login.html
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<body style="background-color:rgb(176, 181, 230);">

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

</div>

{% endblock content %}
```

register.html
```
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  
<body style="background-color:pink;">

<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

* Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
Pertama, saya membuat function pada views.py bernama show_todolist sebagai berikut. Function akan me-render todolist.html.
```
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todo = Task.objects.filter(user=request.user)
    context = {
        'list_todolist' : todo,
        'username' : request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)
```

Lalu, saya membuat todolist.html yang memuat semua ketentuan pada soal. File todolist.html saya sebagai berikut.
```
{% extends 'base.html' %}

 {% block content %}
  <body style="background-color:powderblue;">
  <h1>Tugas 4 Assignment PBP</h1>

  <h5>Username </h5>
  <p>{{username}}</p>
  <style>
    table, th, td {
        border: 1px solid black;
    }
    </style>

  <table>
    <tr>
      <th>User</th>
      <th>Date</th>
      <th>Title</th>
      <th>Description</th>
      <th>Is Finished?</th>
      <th>Change Finish </th>
      <th>Delete</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for task in list_todolist %}
        <tr>
            <th>{{task.user}}</th>
            <th>{{task.date}}</th>
            <th>{{task.title}}</th>
            <th>{{task.description}}</th>
            <th>
                {% if task.is_finished %}
                Selesai
                {% else %}
                Belum Selesai
                {% endif %}
            </th>
            <th>
            <button><a href="{% url 'todolist:change_done' task.id %}" title="">Change</a></button>
            </th>
            <th>
            <button><a href="{% url 'todolist:remove_task' task.id %}" title="">Remove</a></button>
            </th>
        </tr>
    {% endfor %}
  </table>
  <h5>Sesi terakhir login: {{ last_login }}</h5>
  <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
  <button><a href="{% url 'todolist:create_task' %}">Create Task</a></button>


 {% endblock content %}
 ```
 
* Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

Membuat class TodoList pada forms.py yang berisi atribut yang ingin saya simpan dari data user. 
```
from django import forms

class TodoList(forms.Form):
    title = forms.CharField(label = 'Judul Task', max_length = 250)
    description = forms.CharField(label = 'Deskripsi Task', max_length = 250)
```
Lalu, saya membuat function create_task yang akan me-render create_task.html
views.py
```
...
def create_task(request):
    form = TodoList()
    if request.method == 'POST':
        form  = TodoList(request.POST)
        if form.is_valid():
            new_form = Task()
            new_form.user = request.user
            new_form.date = datetime.datetime.now()
            new_form.title = form.cleaned_data['title']
            new_form.description = form.cleaned_data['description']

            new_form.save()
            return redirect('todolist:show_todolist')
        else:
            # messages.info(request, 'Input tidak valid!')
            form = TodoList()
    context = {'form':form}
    return render(request, 'create_task.html', context)
...
```

create_task.html
```
{% extends 'base.html' %}

{% block meta %}
<title>Create Task</title>
{% endblock meta %}

{% block content %}
<body style="background-color:rgb(178, 230, 176);">

<div class = "create_task">
    <h1>Create Task</h1>
        <form method="POST" action="">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
            </table>
            <input type ="submit" name="submit" value="Create Task">
        </form>
</div>
{% endblock content %}
```
* Membuat routing sehingga beberapa fungsi dapat diakses melalui URL sesuai dengan ketentuan soal.
Menambahkan kode berikut pada urls.py yang berada pada folder todolist.
```
rom django.urls import path
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import change_done
from todolist.views import remove_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('change-done/<int:id>', change_done, name='change_done'),
    path('remove-task/<int:id>', remove_task, name='remove_task')
]
```

* Melakukan deployment ke Heroku
Melakukan deployment ke Heroku sesuai dengan step pada Lab 0.


* Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

Saya membuat dua akun dummy dengan tiga dummy data.
![User 1](https://github.com/katrinagisellaui/tugas2pbp/blob/main/todolist/Screenshot%20Dummy/Screen%20Shot%202022-09-29%20at%2009.21.44.png)
![User 2](https://github.com/katrinagisellaui/tugas2pbp/blob/main/todolist/Screenshot%20Dummy/Screen%20Shot%202022-09-29%20at%2009.22.05.png)





### References
* https://www.educative.io/answers/what-is-a-csrf-token-in-django
* https://docs.djangoproject.com/en/4.1/topics/forms/
* https://statmath.wu.ac.at/courses/data-analysis/itdtHTML/node43.html 
* https://www.geeksforgeeks.org/render-django-form-fields-manually/ 



# Tugas 5 PBP

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
* Inline CSS adalah kode CSS yang dituliskan pada atribut elemen HTML secara langsung. Inline CSS berguna ketika memerlukan perubahan yang cepat, ingin menguji perubahan saja, atau proses permintaan HTTP lebih kecil. Namun, inline CSS tidak efisien karena hanya bisa diterapkan pada satu elemen HTML saja.
Contoh inline CSS:
```<h2 style="color:blue; font-family: arial;">Niagahoster</h2>```

* Internal CSS adalah kode CSS yang ditulis dalam tag <style>. Kode HTML ditulis pada bagian atas file HTML. Perubahan yang dibuat oleh internal CSS hanya berlaku pada satu halaman saja. HTML dan CSS juga berada pada satu file. Namun, internal CSS tidak efisien untuk jika ingin menggunakan CSS yang sama pada beberapa file dan performa website tidak begitu cepat.

* External CSS adalah kodes CSS yang tertulis terpisah dari kode HTML yang ditulis dalam file ```.css```. Dengan menggunakan external CSS, ukuran HTML akan lebih kecil dan struktur kode akan lebih rapi. Loading website juga akan menjadi lebih cepat. File CSS juga dapat digunakan di beberapa halaman website sekaligus. 

### Jelaskan tag HTML5 yang kamu ketahui.
* ```<abbr>```: penyingkatan kata atau frasa yang panjang
* ```<b>```: Membuat text menjadi bold
* ```<br>```: Membuat button
* ```<data>```: Me-link konten dengan terjemahan yang bisa dibaca mesin
* ```<form>```: Mendefinisikan form HTML untuk input user
* ```<html>```: Mendefinisikan root dokumen HTML
* ```<head>```: Mendefinisikan bagian atas (head) dari dokumen yang berisi informasi tentant hal-hal seperti title
dan lain-lain yang dapat dibaca [disini](https://www.tutorialrepublic.com/html-reference/html5-tags.php)

###  Jelaskan tipe-tipe CSS selector yang kamu ketahui.
* Selektor Tag: Disebut sebagai type selector. Selektor Tag akan memiliki elemen berdasarkan nama tag.
* Selektor Class: Selektor yang akan memiliki elemen berdasarkan nama class yang diberikan, ditandai dengan titik di depannya.
* Selektor ID: Mirip dengan selektor Class, tetapi hanya dapat digunakan oleh satu elemen saja (unik). Ditandai dengan tanda # didepannya.
* Selektor Atribut: Mirip dengan selektor Tag, selektor Atribut memiliki elemen berdasarkan atribut.
* Selektor Universal: Selektor yang digunakan untuk menyeleksi elemen pada scope tertentu
* Pseudo Selektor: Selektor untuk menyeleksi elemen-elemen semu seperti state dari suatu elemen, elemen before dan after, dsb. Terdapat 2 macam pseudo selektor, yaitu pseudo class selektor untuk state elemen dan pseudo-element selektor untuk elemen semu di HTML.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Memasukkan bootstrap ke dalam ```base.html```.
* Saya mengumbah forms.py saya ke dalam bentuk berikut
```
class TodoList(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Input Judul Task', 'class':'form-control mx-3 my-2'}),
            'description': forms.Textarea(attrs={'placeholder':'Input Judul Task', 'class':'form-control mx-3 my-2'})
        }
```

* Style halaman-halaman yang perlu di-style. Saya sudah mencoba menggunakan style.css, tetapi sayangnya belum berhasil. Untuk mengatasi itu, saya melakukan styling pada setiap .html.
* Menambahkan breakpoints yang berada pada Bootstrap untuk mengimplementasikan queries pada CSS. 

Referensi:
* https://www.petanikode.com/css-selektor/ 
* https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/ 
* https://www.tutorialrepublic.com/html-reference/html5-tags.php 
