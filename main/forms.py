from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import Product, Car

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'thumbnail', 'is_featured', 'is_available', 'category']
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        return strip_tags(name)
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        return strip_tags(description)

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'stock']