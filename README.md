Link aplikasi PWS: https://tangguh-ambha-footballshop.pbp.cs.ui.ac.id/
Nama Aplikasi: SoccaShop

## Dokumentasi Tugas

- [Tugas 2](../../wiki/Tugas-2-PBP-2025-2026)
- [Tugas 3](../../wiki/TUgas-3-PBP-2025-2026)

## Tugas 4

### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya

Django AuthenticationForm adalah Form login bawaan Django yang menyediakan interface standar untuk pengguna login. Apa kelebihannya? efisien baris dalam coding, karena sudah dibuatkan oleh Django beserta validasi inputnya tidak perlu ngoding dari awal, tidak perlu memikirkan apakah password yang dimasukkan tersimpan aman. Kekurangannya? Formulir ini memberikan formulir standar beruba username dan password sehingga perlu dilakukan modifikasi jika perlu formulir kustom.

### Apa perbedaan antara autentikasi dan otorisasi? Bagaimana DJango mengimplementasikan kedua konsep tersebut?

Autentikasi adalah proses memverifikasi siapa yang sedang mengakses simplenya adalah login. Sedangkan Authorization adalah proses memverifikasi akses yang dimiliki pengakses, seperti ada pembagian akses yang hanya dimiliki oleh pengguna tertentu. Dalam pengaplikasiannya Django memiliki decorator "login_required" dan "permission_required" yang menandakan bahwa function tersebut dapat diakses dengan authentication dan authorization

### Apa saja kelebihan dan kekurangan session dan cookies dalam konsteks menyimpan state di aplikasi web?

Kelebihan Session:

1. Lebih aman, session bisa diibaratkan seperti "loker" yang ketika kita simpan data kita hanya mendapat nomor loker (session ID).
2. Bisa menyimpan data yang cukup banyak karena server session memiliki banyak "loker"

Kekurangan Session:

1. Beban server yang lebih berat, karena semua "loker" ada di server, kalau ada ribuan pengguna menyimpan data di "loker" maka server bisa kecapean.
2. Ketika log out, data-data akan langsung hilang tidak bisa di akses lagi

Kelebihan Cookies:

1. Data yang disimpan di cookies mudah untuk diakses, seperti saat login line ada centang "Remember me"
2. Bisa disimpan dalam jangka waktu yang lama
3. Tersimpan di browser, sehingga tidak membebani server

Kekurangan Cookies:

1. Cookies memiliki kapasitas kecil untuk menyimpan data, tidak bisa lebih dari 4KB
2. Data yang disimpan di cookies lebih mudah diakses sehingga kurang aman

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

By default cookies tidak aman. Ada resiko Cookies bocor saat lintas domain, karena Cookies dikirim otomatis oleh browser setiap kali request ke domain itu. Kalau ada web yang bisa mengarahkan user buat request ke server, cookies tetap ikut terkirim, ini resikonya CSRF. Masih banyak resiko lainnya. Tetapi django memiliki CSRF protection built in yang berfungsi melindungi form "POST", ketika ada request palsu akan ditolak

### Jelaskan bagaimana car akamu mengimplementasikan checklist diatas secara step-by-step

#### 1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.

1. Membuat fungsi login_user, register, dan logout_user di views.py. nama funcionnya kalau bisa jangan login dan logout karena nanti akan memanggil fungsi itu sendiri dan bukan fungsi bawaan django.
2. Membuat template login dan register dan menambahkan routing untuk function ini
   2.1 login_user akan merender AuthenticationForm ke login.html
   2.2 register akan merender UserCreationForm ke register.html
3. Setelah tambahkan decorator "@login_required" pada function yang menghandle homepage, untuk kasus ini adalah function show_main. Tambahkan parameter login_url untuk kasus ini adalah login/
4. runserver dan coba akses homepage akan menampilkan page login (/login/) karena belum melakukan login.

##### 2. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.

1. Lakukan register dan login untuk setiap akun
2. Tambahkan 3 Produk untuk masing - masing akun

#### 3. Menghubungkan model Product dengan User.

1. Tambahakan kode berikut pada model untuk mengaitkan product dengan user

```python
user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Pemilik Produk", null=True)
```

2. Ketika on_delete=models.CASCADE maka model lama tidak akan dihapus.
3. Ubah detail_product.html menambahkan pemilik produk tersebut dengan

```python
{% if product.user %}
<p>Author: {{ product.user.username }}</p>
{% else %}
<p>Author: Anonymous</p>
{% endif %}
```

4. Nantinya 3 product yang ditambahkan untuk setiap akun akan menampilkan anonymouse karena product.user.username mengembalikan NONE

#### 4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi

1. Mengedit main.html dengan mengganti

```python
owner : <h5>Owner: {{ name }}</h5>
```

2. mengedit show_main di views.py untuk mengakses nama user yang sedang login

```python
context = {
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login'),
        'product_list': product_list,
    }
```

3. Menambahkan set_cookies untuk last login pada fungsi login_user pada views.py
   kemudian menambahkan delete_cookies pada logout.
