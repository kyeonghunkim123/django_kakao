from django.db import models
from django_mysql.models import ListCharField
from datetime import datetime, date
from django.utils import timezone


# Create your models here.
class ScheduleInfo(models.Model):
    skd_id = models.CharField(max_length=250, primary_key=True)
    user_id = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE, db_column='user_id')
    skd_name = models.CharField(max_length=500)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    companion = models.IntegerField()
    theme = ListCharField(models.CharField(max_length=100), null=True, max_length=(6 * 11))
    transport_type = models.IntegerField()

    class Meta:
        db_table = 'ScheduleInfo'

    def save(self, *args, **kwargs):
        if not self.skd_id:
            # 새로운 객체인 경우에만 기본 키 생성
            user_id = self.user_id.user_id
            id_number = ScheduleInfo.objects.filter(user_id=self.user_id).count() + 1
            # padding_length = 4 - len(str(id_number))
            padding_length = 3
            skd_id = f'{str(user_id)}-{id_number:0{padding_length}}'
            self.skd_id = skd_id
        if self.start_date and isinstance(self.start_date, date):
            # 입력된 값이 date 형식인 경우에만 기본값 생성
            default_time = timezone.now().time()
            start_date_time = datetime.combine(self.start_date, default_time)
            current_tz = timezone.get_current_timezone()
            self.start_date = current_tz.localize(start_date_time)
        if self.end_date and isinstance(self.end_date, date):
            # 입력된 값이 date 형식인 경우에만 기본값 생성
            default_time = timezone.now().time()
            end_date_time = datetime.combine(self.end_date, default_time)
            current_tz = timezone.get_current_timezone()
            self.end_date = current_tz.localize(end_date_time)
        super().save(*args, **kwargs)
        return self.skd_id


class SchedulePlace(models.Model):
    pid = models.AutoField(primary_key=True)
    skd_id = models.ForeignKey('ScheduleInfo', on_delete=models.CASCADE, db_column='skd_id')
    place_id = models.ForeignKey('schedule.PlaceInfo', null=True, blank=True, on_delete=models.CASCADE,
                                 db_column='place_id', db_constraint=False)
    accom_id = models.ForeignKey('schedule.Accommodation', null=True, blank=True, on_delete=models.CASCADE,
                                 db_column='accom_id', db_constraint=False)
    restro_id = models.ForeignKey('schedule.Restaurant', null=True, blank=True, on_delete=models.CASCADE,
                                  db_column='restro_id', db_constraint=False)
    terminal_id = models.ForeignKey('schedule.Terminal', null=True, blank=True, on_delete=models.CASCADE, db_column='id',
                                    db_constraint=False)
    date = models.DateField(null=True)
    destination_order_num = models.IntegerField(null=True)

    class Meta:
        db_table = 'SchedulePlace'




# ------------------------------------------
# All places

class PlaceInfo(models.Model):
    place_id = models.CharField(primary_key=True, max_length=100)
    contenttypeid = models.IntegerField(blank=True, null=True)
    tourapi_contentid = models.IntegerField(blank=True, null=True)
    place_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    mapx = models.FloatField(blank=True, null=True)
    mapy = models.FloatField(blank=True, null=True)
    image_url = models.CharField(max_length=1000, blank=True, null=True)
    tel = models.CharField(max_length=100, blank=True, null=True)
    cat1 = models.CharField(max_length=255, blank=True, null=True)
    cat2 = models.CharField(max_length=255, blank=True, null=True)
    cat3 = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    overview = models.CharField(max_length=5000, blank=True, null=True)
    recommender_src = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'PlaceInfo'


class PlaceInfoDetail(models.Model):
    place = models.OneToOneField(PlaceInfo, models.DO_NOTHING, primary_key=True)
    accom_count = models.CharField(max_length=500, blank=True, null=True)
    chk_baby_carriage = models.CharField(max_length=500, blank=True, null=True)
    chk_credit_card = models.CharField(max_length=500, blank=True, null=True)
    chk_pet = models.CharField(max_length=500, blank=True, null=True)
    discount_info = models.CharField(max_length=500, blank=True, null=True)
    exp_age_range = models.CharField(max_length=500, blank=True, null=True)
    exp_guide = models.CharField(max_length=1500, blank=True, null=True)
    info_center = models.CharField(max_length=500, blank=True, null=True)
    parking = models.CharField(max_length=500, blank=True, null=True)
    parking_fee = models.CharField(max_length=500, blank=True, null=True)
    rest_date = models.CharField(max_length=500, blank=True, null=True)
    spend_time = models.CharField(max_length=500, blank=True, null=True)
    use_fee = models.CharField(max_length=1000, blank=True, null=True)
    use_time = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'PlaceInfoDetail'


class PlaceInfoNaver(models.Model):
    place = models.OneToOneField(PlaceInfo, models.DO_NOTHING, primary_key=True)
    naver_id = models.CharField(max_length=500)
    cat = models.CharField(max_length=500, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    road_address = models.CharField(max_length=500, blank=True, null=True)
    opening_hour = models.CharField(max_length=500, blank=True, null=True)
    tel = models.CharField(max_length=500, blank=True, null=True)
    use_fee = models.JSONField(blank=True, null=True)
    chk_parking = models.IntegerField(blank=True, null=True)
    chk_booking = models.IntegerField(blank=True, null=True)
    chk_wifi = models.IntegerField(blank=True, null=True)
    chk_facilities = models.CharField(max_length=500, blank=True, null=True)
    hashtag = models.CharField(max_length=500, blank=True, null=True)
    homepage = models.JSONField(blank=True, null=True)
    overview = models.CharField(max_length=5000, blank=True, null=True)
    overview_href = models.CharField(max_length=500, blank=True, null=True)
    chk_pet = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'PlaceInfoNaver'


class Accommodation(models.Model):
    accom_id = models.CharField(primary_key=True, max_length=100)
    contenttypeid = models.IntegerField(blank=True, null=True)
    tourapi_contentid = models.IntegerField(blank=True, null=True)
    accom_name = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    mapx = models.FloatField(blank=True, null=True)
    mapy = models.FloatField(blank=True, null=True)
    image_url = models.CharField(max_length=1000, blank=True, null=True)
    tel = models.CharField(max_length=100, blank=True, null=True)
    cat1 = models.CharField(max_length=255, blank=True, null=True)
    cat2 = models.CharField(max_length=255, blank=True, null=True)
    cat3 = models.CharField(max_length=255, blank=True, null=True)
    check_in_time = models.CharField(max_length=255, blank=True, null=True)
    check_out_time = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    parking = models.CharField(max_length=255, blank=True, null=True)
    subfacility = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Accommodation'


class AccomInfoNaver(models.Model):
    accom = models.OneToOneField(Accommodation, models.DO_NOTHING, primary_key=True)
    naver_id = models.CharField(max_length=500)
    cat = models.CharField(max_length=500, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    road_address = models.CharField(max_length=500, blank=True, null=True)
    opening_hour = models.JSONField(blank=True, null=True)
    tel = models.CharField(max_length=500, blank=True, null=True)
    use_fee = models.JSONField(blank=True, null=True)
    chk_facilities = models.CharField(max_length=500, blank=True, null=True)
    homepage = models.JSONField(blank=True, null=True)
    overview = models.CharField(max_length=5000, blank=True, null=True)
    booking_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'AccomInfoNaver'


class Terminal(models.Model):
    id = models.BigAutoField(primary_key=True)
    place_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    mapx = models.FloatField()
    mapy = models.FloatField()
    additional_values = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Terminal'


class PlaceStatus(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    place_id = models.ForeignKey('schedule.PlaceInfo', on_delete=models.CASCADE, db_column='place_id')
    check_time = models.DateTimeField(null=True)
    post_cnt = models.IntegerField(null=True)
    congestion = models.BooleanField(default=False)
    congestion_cnt = models.IntegerField(null=True)
    temp_closure = models.BooleanField(default=False)
    temp_closure_cnt = models.IntegerField(null=True)
    # weather = models.BooleanField(default=False)
    # weather_cnt = models.IntegerField(null=True)
    weather_etc = models.BooleanField(default=False)
    weather_etc_cnt = models.IntegerField(null=True)
    weather_heat = models.BooleanField(default=False)
    weather_heat_cnt = models.IntegerField(null=True)
    weather_rain = models.BooleanField(default=False)
    weather_rain_cnt = models.IntegerField(null=True)
    weather_snow = models.BooleanField(default=False)
    weather_snow_cnt = models.IntegerField(null=True)

    class Meta:
        db_table = 'PlaceStatus'


class RestroStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    restro_id = models.ForeignKey('schedule.Restaurant', on_delete=models.CASCADE, db_column='restro_id')
    check_time = models.DateTimeField(null=True)
    post_cnt = models.IntegerField(null=True)
    congestion = models.CharField(max_length=255, null=True)
    congestion_cnt = models.IntegerField(null=True)
    temp_closure = models.CharField(max_length=255, null=True)
    temp_closure_cnt = models.IntegerField(null=True)
    # weather = models.BooleanField(default=False)
    # weather_cnt = models.IntegerField(null=True)
    weather_etc = models.BooleanField(default=False)
    weather_etc_cnt = models.IntegerField(null=True)
    weather_heat = models.BooleanField(default=False)
    weather_heat_cnt = models.IntegerField(null=True)
    weather_rain = models.BooleanField(default=False)
    weather_rain_cnt = models.IntegerField(null=True)
    weather_snow = models.BooleanField(default=False)
    weather_snow_cnt = models.IntegerField(null=True)

    class Meta:
        db_table = 'RestroStatus'




# ------------------------------------------
# Especially Restaurant

class Restaurant(models.Model):
    restro_id = models.CharField(primary_key=True, max_length=100)
    business_code = models.IntegerField(blank=True, null=True)
    localdata_no = models.CharField(max_length=500, blank=True, null=True)
    restro_name = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    road_address = models.CharField(max_length=1000, blank=True, null=True)
    mapx = models.FloatField(blank=True, null=True)
    mapy = models.FloatField(blank=True, null=True)
    image_url = models.CharField(max_length=1000, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)
    cat = models.CharField(max_length=255, blank=True, null=True)
    opening_hour = models.CharField(max_length=1000, blank=True, null=True)
    homepage = models.CharField(max_length=500, blank=True, null=True)
    external_link = models.CharField(max_length=500, blank=True, null=True)
    zzinview_id = models.IntegerField(blank=True, null=True)
    zzinview_score = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'Restaurant'


class RestroInfoNaver(models.Model):
    restro = models.OneToOneField(Restaurant, models.DO_NOTHING, primary_key=True)
    naver_id = models.CharField(max_length=500)
    cat = models.CharField(max_length=500, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    road_address = models.CharField(max_length=500, blank=True, null=True)
    opening_hour = models.CharField(max_length=1000, blank=True, null=True)
    tel = models.CharField(max_length=500, blank=True, null=True)
    chk_parking = models.IntegerField(blank=True, null=True)
    chk_booking = models.IntegerField(blank=True, null=True)
    chk_wifi = models.IntegerField(blank=True, null=True)
    chk_takeout = models.IntegerField(blank=True, null=True)
    chk_group_seat = models.IntegerField(blank=True, null=True)
    chk_facilities = models.CharField(max_length=500, blank=True, null=True)
    menu = models.JSONField(blank=True, null=True)
    homepage = models.JSONField(blank=True, null=True)
    overview = models.CharField(max_length=5000, blank=True, null=True)
    chk_pet = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'RestroInfoNaver'


