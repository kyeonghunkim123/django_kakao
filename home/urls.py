from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    #test
    path('test_hello/', views.test_hello),

    #normal functions
    path('main/', views.main),
    path('hotspots/', views.hotspots),
    path('hotrestros/', views.hotrestros),
    path('hotaccoms/', views.hotaccoms),
    path('plans/', views.plans),

    #packing
    path('packing/goods', views.packing_goods),
    path('packing/update', views.packing_update),

    # #notice
    # path('notice/', views.notice),
    # # notification
    # path('notifications', views.notifications),


]




