from django.urls import path
from schedule import views

urlpatterns = [

    path('main/', views.main),
    path('delete/', views.delete),
    path('places/', views.places),
    path('accoms/', views.accoms),

    #schedule/plan/plans-detail
    path('plan/detail/', views.plan_detail),

    path('plan/place/update/', views.plan_place_update),
    path('plan/place/delete/', views.plan_place_delete),

    path('plan/accom/update/', views.plan_accom_update),
    path('plan/accom/delete/', views.plan_accom_delete),

    path('plan/title/update/', views.plan_title_update),

    path('plan/date/update/', views.plan_date_update),
    path('plan/date/delete/', views.plan_date_delete),

    path('aiplan/', views.aiplan),

]
