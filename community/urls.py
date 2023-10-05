from django.contrib import admin
from django.urls import path, include

from community import views

app_name = 'community'

urlpatterns = [
    path('main/', views.main),
    path('feed/myfeeds/', views.feed_myfeeds),
    path('feed/write/', views.feed_write),

    path('feed/myfeed/update/', views.feed_myfeed_update), # 'GET' is used for 'editing,' while 'POST' is used for 'editing completion.'

    path('travelreviews/', views.travelreviews),
    path('plans/', views.plans),

    path('travelreview/write/', views.travelreview_write),
    path('travelreview/detail/', views.travelreview_detail),
    path('travelreview/update/', views.travelreview_update),

    path('search/aftertravel/', views.search_aftertravel),

]
