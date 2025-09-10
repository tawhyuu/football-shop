Link aplikasi PWS: https://tangguh-ambha-footballshop.pbp.cs.ui.ac.id/
Nama Aplikasi: SoccaShop

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
   - Membuat sebuah proyek Django baru.
   1. Buka terminal pada direktori yang akan dijadikan tempat untuk pengembangan project
   2. Buat virtual environment dengan:
      - python -m venv env
        Kenapa pakai venv? untuk menghindari conflict. seperti contoh satu package memiliki 2 project
   3. Aktifkan venv dengan:
      - env\Scripts\activate
   4. Membuat file requirements.txt untuk kumpulan package yang akan di download diantaranya:
      - django
      - gunicorn
      - whitenoise
      - psycopg2-binary
      - requests
      - urllib3
      - python-dotenv
   5. Install semua package dengan:
      - pip install -r requirements.txt
   6. Buat project Django:
      - django-admin startproject football_shop

- Membuat aplikasi dengan nama main pada proyek tersebut

  1. Buat App dengan nama main, setelah berhasil membuat project baru dan melakukan konfigurasi
     - python manage.py startapp main .
       Aplikasi main akan menjadi aplikasi utama yang menangani homepage

- Melakukan routing pada proyek agar dapat menjalankan main.

  1. Tambahkan 'main' ke INSTALLED_APPS pada settings.py
  2. Buat file urls.py pada direktori main
  3. Hubungkan url proyek dengan url app main di urls.py proyek (bukan di direktori main) menggunakan include (import dari django.urls):
     - path('', include('main.urls')), # Include URL dari app main

- Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai beriku:

  - name sebagai nama item dengan tipe CharField
  - price sebagai harga item dengan tipe IntegerField
  - description sebagai deskripsi item dengan tipe TextField
  - thumbnail sebagai gambar item dengan tipe URLField
  - category sebagai kategori iteme dengan tipe CharField
  - is_featured sebagai status unggulan item dengan tipe BooleanField

  1.  Pergi ke models.py pada main dan buat class Product yang menerima parameter models.Model:
      from django.db import models
      import uuid

      class Product(models.Model):
      CATEGORY_CHOICES = [
      ('jersey', 'Jersey'),
      ('sepatu', 'Sepatu'),
      ('bola', 'Bola'),
      ('aksesoris', 'Aksesoris'),
      ('celana', 'Celana'),
      ]
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID Produk")
      name = models.CharField(max_length=100, verbose_name="Nama Produk")
      price = models.IntegerField(verbose_name="Harga Produk")
      description = models.TextField(verbose_name="Deskripsi Produk")
      thumbnail = models.URLField(verbose_name="URL Thumbnail Produk")
      is_featured = models.BooleanField(default=False, verbose_name="Produk Unggulan")
      category = models.CharField(max_length=20, verbose_name="Kategori Produk")

          class Meta:
              verbose_name = "Produk"
              verbose_name_plural = "Produk"
              ordering = ['-created_at']

          def __str__(self):
              return self.name

  2.  Buat dan Jalankan Migrasi dengan python manage.py makemigrations, kemudian python manage.py migrate

  Migrasi ini berfungsi untuk mengaplikasikan perubahan model dalam berkas migrasi ke basis data

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan halaman utama

  1. Saya membuat fungsi show_main(request) yang menerima request sebagai parameter.
     def show_main(request):
     context = {
     'category' : 'jersey',
     'name' : 'Jersey Custom',
     'price' : 150000,
     'description' : 'Jersey Custom Nama dan Nomor Punggung. Terbuat dari bahan berkualitas tinggi dengan teknologi dry-fit untuk kenyamanan maksimal.',
     'thumbnail' : 'https://5.imimg.com/data5/SELLER/Default/2024/3/404714376/NM/AG/BO/14081053/football-uniforms.jpg',
     'is_featured' : True,
     }
     return render(request, 'main.html', context)

  2. Fungi show_main ini nantinya akan menghandle request dan menampilkan context ke main.html (template yang sblumnya dibuat)

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py

  1. from . import views (Mengimport views dari direktori yang sama)
  2. Menambahkan urlpatterns = [
     path('', views.show_main, name='show_main')
     ]

- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui internet.
  1. Menambahkan "https://tangguh-ambha-footballshop" ke ALLOWED_HOST pada setting.py.
  2. Push code ke pws master
  3. Jika merupakan pertama kali push PWS akan meminta username dan password untuk melanjutkan.
  4. View Project untuk melihat hasilnya

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis django beserta responnya dan jelaskan pada bagan tersebut
   ![Alur Django](https://drive.google.com/uc?export=view&id=1slTc7Tk7jXhsCYAnfPKQhrypHJPmef6h)
   Penjelasan Alur:

   1. Browser mengirim request ke URL tertentu
   2. urls.py memetakan URL ke view function yang sesuai

   - Django mencari pattern URL yang cocok dari atas ke bawah

   - URL cocok dengan path('', include('main.urls'))

   - Django lanjut cek di main/urls.py

   - Django menemukan path('', views.show_main, name='show_main')

   - Django memanggil function show_main di main/views

   3. views.py memproses request dan query data dari models jika diperlukan
   4. models.py berinteraksi dengan database untuk mengambil/menyimpan data
   5. views.py menggabungkan data dengan template HTML
   6. Template HTML dirender dan dikirim kembali sebagai response ke browser

   ### Kaitan antar komponen:

   - urls.py - Sebagai router yang menentukan view mana yang akan menangani request
   - views.py - Sebagai controller yang mengatur logic dan menghubungkan model dengan template
   - models.py - Representasi data dan business logic untuk database
   - HTML template - Layer presentasi yang menampilkan data ke user

3. Jelaskan peran settings.py
   settings.py adalah file **konfigurasi utama** yang mengatur seluruh aspek app django. Semua aturan utama proyek didapatkan dan dibuat di settings.py.

4. Bagaimana cara kerja migrasi database di Django?
   python manage.py makemigrations disini django akan membandingkan model saat ini dengan migration terakhir. Jika terdapat perubahan maka django akan membuat file migration yang berisi perubahan. python manage.py migrate artinya django membaca file migration yang belom di jalankan. Mungkin sistemnya seperti pull pada git. Migration yang sudah dijalankan akan dicatat di table django_migrations.

5. Mengapa framework Django dijadikan permulaan pembelajaraan pengembangan perangkat lunak?
   Menurut saya dan penjelasan yang saya tangkap dari pembelajaran PBP. Kita tidak menggunakan PHP karena PHP jika tidak disanitasi akan berbahaya. Sedangkan Django memiliki validasi input sehingga lebih aman. Kemudian django memiliki struktur arsitektur yang jelas (Model - View - Template) sehingga mudah dipahami dan diorganisir.

6. Feedback untuk asisten dosen tutorial 1
   Semua penjelasan tutorial 1 sudah cukup jelas sehingga tugas saya lancar. tetapi mungkin ada beberapa typo seperti urls pada football-news. Saya kira ini di direktori yang sejajar dengan manage.py ternyata yang dimaksud football_news.
