
from django.contrib import admin
from django.urls import path, include
app_name='ecart'
from . import views

urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProDetail, name='Product_cat_detail')

]
