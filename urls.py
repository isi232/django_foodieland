from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Home səhifəsi
    path('recipes/', views.recipes, name='recipes'),  # Recipes səhifəsi
    path('blog/', views.blog, name='blog'),  
    path('contact/', views.contact, name='contact'),  
    path('about/', views.about, name='about'),  # About səhifəsi
]
