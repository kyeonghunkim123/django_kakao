from django.contrib import admin
from django.urls import path, include

from mypage import views

urlpatterns = [
    path('main/', views.main),
    path('myreviews/', views.myreviews),
    path('travelreviews/', views.travelreviews),

    path('dibs/', views.dibs),
    path('dibs/create/', views.dibs_create),
    path('dibs/delete/', views.dibs_delete),

    path('myreview/detail/', views.myreview_detail),
    path('myreview/save/', views.myreview_save),

    path('profile/', views.profile),
    path('profile/update/', views.profile_update),

    path('configs/', views.configs),
    path('config/update/', views.config_update),

    path('notices/', views.notices),
    path('notice/detail/', views.notice_detail),

    path('terms/', views.terms),
]




