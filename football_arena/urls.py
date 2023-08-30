

from django.urls import path
from. import views

urlpatterns = [
    path('',views.start,name='start'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('nav',views.nav,name='nav'),
    path('cat',views.cat,name='cat'),
    path('product',views.product,name='product'),
    path('show_products',views.show_products,name='show_products'),
    path('user_detail',views.user_detail,name='user_detail'),
    path('userhome',views.userhome,name='userhome'),
    path('card/<int:pk>',views.card,name='card'),
    path('show_cart',views.show_cart,name='show_cart'),


    path('register',views.register,name='register'),
    path('d_login',views.d_login,name='d_login'),
    path('add_category',views.add_category,name='add_category'),
    path('add_product',views.add_product,name='add_product'),
    path('edit_product/<int:pk>',views.edit_product,name='edit_product'),
    path('delete_product/<int:pk>',views.delete_product,name='delete_product'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user'),
    path('d_logout',views.d_logout,name='d_logout'),
    path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('delete_cart/<int:pk>',views.delete_cart,name='delete_cart')




]
