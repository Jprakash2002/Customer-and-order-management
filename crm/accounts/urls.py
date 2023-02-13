from django.urls import path
from . import views
 
urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('products/',views.products,name='products'),
    path('customers/<str:cusid>/',views.customers,name='customers'),
    path('createorder/<str:cusid>',views.createorder,name='createorder'),
    path('updateorder/<str:ordid>/',views.updateorder,name='updateorder'),
    path('deleteorder/<str:ordid>/',views.deleteorder,name='deleteorder')
]