Link aplikasi PWS: https://tangguh-ambha-footballshop.pbp.cs.ui.ac.id/
Nama Aplikasi: SoccaShop

## Dokumentasi Tugas

- [Tugas 2](../../wiki/Tugas-2-PBP-2025-2026)
- [Tugas 3](../../wiki/TUgas-3-PBP-2025-2026)
- [Tugas 4](../../wiki/Tugas-4-PBP-2025-2026)
- [Tugas 5](../../wiki/Tugas-5-PBP-2025-2026)

## Tugas 6

### 1. Apa perbedaan antara synchronous request dan asynchronous request?

**Synchronous Request:**

- Eksekusi kode berjalan secara berurutan (sequential)
- Browser menunggu response dari server sebelum melanjutkan eksekusi kode berikutnya
- Halaman web akan "freeze" atau tidak responsif selama menunggu response
- User tidak bisa melakukan interaksi lain sampai request selesai
- Contoh: Form submission biasa yang menyebabkan page reload

**Asynchronous Request:**

- Eksekusi kode tidak menunggu response dari server
- Browser dapat melanjutkan eksekusi kode lain sambil menunggu response
- Halaman web tetap responsif dan user bisa melakukan interaksi lain
- Response ditangani melalui callback, promise, atau async/await
- Contoh: AJAX request, fetch API

Synchronous seperti antri di kasir, harus menunggu orang di depan selesai baru bisa dilayani, sedangkan Asynchronous seperti pesan makanan di restoran, kita bisa ngobrol atau main HP sambil menunggu pesanan datang

### 2. Bagaimana AJAX bekerja di Django (alur request–response)?

Berikut adalah alur lengkap AJAX di Django:

1. User Interaction (Frontend)
2. JavaScript Event Trigger
3. AJAX Request dibuat menggunakan fetch() atau XMLHttpRequest
4. Request dikirim ke Django URL endpoint
5. Django URL Router mencocokkan URL dengan view
6. Django View menerima request
7. View memproses data (CRUD operations, validasi, etc)
8. View mengembalikan response dalam format JSON
9. JavaScript menerima response
10. Callback/Promise handler memproses response
11. DOM diupdate secara dinamis (tanpa page reload)
12. UI menampilkan perubahan ke user

### 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

**Keuntungan AJAX:**

1. **User Experience (UX) Lebih Baik**

   - Tidak ada page reload yang mengganggu
   - Interaksi terasa lebih cepat dan smooth
   - Loading hanya pada bagian yang diperlukan

2. **Performance Lebih Efisien**

   - Hanya data yang diperlukan yang ditransfer (JSON format)
   - Bandwidth lebih hemat dibanding full HTML
   - Server hanya perlu mengirim data, bukan template lengkap

3. **Interaktivitas Tinggi**

   - Real-time updates tanpa mengganggu user
   - Multiple requests bisa berjalan bersamaan
   - State aplikasi tetap terjaga (scroll position, form input, dll)

4. **Separation of Concerns**

   - Backend fokus pada data (API)
   - Frontend fokus pada presentation
   - Lebih mudah untuk maintenance dan testing

5. **Mobile-Friendly**
   - API yang sama bisa digunakan untuk web dan mobile app
   - Data format JSON mudah diparse di berbagai platform

### 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

- Menggunakan HTTPS untuk mencegah man-in-the-middle attack
- Menggunakan CSRF token saat melakukan request
- Menambahkan validasi input pada sisi server (bukan hanya di client side saja)
- Menggunakan response JSON, bukan HTML render

### 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

## Implementasi Checklist Tugas 6

## Perubahan pada File

### 1. **forms.py**

**Perubahan:**

- Menambahkan import `strip_tags` dari `django.utils.html`
- Menambahkan method `clean_name()` untuk sanitize input name
- Menambahkan method `clean_description()` untuk sanitize input description

### 2. **views.py**

**Perubahan:**

- Menambahkan import `JsonResponse`, `csrf_exempt`, `require_POST`, dan `json`
- Menambahkan 3 function baru untuk AJAX CRUD:
  - `add_product_ajax()` - Handle create product via AJAX
  - `edit_product_ajax()` - Handle update product via AJAX
  - `delete_product_ajax()` - Handle delete product via AJAX
- Mengubah `show_json()` untuk return `JsonResponse` dengan safe=False dan support filter
- Mengubah `show_json_by_id()` untuk return `JsonResponse` dengan safe=False
- Mengubah `show_main()` untuk tidak pass product_list ke context (akan diload via AJAX)
- Mengubah `register()` untuk support AJAX request
- Mengubah `login_user()` untuk support AJAX request dengan header check

### 3. **urls.py**

**Perubahan:**

- Menambahkan 3 URL pattern baru untuk AJAX endpoints:
  ```python
  path('add-product-ajax/', views.add_product_ajax, name='add_product_ajax'),
  path('edit-product-ajax/<uuid:id>/', views.edit_product_ajax, name='edit_product_ajax'),
  path('delete-product-ajax/<uuid:id>/', views.delete_product_ajax, name='delete_product_ajax'),
  ```

### 4. **base.html**

**Perubahan:**

- Menambahkan DOMPurify CDN script
  ```html
  <script src="https://cdn.jsdelivr.net/npm/dompurify@3.0.5/dist/purify.min.js"></script>
  ```
- Menambahkan toast.js script
  ```html
  <script src="{% static 'js/toast.js' %}"></script>
  ```
- Menambahkan include untuk toast.html
  ```html
  {% include 'toast.html' %}
  ```

### 5. **toast.js (File Baru)**

**Lokasi:** `static/js/toast.js`

**Fitur:**

- Function `showToast(title, message, type, duration)`
- Support 4 types: success, error, warning, normal

### 6. **toast.html (File Baru)**

**Lokasi:** `templates/toast.html`

### 7. **main.html**

**Perubahan:**

1. Filter Section Diubah dari Link ke Button:
2. Menambahkan Refresh Button
3. Menambahkan Add Product Button (buka modal, bukan redirect)
4. Menambahkan 3 States:

   - Loading State (spinner animation)
   - Empty State (no products message)
   - Error State (error message dengan retry button)

5. Product List Container
6. Menambahkan Modal untuk Add/Edit Product:

   - Form dengan semua field product
   - Validation
   - Cancel dan Save button

7. Menambahkan Delete Confirmation Modal

   - Warning message
   - Cancel dan Delete button

8. **JavaScript Functions:**

   ```javascript
   - filterProducts(filter) - Filter all/my products
   - refreshProducts() - Fetch dan display products
   - displayProducts(products) - Render products ke DOM
   - createProductCard(product) - Generate HTML untuk card
   - showAddModal() - Open modal untuk create
   - showEditModal(productId) - Open modal untuk edit
   - closeModal() - Close product modal
   - showDeleteModal(productId) - Open delete confirmation
   - confirmDelete() - Execute delete via AJAX
   ```

### 8. **login.html**

**Perubahan:**

- Menghapus form errors display (sudah tidak perlu)
- Menambahkan AJAX form submission

### 9. **register.html**

**Perubahan:**

- Menambahkan error message placeholders untuk setiap field
- Menambahkan AJAX form submission

### 10. **navbar.html**

**Perubahan:**

1. Desktop Logout → AJAX
2. Mobile Logout → AJAX
3. Menambahkan handleLogout() Function
