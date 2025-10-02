from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Pemilik Produk", null=True)
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
    is_available = models.BooleanField(default=True, verbose_name="Ketersediaan Produk")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey', verbose_name="Kategori Produk")

    class Meta:
        verbose_name = "Produk"
        verbose_name_plural = "Produk"
        
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    persona = models.TextField()

class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    stock = models.IntegerField()