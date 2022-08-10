from django.contrib import admin
from django.urls import path
from proyecto_app.views import create_product, create_usuario , search_product , search_usuario , search_blog, list_products, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-product/',create_product,name='create_product'),
    path('create-usuario/', create_usuario, name= 'create_usuario'),
    path('search-product/',search_product, name= 'search_product'),
    path('search-usuario/', search_usuario, name= 'search_usuario'),
    path('search-blog/',search_blog, name= 'search_blog'),
    path('home/', home, name='home'),
    path('list-products/', list_products, name='list_products'),
]