import pandas as pd
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
# import jwt
# from jwt.algorithms import RSAAlgorithm
from rest_framework import exceptions
import json
from datetime import datetime

from users.models import UserInfo, UserStatus, UserFeedback, UserLocation
from schedule.models import ScheduleInfo, SchedulePlace, PlaceInfo, Accommodation, Terminal, Restaurant

from schedule.utils import calculate_distance
# ------------------------------------

@api_view(['POST'])
def login(request):
    return Response("data", status=200)

@api_view(['POST'])
def logout(request):
    return Response("data", status=200)


# -------------------------------------------------

### COORDINATE SETTING
# location 계산을 위해 모든 관광지, 음식점, 숙소, 터미널의 x, y좌표를 dataframe으로 만들어놓음
# column_name = ['id', 'mapx', 'mapy']
# all_place_info = PlaceInfo.objects.all().values('place_id', 'mapx', 'mapy')
# all_place_info = pd.DataFrame.from_records(all_place_info).rename(columns={'place_id': 'id'})
# all_restro_info = Restaurant.objects.all().values('restro_id', 'mapx', 'mapy')
# all_restro_info = pd.DataFrame.from_records(all_restro_info).rename(columns={'restro_id': 'id'})
# all_accom_info = Accommodation.objects.all().values('accom_id', 'mapx', 'mapy')
# all_accom_info = pd.DataFrame.from_records(all_accom_info).rename(columns={'accom_id': 'id'})
# all_terminal_info = Terminal.objects.all().values('id', 'mapx', 'mapy')
# all_terminal_info = pd.DataFrame.from_records(all_terminal_info)
# all_place_info = pd.concat([all_place_info, all_restro_info, all_accom_info, all_terminal_info]).dropna(
#     subset=['mapx', 'mapy'])


# ---------------------------------------------------
def get_kakao_user_info(access_token):
    # data = {
    #     "grant_type": 'authorization_code',
    #     'client_id': '1d9169cf5a6507229beb1811c1516ec3',
    #     'redirect_uri': 'https://nople.o2o.kr/oauth/',
    #     'code': kakao_code
    # }

    # kakao_token_api = 'https://kauth.kakao.com/oauth/token'
    # access_token = requests.post(kakao_token_api, data=data).json()['access_token']

    kakao_user_api = 'https://kapi.kakao.com/v2/user/me'
    header = {'Authorization': f'Bearer {access_token}'}
    user_info = requests.get(kakao_user_api, headers=header).json()
    if 'response' in user_info:
        user_info.update({'oauth_status': True})
    else:
        user_info.update({'oauth_status': False})

    return user_info


def get_naver_user_info(access_token):
    naver_user_api = 'https://openapi.naver.com/v1/nid/me'
    header = {'Authorization': f'Bearer {access_token}'}
    user_info = requests.get(naver_user_api, headers=header).json()
    if 'response' in user_info:
        user_info.update({'oauth_status': True})
    else:
        user_info.update({'oauth_status': False})

    return user_info

## NEED TO WAIT FOR SETTING APPLE DEVERERS SYSTEM
# def get_apple_user_info(apple_user_token):
#     apple_user_api = 'https://appleid.apple.com/auth/keys'
#
#     try:
#         unverified_header = jwt.get_unverified_header(apple_user_token)
#
#         key_payload = requests.get(apple_user_api).json()
#         keys = key_payload["keys"]
#
#         for key in keys:
#             if key["kid"] == unverified_header["kid"]:
#                 public_key = RSAAlgorithm.from_jwk(json.dumps(key))
#
#                 user_info = jwt.decode(
#                     apple_user_token,
#                     public_key,
#                     algorithms="RS256",
#                 )
#
#                 if 'sub' in user_info:
#                     user_info.update({'oauth_status': True})
#                 else:
#                     user_info.update({'oauth_status': False})
#
#                 return user_info
#     except Exception:
#         raise exceptions.AuthenticationFailed
#
#     # header = {'Authorization': f'Bearer {access_token}'}
#     # user_info = requests.get(apple_user_api, headers=header).json()


def get_google_user_info(access_token):
    # token_val = id_token.verify_oauth2_token(
    # {token},
    # requests.Request(),
    # audience={audience}), # optional

    user_info = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={access_token}").json()
    if 'response' in user_info:
        user_info.update({'oauth_status': True})
    else:
        user_info.update({'oauth_status': False})

    return user_info


# 현재 여행 정보 DB에서 확인
def get_user_status(user_id):
    now = datetime.now()
    today = now.date()

    # schedule_list = ScheduleInfo.objects.filter(Q(user_id=user_id) & Q(start_date__lte=today) & Q(end_date__gte=today)).values('skd_id', 'skd_name', 'start_date', 'end_date')
    schedule_list = ScheduleInfo.objects.filter(Q(user_id=user_id) & Q(start_date__lte=today) & Q(end_date__gte=today)).values('skd_id')
    if schedule_list:
        # print(schedule_list)
        traveling = True
        travelSkdId = schedule_list[0]['skd_id']
    else:
        traveling = False
        travelSkdId = None

    return traveling, travelSkdId


def check_moving_status(lat, lon, place_info):
    moving_status = ['moving', 'arrived']

    des_lat = place_info['mapy']
    des_lon = place_info['mapx']
    dist = calculate_distance(lat, lon, des_lat, des_lon)

    if place_info['id'].tolist()[0].startswith('R'):
        if dist <= 0.2:
            return moving_status[1]
        else:
            return moving_status[0]
    else:
        if dist <= 1:
            return moving_status[1]
        else:
            return moving_status[0]


# Create your views here.
@api_view(['POST'])
def save_kakao_data(request):
    """프론트에서 보낸 kakao의 user data를 DB에 저장
    """
    body_data = json.loads(request.body)
    print('save_kakao_data body_date:', body_data)
    age_range = body_data['ageRange']
    age_range_agree = body_data['ageRangeNeedsAgreement']
    gender = body_data['gender']
    gender_agree = body_data['genderNeedsAgreement']
    birthday = body_data['birthday']
    birthday_agree = body_data['birthdayNeedsAgreement']
    birthday_type = body_data['birthdayType']
    email = body_data['email']
    email_agree = body_data['emailNeedsAgreement']
    kakao_id = body_data['id']
    nickname = body_data['nickname']
    image_url = body_data['profileImageUrl']
    image_url_agree = body_data['profileNeedsAgreement']

    # access_token = body_data['accessToken']
    # access_token_expire = body_data['accessTokenExpiresAt']
    # refresh_token = body_data['refreshToken']
    # refresh_token_expire = body_data['refreshTokenExpiresAt']

    if not UserInfo.objects.filter(kakao_id=kakao_id).exists():
        # DB에 데이터 추가
        user_add = UserInfo(nickname=nickname,
                            kakao=True,
                            kakao_id=kakao_id,
                            age_range=age_range,
                            age_range_agreement=age_range_agree,
                            gender=gender,
                            gender_agreement=gender_agree,
                            birthday=birthday,
                            birthday_agreement=birthday_agree,
                            birthday_type=birthday_type,
                            email=email,
                            email_agreement=email_agree,
                            profile_image_url=image_url,
                            profile_image_url_agreement=image_url_agree,
                            join_date=datetime.now().date())
        if 'accessToken' in body_data.keys(): user_add.access_token = body_data['accessToken']
        if 'accessTokenExpiresAt' in body_data.keys(): user_add.access_token_expire = body_data['accessTokenExpiresAt']
        if 'refreshToken' in body_data.keys(): user_add.refresh_token = body_data['refreshToken']
        if 'refreshTokenExpiresAt' in body_data.keys(): user_add.refresh_token_expire = body_data[
            'refreshTokenExpiresAt']
        user_id = user_add.save()

        user_info_obj = UserInfo.objects.get(user_id=user_id)
        user_status = UserStatus(user_id=user_info_obj,
                                 moving_status=None,
                                 travelling=False,
                                 travel_skd_id=None,
                                 current_place_id=None)
        user_status.save()

        result = {'status': status.HTTP_200_OK, 'user_id': user_id, 'travelling': False, 'travelSkdId': None}
        print(result)
        return Response(result)

    else:
        user_id = UserInfo.objects.filter(kakao_id=kakao_id).values('user_id')[0]['user_id']
        user_status = UserStatus.objects.filter(user_id=user_id).values('travelling', 'travel_skd_id')

        if user_status:
            travelling = user_status[0]['travelling']
            travel_skd_id = user_status[0]['travel_skd_id']

        # travelling, travelSkdId = get_user_status(user_id)
        result = {'status': status.HTTP_200_OK, 'msg': 'kakao_id가 이미 존재합니다.', 'user_id': user_id,
                  'travelling': travelling, 'travelSkdId': travel_skd_id}
        print(result)
        return Response(result)


# @swagger_auto_schema(method='post',
#                      tags=['user'],
#                      #  request_body=CreateScheduleSerializer,
#                      responses={200: 'Success',
#                                 # 400:
#                                 #     ec.APPLY_400_FIELD_REQUIRED.as_md() +
#                                 #     ec.APPLY_400_PLACEINFO_NOT_EXIST.as_md(),
#                                 # 405: ec.APPLY_405_METHOD_NOT_ALLOWED.as_md(),
#                                 # 503: ec.APPLY_503_SCHEDULING_SERVICE_UNAVAILABLE.as_md()
#                                 })

@api_view(['POST'])
def social_login(request):
    """_summary_
    """
    body_data = json.loads(request.body)
    print('third_party_oauth body_date:', body_data)
    third_party_id = body_data['id']
    third_party = body_data['third_party']
    access_code = body_data['access_code']

    result = dict()

    try:
        if third_party == 'kakao':
            if not UserInfo.objects.filter(kakao_id=third_party_id).exists():
                user_info = get_kakao_user_info(access_code)
                if user_info['oauth_status'] == True:
                    kakao_account = user_info['kakao_account']
                    # DB에 데이터 추가
                    user_add = UserInfo(kakao=True,
                                        kakao_id=third_party_id,
                                        join_date=datetime.now().date(), )
                    if 'profile' in kakao_account.keys(): user_add.profile_nickname = kakao_account['profile'][
                        'nickname']
                    if 'gender' in kakao_account.keys(): user_add.gender = kakao_account['gender']
                    # if 'email' in kakao_account.keys(): user_add.account_email=kakao_account['email']
                    # if 'age_range' in kakao_account.keys(): user_add.age_range=kakao_account['age_range']
                    # if 'birthday' in kakao_account.keys(): user_add.birthday=kakao_account['birthday']
                    user_id = user_add.save()

                    result = {'status': status.HTTP_200_OK, 'msg': f'id {user_id}를 추가했습니다.', 'user_id': user_id}
                    request.session['user_id'] = user_id
                else:
                    result = {'status': status.HTTP_400_BAD_REQUEST, 'msg': 'access_token으로 받아올 수 있는 데이터가 없습니다',
                              'user_info': user_info}
            else:
                user_id = UserInfo.objects.filter(kakao_id=third_party_id).values('user_id')[0]['user_id']
                result = {'status': status.HTTP_200_OK, 'msg': 'id가 존재합니다.', 'user_id': user_id}
                request.session['user_id'] = user_id

        elif third_party == 'naver':
            if not UserInfo.objects.filter(naver_id=third_party_id).exists():
                user_info = get_naver_user_info(access_code)
                if user_info['oauth_status'] == True:
                    naver_account = user_info['response']
                    # DB에 데이터 추가
                    user_add = UserInfo(naver=True,
                                        naver_id=third_party_id,
                                        join_date=datetime.now().date(), )
                    if 'nickname' in naver_account.keys(): user_add.profile_nickname = naver_account['nickname']
                    if 'gender' in naver_account.keys(): user_add.gender = naver_account['gender']
                    user_id = user_add.save()

                    result = {'status': status.HTTP_200_OK, 'msg': f'id {user_id}를 추가했습니다.', 'user_id': user_id}
                    request.session['user_id'] = user_id
                else:
                    result = {'status': status.HTTP_400_BAD_REQUEST, 'msg': 'access_token으로 받아올 수 있는 데이터가 없습니다',
                              'user_info': user_info}
            else:
                user_id = UserInfo.objects.filter(naver_id=third_party_id).values('user_id')[0]['user_id']
                result = {'status': status.HTTP_200_OK, 'msg': 'id가 존재합니다.', 'user_id': user_id}
                request.session['user_id'] = user_id

        # elif third_party == 'apple':
        #     if not UserInfo.objects.filter(apple_id=third_party_id).exists():
        #         user_info = get_apple_user_info(access_code)
        #         if user_info['oauth_status'] == True:
        #             apple_id = user_info['sub']
        #             # DB에 데이터 추가
        #             user_add = UserInfo(user_id=user_id,
        #                                 apple=True,
        #                                 apple_id=third_party_id,
        #                                 join_date=datetime.now().date(), )
        #             if 'email' in user_info.keys(): user_add.profile_nickname = user_info['email']
        #             if 'gender' in user_info.keys(): user_add.gender = user_info['gender']
        #             user_id = user_add.save()
        #
        #             result = {'status': status.HTTP_200_OK, 'msg': f'id {user_id}를 추가했습니다.', 'user_id': user_id}
        #             request.session['user_id'] = user_id
        #         else:
        #             result = {'status': status.HTTP_400_BAD_REQUEST, 'msg': 'access_token으로 받아올 수 있는 데이터가 없습니다',
        #                       'user_info': user_info}
        #     else:
        #         user_id = UserInfo.objects.filter(apple_id=third_party_id).values('user_id')[0]['user_id']
        #         result = {'status': status.HTTP_200_OK, 'msg': 'id가 존재합니다.', 'user_id': user_id}
        #         request.session['user_id'] = user_id

        elif third_party == 'google':
            if not UserInfo.objects.filter(google_id=third_party_id).exists():
                user_info = get_google_user_info(access_code)
                if user_info['oauth_status'] == True:
                    google_account = user_info['google_account']
                    # DB에 데이터 추가
                    user_add = UserInfo(google=True,
                                        google_id=third_party_id,
                                        join_date=datetime.now().date(), )
                    if 'profile' in google_account.keys(): user_add.profile_nickname = google_account['profile'][
                        'nickname']
                    if 'gender' in google_account.keys(): user_add.gender = google_account['gender']
                    user_id = user_add.save()

                    result = {'status': status.HTTP_200_OK, 'msg': f'id {user_id}를 추가했습니다.', 'user_id': user_id}
                    request.session['user_id'] = user_id
                else:
                    result = {'status': status.HTTP_400_BAD_REQUEST, 'msg': 'access_token으로 받아올 수 있는 데이터가 없습니다',
                              'user_info': user_info}
            else:
                user_id = UserInfo.objects.filter(google_id=third_party_id).values('user_id')[0]['user_id']
                result = {'status': status.HTTP_200_OK, 'msg': 'id가 존재합니다.', 'user_id': user_id}
                request.session['user_id'] = user_id

    except Exception as e:
        result = {'status': status.HTTP_400_BAD_REQUEST, 'msg': e}

    print(result)
    return Response(result)


@api_view(['POST'])
def user_session_chk(request):
    """세션을 확인해서 자동로그인 시키기 위한 api
    """
    body_data = json.loads(request.body)
    print('save_kakao_data body_date:', body_data)
    id = body_data['id']
    session = body_data['session']

    result = {'status': status.HTTP_200_OK, 'msg': 'kakao_id가 이미 존재합니다.'}
    print(result)
    return Response(result)


@api_view(['GET'])
def is_travelling(request):
    """여행 시작할 때 프론트에서  userId, skdId 던지면 user db의 travelling이 true가 되는 api
    """
    user_id = request.GET.get('userId', '')
    skd_id = request.GET.get('skdId', '')
    state = request.GET.get('state', '')
    print('is_travelling user_id:', user_id, 'skd_id:', skd_id, 'state:', state)

    if user_id != '' and skd_id != '':
        if state == 'start':
            skd_id_obj = ScheduleInfo.objects.get(skd_id=skd_id)
            user_info_obj = UserInfo.objects.get(user_id=user_id)
            # UserStatus 초기값 세팅. current_place_id는 공항이므로 1로 저장
            user_status = UserStatus(user_id=user_info_obj,
                                     moving_status='pause',
                                     travelling=True,
                                     travel_skd_id=skd_id_obj,
                                     current_place_id='1')
            user_status.save()
        elif state == 'end':
            user_status_obj = UserStatus.objects.get(user_id=user_id)
            user_status_obj.travelling = False
            user_status_obj.travel_skd_id = None
            user_status_obj.current_place_id = None
            user_status_obj.moving_status = None
            user_status_obj.save()

        result = {'status': status.HTTP_200_OK}
        print('is_travelling result:', result)
        return Response(result)
    else:
        result = {'status': status.HTTP_400_BAD_REQUEST,
                  'msg': f'데이터 값이 잘못 되었습니다. userId: {user_id} , skdId: {skd_id}'}
        print('is_travelling result:', result)
        return Response(result)


@api_view(['POST'])
def save_user_location(request):
    """프론트에서 보낸 kakao의 user data를 DB에 저장
    """
    body_data = json.loads(request.body)
    print('save_user_location body_date:', body_data)

    user_id = body_data['userId']
    lat = body_data['lat']
    lon = body_data['lng']

    return_dict = dict()
    today = datetime.now()
    formatted_date = today.date()

    try:
        # UserStatus 데이터 업데이트
        user_info_obj = UserInfo.objects.get(user_id=user_id)
        user_status_obj = UserStatus.objects.get(user_id=user_id)

        user_status_value = UserStatus.objects.filter(user_id=user_id).values('travel_skd_id', 'current_place_id')[0]
        travel_skd_id = user_status_value['travel_skd_id']
        current_place_id = user_status_value['current_place_id']

        if current_place_id.isdigit():
            destination_order_num = SchedulePlace.objects.filter(
                Q(terminal_id=current_place_id),
                skd_id=travel_skd_id,
                date=formatted_date
            ).values('destination_order_num')[0]['destination_order_num']
        else:
            destination_order_num = SchedulePlace.objects.filter(
                Q(place_id=current_place_id) | Q(accom_id=current_place_id) | Q(restro_id=current_place_id),
                skd_id=travel_skd_id,
                date=formatted_date
            ).values('destination_order_num')[0]['destination_order_num']

        print("destination_order_num:", destination_order_num)

        next_place_id = SchedulePlace.objects.filter(
            skd_id=travel_skd_id,
            date=formatted_date,
            destination_order_num=destination_order_num + 1
        ).values_list('place_id', 'accom_id', 'restro_id', 'terminal_id')
        # 'place_id', 'accom_id', 'restro_id', 'terminal_id' 중 값이 있는 것만 리스트에 추가
        for row in next_place_id:
            for id_value in row:
                if id_value is not None:
                    next_place_id = id_value
        print('next_place_id:', next_place_id)

        # 1차 검사 (현재 place 기준)
        current_place_info = all_place_info.loc[all_place_info['id'] == current_place_id]
        current_moving_status = check_moving_status(lat, lon, current_place_info)

        if current_moving_status == 'arrived':
            user_status_obj.moving_status = 'pause'
            return_dict['movingStatus'] = 'pause'
        else:
            # 2차 검사 (다음 place 기준)
            next_place_info = all_place_info.loc[all_place_info['id'] == next_place_id]
            next_moving_status = check_moving_status(lat, lon, next_place_info)

            next_moving_status = 'arrived'
            if next_moving_status == 'arrived':
                user_status_obj.moving_status = 'arrived'
                return_dict['movingStatus'] = 'arrived'

                place_id = next_place_info['id'].tolist()[0]
                return_dict['placeId'] = place_id
                user_status_obj.current_place_id = place_id

                if place_id.isdigit():
                    if place_id == 1:
                        place_name = Terminal.objects.filter(id=place_id).values('place_name')[0]['place_name']
                else:
                    if place_id.startswith('P'):
                        place_name = PlaceInfo.objects.filter(place_id=place_id).values('place_name')[0]['place_name']
                    elif place_id.startswith('A'):
                        place_name = Accommodation.objects.filter(accom_id=place_id).values('accom_name')[0][
                            'accom_name']
                    elif place_id.startswith('R'):
                        place_name = Restaurant.objects.filter(restro_id=place_id).values('restro_name')[0][
                            'restro_name']
                return_dict['placeName'] = place_name
            else:
                user_status_obj.moving_status = 'moving'
                return_dict['movingStatus'] = 'moving'
        user_status_obj.save()

        # UserLocation 데이터 업데이트
        if UserLocation.objects.filter(user_id=user_id).count() <= 12:
            user_loc_save = UserLocation(user_id=user_info_obj,
                                         lat=lat,
                                         lon=lon)
            user_loc_save.save()
            result = {'status': status.HTTP_200_OK, 'msg': '새로운 데이터 추가', 'result': return_dict}
        else:
            # data_chk = UserLocation.objects.filter(user_id=user_id).order_by('chk_date').values('chk_date', 'lat', 'lon')
            # print('data_chk', data_chk)
            user_info = UserLocation.objects.filter(user_id=user_id).order_by('chk_date').first()
            user_info.lat = lat
            user_info.lon = lon
            user_info.save()
            result = {'status': status.HTTP_200_OK, 'msg': '기존 데이터 업데이트함', 'result': return_dict}

    except Exception as e:
        result = {'status': status.HTTP_400_BAD_REQUEST, 'msg': e}

    print('save_user_location resp:', result)
    return Response(result)


@api_view(['GET'])
def to_next_place(request):
    """skd_id로 스케줄 찾아서 리턴 (자세한 정보)
    Param {skdId: 스케줄 id}
    """
    user_id = request.GET.get('userId', '')
    arrived = request.GET.get('arrived', '')
    place_id = request.GET.get('placeId', '')
    print('get_next_schedule user_id:', user_id, ', arrived:', arrived, ', place_id:', place_id)

    user_status_obj = UserStatus.objects.get(user_id=user_id)
    if arrived == True:
        user_status_obj.moving_status = 'pause'
        user_status_obj.current_place_id = place_id
    else:
        user_status_obj.moving_status = 'moving'
    user_status_obj.save()

    result = {"status": status.HTTP_200_OK}
    print('get_next_schedule resp:', result)
    return Response(result)


@api_view(['POST'])
def alpha_feedback(request):
    """프론트에서 보낸 kakao의 user data를 DB에 저장
    """
    body_data = json.loads(request.body)
    print('alpha_feedback body_date:', body_data)

    user_id = body_data['userId']
    feedback = body_data['feedback']
    screen = body_data['screen']

    if not UserFeedback.objects.filter(user_id=user_id, feedback=feedback).exists():
        user_info_obj = UserInfo.get(user_id=user_id)
        feedback_add = UserFeedback(user_id=user_info_obj,
                                    feedback=feedback,
                                    screen=screen)
        feedback_add.save()

        result = {'status': status.HTTP_200_OK}

    else:
        result = {'status': status.HTTP_400_BAD_REQUEST, 'msg': '동일한 피드백이 이미 존재합니다.'}

    print('alpha_feedback resp:', result)
    return Response(result)