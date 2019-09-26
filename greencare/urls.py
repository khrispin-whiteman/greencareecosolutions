from django.conf.urls import url
from django.urls import path

from greencare import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contactus, name='contact'),
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('newslist/', views.newslist, name='newslist'),
    path('newslist/<int:news_id>/', views.newsdetail, name='newsdetail'),

    #agriculture
    path('agriculturehome/', views.agriculturehome, name='agriculturehome')
]