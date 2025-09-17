Link aplikasi PWS: https://tangguh-ambha-footballshop.pbp.cs.ui.ac.id/
Nama Aplikasi: SoccaShop

## Tugas 3 PBP

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan agar platform bisa **bertukar data antar komponen atau layanan**. Dengan adanya data delivery, aplikasi front-end bisa menampilkan informasi dari back-end, dan aplikasi lain bisa mengkonsumsi data dari API. Tanpa data delivery, sistem akan terisolasi dan tidak bisa berkomunikasi dengan sistem lain.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

- **JSON** lebih baik untuk pertukaran data modern karena:
  - Lebih **ringkas** dan lebih readable.
  - Didukung langsung oleh **JavaScript** dan banyak bahasa pemrograman lain.
  - Parsing lebih cepat.
- Tetapi **XML** masih digunakan dalam beberapa sistem lama karena memiliki struktur **tag** yang kuat dan dukungan untuk **metadata** (attributes, namespace).
- JSON lebih populer karena lebih **sederhana, efisien, dan langsung terintegrasi** dengan ekosistem web.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

- Fungsi `is_valid()` digunakan untuk **validasi input form**.
- Django akan memeriksa apakah semua field diisi sesuai aturan (misalnya: tipe data benar, panjang karakter sesuai).
- Jika valid → mengembalikan `True`, dan data bisa diakses melalui `cleaned_data`.
- Jika tidak valid → mengembalikan `False`, serta menghasilkan pesan error.

Tanpa `is_valid()`, aplikasi bisa menerima input yang salah atau berbahaya.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

- `csrf_token` digunakan untuk mencegah **Cross-Site Request Forgery (CSRF)**.
- Jika tidak ada token, form bisa di-submit oleh pihak ketiga (penyerang) tanpa sepengetahuan pengguna.
- Penyerang bisa memanfaatkan ini untuk:
  - Mengirim permintaan palsu dengan kredensial pengguna.
  - Melakukan transaksi atau perubahan data yang tidak sah.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

#### 1. Membuat 4 Fungsi Views Baru untuk JSON dan XML (by ID dan all)

1. Buka `views.py` pada app utama.
2. Import `HttpResponse` dan `serializers`:

   ```python
   from django.http import HttpResponse
   from django.core import serializers
   from .models import Product
   ```

3. Tambahkan fungsi untuk menampilkan semua data dalam format **XML**:

   ```python
   def show_xml(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```

4. Tambahkan fungsi untuk menampilkan semua data dalam format **JSON**:

   ```python
   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

5. Tambahkan fungsi untuk menampilkan data **berdasarkan ID dalam format XML**:

   ```python
   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```

6. Tambahkan fungsi untuk menampilkan data **berdasarkan ID dalam format JSON**:

   ```python
   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

---

#### 2. Membuat Routing URL untuk Setiap Views

1. Buka `urls.py` pada app.
2. Tambahkan import views dan path URL:

   ```python
   from django.urls import path
   from .views import show_xml, show_json, show_xml_by_id, show_json_by_id

   urlpatterns = [
      ...
       path('xml/', show_xml, name='show_xml'),
       path('json/', show_json, name='show_json'),
       path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
       path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
       ...
   ]
   ```

---

#### 3. Membuat Halaman Utama untuk Daftar Objek

1. Mengedit `main.html` yang sebelumnya hanya untuk satu objek sekarang untuk semua produk.
2. Gunakan loop untuk menampilkan produk, dengan tombol **Add** dan **Detail**:

   ```html
   {% for product in products %}
   <h3>{{ product.name }}</h3>
   <p>{{ product.price }}</p>
   <a href="{% url 'add_product' %}">Add</a>
   <a href="{% url 'detail_product' product.id %}">Detail</a>
   {% endfor %}
   ```

---

#### 4. Membuat Halaman Form untuk Menambahkan Objek

1. Buat file `forms.py` dan tambahkan `ModelForm`:

   ```python
   from django import forms
   from .models import Product

   class ProductForm(forms.ModelForm):
       class Meta:
           model = Product
           fields = ['name', 'price', 'description', 'thumbnail', 'is_featured', 'is_available', 'category']
   ```

2. Buat template `create_product` di direktori templates untuk menampilkan form penambahan produk
3. Tambahkan fungsi `create_product` di `views.py` untuk menampilkan dan memproses form.
   Jika form valid, data disimpan ke database.
4. Membuat routing url di urlpatterns

---

#### 5. Membuat Halaman Detail untuk Setiap Objek

1. Tambahkan fungsi `show_product` di `views.py` dengan parameter `id` untuk mengambil satu produk.
2. Buat template `product_detail.html` untuk menampilkan detail produk.
3. Membuat routing url di urlpatterns

---

#### 6. Mengakses URL dengan Postman

1. Buka Postman.
2. Akses URL berikut:

   - `http://localhost:8000/json/`
   - `http://localhost:8000/xml/`
   - `http://localhost:8000/json/<id>`
   - `http://localhost:8000/xml/<id>`

3. Ambil screenshot hasil respon.
4. Tambahkan screenshot ke dokumentasi README/Wiki.

---

#### 6. Apakah ada feedback untuk asdos di tutorial 2?

Sangat aman kak untuk tutorial 2 ini. Semua penjelasannya sudah jelas dan mudah dipahami

### 6. Bukti Screenshoot Postman

![Screenshot](https://drive.google.com/uc?export=view&id=1JY0mt8bOKtiulbmig86ig470A6QPlE2D)
![Screenshot](https://drive.google.com/uc?export=view&id=14t7txIn_8qsMWuVrTxn7nyTKIp3dUoou)
![Screenshot](https://drive.google.com/uc?export=view&id=1tq2KTHTOjPLpwlXVti_hlRrKDkTXmFj6)
![Screenshot](https://drive.google.com/uc?export=view&id=1J8HrYr9RCiFaNDs2fZY1wJqdu7nOPSp0)
