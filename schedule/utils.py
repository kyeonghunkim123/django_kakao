import math
import numpy as np


def calculate_distance(lat1, lon1, lat2, lon2):
    # 지구의 반경 (km)
    radius = 6371

    # 위도, 경도를 라디안으로 변환
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # 위도 및 경도의 차이 계산
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # 허버스인 거리 공식 계산
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(
        dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance


def search_near_restaurant(current_position, all_place_info):
    cur_lat = current_position['mapy']
    cur_lon = current_position['mapx']

    dist_list = []
    for idx in range(len(all_place_info)):
        des_lat = all_place_info['mapy'].iloc[idx]
        des_lon = all_place_info['mapx'].iloc[idx]
        dist = calculate_distance(cur_lat, cur_lon, des_lat, des_lon)
        dist_list.append(dist)

    all_place_info['distance'] = dist_list
    all_place_info = all_place_info[all_place_info['distance'] <= 15]
    all_place_info = all_place_info.sort_values(by='distance', ascending=True)

    return all_place_info
