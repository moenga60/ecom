from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name='index'),
    path("shop/", views.shop, name='shop'),
    path("aboutus/", views.aboutus, name='aboutus'),
    path("services/", views.services, name='services'),
    path("blog/", views.blog, name='blog'),
    path("contactus/", views.contactus, name='contactus'),
    path("thankyou/", views.thankyou, name='thankyou'),
    path('checkout/', views.checkout, name='checkout')
]

