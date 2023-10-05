from django.test import TestCase
from django.shortcuts import render, redirect
import requests
### This is a testing code for local environment.
def kakao_login(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)

def kakaoLoginLogic(request):
    _restApiKey = '853d3c186500d34b233c2c5f3fa780e5' #'1d9169cf5a6507229beb1811c1516ec3' <- used in the server.
    _redirectUrl = 'http://127.0.0.1:8000/users/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = '853d3c186500d34b233c2c5f3fa780e5'
    _redirect_uri = 'http://127.0.0.1:8000/users/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()

    _access_token = _result['access_token']
    _kakao_user_api = 'https://kapi.kakao.com/v2/user/me'
    _header = {'Authorization': f'Bearer {_access_token}'}
    print("#####access_token#####", _access_token)
    _user_info = requests.get(_kakao_user_api, headers=_header).json()
    _data_you_need = {"third_party": "kakao","id": _user_info['id'],"access_token": _access_token}
    print("#####data_you_need#####", _data_you_need)
    print("user_info", _user_info)
    _kakao_account = _user_info['kakao_account']
    print("kakao_account : ", _kakao_account)
    print("nickname : ", _kakao_account['profile']['nickname'])

    request.session['access_token'] = _access_token
    request.session.modified = True
    return render(request, 'loginSuccess.html')

def kakaoLogout(request):
    _token = request.session['access_token']
    _url = 'https://kapi.kakao.com/v1/user/logout'
    _header = {
      'Authorization': f'bearer {_token}'
    }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        del request.session['access_token']
        return render(request, 'loginoutSuccess.html')
    else:
        return render(request, 'logoutError.html')
