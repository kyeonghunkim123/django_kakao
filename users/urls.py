from django.urls import path
from users import views
from users import tests as ut

urlpatterns = [
    #-----------------------------------------------
    # For Testing - kakao login
    path('kakao-login', ut.kakao_login, name='kakao'), # http://127.0.0.1:8000/users/kakao-login
    path('kakaoLoginLogic/', ut.kakaoLoginLogic),
    path('kakaoLoginLogicRedirect/', ut.kakaoLoginLogicRedirect),
    path('kakaoLogout/', ut.kakaoLogout),

    # -----------------------------------------------
    path('social-login/', views.social_login),

    path('login/', views.login),
    path('logout/', views.logout),





]






