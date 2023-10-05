from django.db import models
from datetime import datetime


# Create your models here.
class UserInfo(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    nickname = models.CharField(max_length=1000)
    kakao = models.BooleanField(default=False)
    kakao_id = models.CharField(max_length=500, null=True)
    naver = models.BooleanField(default=False)
    naver_id = models.CharField(max_length=500, null=True)
    apple = models.BooleanField(default=False)
    apple_id = models.CharField(max_length=500, null=True)
    google = models.BooleanField(default=False)
    google_id = models.CharField(max_length=500, null=True)
    gender = models.CharField(max_length=500, null=True)
    join_date = models.DateField()

    class Meta:
        db_table = 'UserInfo'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return self.user_id


class UserStatus(models.Model):
    user_id = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE, db_column='user_id', primary_key=True)
    travelling = models.BooleanField(default=False)
    moving_status = models.CharField(max_length=500, null=True)
    travel_skd_id = models.ForeignKey('schedule.ScheduleInfo', on_delete=models.SET_NULL, db_column='skd_id', null=True)
    current_place_id = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = 'UserStatus'


class UserLocation(models.Model):
    user_id = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE, db_column='user_id')
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    chk_date = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'UserLocation'


class UserFeedback(models.Model):
    user_id = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE, db_column='user_id')
    feedback = models.CharField(max_length=1000)
    screen = models.CharField(max_length=500)

    class Meta:
        db_table = 'UserFeedback'

