from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm, CarForm
from main.models import Product, Employee
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import datetime
import json

# Create your views here.
@login_required(login_url='login/')
def show_main(request):
    context = {
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, 'main.html', context)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    try:
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        thumbnail = request.POST.get('thumbnail')
        is_featured = request.POST.get('is_featured') == 'true'
        is_available = request.POST.get('is_available') == 'true'
        category = request.POST.get('category')
        
        product = Product.objects.create(
            user=request.user,
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            is_featured=is_featured,
            is_available=is_available,
            category=category
        )
        
        return JsonResponse({
            'status': 'success',
            'message': 'Product created successfully',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'description': product.description
            }
        }, status=201)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        
        product.name = request.POST.get('name', product.name)
        product.price = request.POST.get('price', product.price)
        product.description = request.POST.get('description', product.description)
        product.thumbnail = request.POST.get('thumbnail', product.thumbnail)
        product.is_featured = request.POST.get('is_featured') == 'true'
        product.is_available = request.POST.get('is_available') == 'true'
        product.category = request.POST.get('category', product.category)
        product.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Product updated successfully'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        product.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Product deleted successfully'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form,}
    return render(request, "create_product.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form,}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse("main:show_main"))

def add_employee(request):
    employee = Employee.objects.create(name = 'Daniel', age = 20, persona = 'baik banget buat challenge')
    context = {
        'name' : employee.name,
        'age' : employee.age,
        'persona' : employee.persona,
    }
    return render(request, "employee.html", context)

def create_car(request):
    form = CarForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form,}
    return render(request, "create_car.html", context)

@login_required(login_url='login/')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize('xml', product_list)
    return HttpResponse(xml_data, content_type='application/xml')

def show_json(request):
    filter_type = request.GET.get('filter', 'all')
    if filter_type == 'my' and request.user.is_authenticated:
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()
    
    data = []
    for product in product_list:
        data.append({
            'id': str(product.id),
            'name': product.name,
            'price': float(product.price),
            'description': product.description,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'is_available': product.is_available,
            'category': product.category,
            'user': product.user.username if product.user else 'Anonymous'
        })
    
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize('xml', product)
        return HttpResponse(xml_data, content_type='application/xml')
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': float(product.price),
            'description': product.description,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'is_available': product.is_available,
            'category': product.category,
            'user': product.user.username if product.user else 'Anonymous'
        }
        return JsonResponse(data, safe=False)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    
@csrf_exempt
def register(request):
    if request.method == "POST":
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            form = UserCreationForm(data={
                'username': username,
                'password1': password1,
                'password2': password2
            })
            
            if form.is_valid():
                form.save()
                return JsonResponse({
                    'status': 'success',
                    'message': 'Account created successfully!'
                })
            else:
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = error_list
                return JsonResponse({
                    'status': 'error',
                    'errors': errors
                }, status=400)
        else:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created')
                return redirect('main:login')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'status': 'success',
                    'message': 'Login successful!'
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid username or password'
                }, status=400)
        else:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)
    
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response