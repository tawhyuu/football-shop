from django.db import models
import uuid
# Create your models here.
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