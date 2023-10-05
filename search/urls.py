from django.urls import path
from search import views

urlpatterns = [

    path('main/', views.main),
    path('delete/', views.delete),
    path('results/', views.results),
    path('more/', views.more),
    path('categories/', views.categories),


    path('category/review/create/', views.category_review_create),
    path('category/review/update/', views.category_review_update),
    path('category/review/delete/', views.category_review_delete),

    path('category/review/heart/create/', views.category_review_heart_create),
    path('category/review/heart/delete/', views.category_review_heart_delete),

    path('category/review/reply/create/', views.category_review_reply_create),
    path('category/review/reply/update/', views.category_review_reply_update),
    path('category/review/reply/delete/', views.category_review_reply_delete),


    path('author-report/', views.author_report),

]