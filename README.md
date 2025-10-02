Link aplikasi PWS: https://tangguh-ambha-footballshop.pbp.cs.ui.ac.id/
Nama Aplikasi: SoccaShop

## Dokumentasi Tugas

- [Tugas 2](../../wiki/Tugas-2-PBP-2025-2026)
- [Tugas 3](../../wiki/TUgas-3-PBP-2025-2026)
- [Tugas 4](../../wiki/Tugas-4-PBP-2025-2026)

## Tugas 5

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutannya:

- Inline style (langsung di elemen HTML) paling tinggi.
- Internal Style Sheet atau External.
- Browser default.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design bikin tampilan web tetap nyaman di berbagai ukuran layar (HP, tablet, laptop). Kalau nggak responsive, web bisa kelihatan berantakan di HP—tombol kepotong, teks susah dibaca.

Contoh aplikasi yang sudah responsive: Instagram, Tokopedia (tampilan tetap rapi di HP). Contoh yang belum: Website jadul yang kalau dibuka di HP harus di-zoom dan geser-geser.

Kenapa penting? Karena sekarang banyak orang akses web lewat HP, jadi harus ramah di semua device.

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal ini

- Margin: Jarak di luar border elemen, buat ngatur spasi antar elemen.
- Border: Garis di sekeliling elemen.
- Padding: Jarak antara isi elemen dan bordernya.
  Intinya Margin yang mengatur jarak antara border ke elemen lainnya, sedangkan padding adalah jarak isi content terhadap border

Untuk contoh implementasinya pada file css:
.card {
margin: 20px; /_ jarak antar card _/
border: 2px solid #333; /_ garis di sekeliling card _/
padding: 10px; /_ jarak isi card ke border _/
}

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox (Flexible Box) cocok digunakan saat ingin membuat barisan elemen yang fleksibel, misalnya deretan kartu produk yang otomatis rapi walaupun jumlahnya berubah-ubah. Dengan flexbox, kita bisa dengan mudah mengatur arah (horizontal/vertikal), jarak antar elemen, dan bagaimana elemen-elemen tersebut membesar atau mengecil mengikuti ukuran layar.

Sementara itu, grid layout lebih powerful untuk membuat desain yang kompleks, seperti membagi halaman menjadi beberapa kolom dan baris sekaligus. Grid memungkinkan kita menentukan area tertentu untuk elemen, sehingga cocok untuk layout seperti dashboard atau galeri foto yang butuh struktur lebih teratur. Intinya, flexbox lebih pas untuk tata letak satu dimensi (baris atau kolom), sedangkan grid layout untuk dua dimensi (baris dan kolom sekaligus). Keduanya sangat membantu agar tampilan web tetap rapi dan responsif di berbagai ukuran layar.

### Jelaskan cara kamu mengimplementasikan checklist di atas secara step-by-step

#### 1. Implementasikan fungsi untuk menghapus dan mengedit product]

1. Membuat 2 function baru di views.py, yaitu edit_product dan delete_product.
2. Buat URL untuk edit dan delete
3. Buat template untuk edit_product
4. Pada main.html tambahkan tombol edit dan delete ketika user == product.user

#### 2. Kustomisasi desain pada template HTML yangtelah dibuat pada tugas sebelumnya menggunakan CSS atau CSS framework

1. Buka Figma dan mulai mendesign WebPagenya seperti apa
   1.1 Menentukan dulu color palet dan typograph nya
   1.2 Buat beberapa component seperti Button, Button Hover, Card Product, Card Product Hover, dll
   1.3 Membuat Logo di Canva dan import ke Figma
   1.4 Rangkai menjadi home page yang indah
   [Desain Figma](./assets/img/Desain%20Figma.png)
2. Setelah sudah jadi export code ke dalam bentuk CSS + HTML dengan plugins yang sudah disediakan Figma
3. Ubah menjadi tailwind CSS dengan styling inline
