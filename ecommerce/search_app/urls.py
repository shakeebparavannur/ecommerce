from django.urls import path, include
app_name='search_app'
from . import views

urlpatterns= [
    path('search',views.SeachResult,name='searchapp'),
]