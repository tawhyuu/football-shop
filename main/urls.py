from django.urls import path
from . import views 

app_name = 'main'
urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product/', views.create_product, name='create_product'),
    path('create-car/', views.create_car, name='create_car'),
    path('employee/', views.add_employee, name='employee'),
    path('product/<str:id>/', views.show_product, name='show_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<str:product_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('product/<uuid:id>/edit', views.edit_product, name="edit_product"),
    path('product/<uuid:id>/delete', views.delete_product, name="delete_product"),
    # AJAX endpoints
    path('add-product-ajax/', views.add_product_ajax, name='add_product_ajax'),
    path('edit-product-ajax/<uuid:id>/', views.edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<uuid:id>/', views.delete_product_ajax, name='delete_product_ajax'),
]