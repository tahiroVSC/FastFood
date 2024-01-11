from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('blogs/', views.blogs, name='blogs'),
    path('shop/', views.Shop,name ='shop' ),
    path('cart/', views.Cart, name='cart'),
    path('blog-details/<int:id>/', views.blog_details, name='blog-details'),
    path('contact/',views.contact, name='contact' ),
    path('shop-details/<int:id>/',views.shop_detail, name= 'shop-details' )
]