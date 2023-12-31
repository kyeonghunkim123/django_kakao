# Generated by Django 4.2.1 on 2023-09-15 14:21

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('accom_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('contenttypeid', models.IntegerField(blank=True, null=True)),
                ('tourapi_contentid', models.IntegerField(blank=True, null=True)),
                ('accom_name', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('mapx', models.FloatField(blank=True, null=True)),
                ('mapy', models.FloatField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('tel', models.CharField(blank=True, max_length=100, null=True)),
                ('cat1', models.CharField(blank=True, max_length=255, null=True)),
                ('cat2', models.CharField(blank=True, max_length=255, null=True)),
                ('cat3', models.CharField(blank=True, max_length=255, null=True)),
                ('check_in_time', models.CharField(blank=True, max_length=255, null=True)),
                ('check_out_time', models.CharField(blank=True, max_length=255, null=True)),
                ('homepage', models.CharField(blank=True, max_length=255, null=True)),
                ('parking', models.CharField(blank=True, max_length=255, null=True)),
                ('subfacility', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Accommodation',
            },
        ),
        migrations.CreateModel(
            name='PlaceInfo',
            fields=[
                ('place_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('contenttypeid', models.IntegerField(blank=True, null=True)),
                ('tourapi_contentid', models.IntegerField(blank=True, null=True)),
                ('place_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('mapx', models.FloatField(blank=True, null=True)),
                ('mapy', models.FloatField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('tel', models.CharField(blank=True, max_length=100, null=True)),
                ('cat1', models.CharField(blank=True, max_length=255, null=True)),
                ('cat2', models.CharField(blank=True, max_length=255, null=True)),
                ('cat3', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('overview', models.CharField(blank=True, max_length=5000, null=True)),
                ('recommender_src', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PlaceInfo',
            },
        ),
        migrations.CreateModel(
            name='PlaceStatus',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('check_time', models.DateTimeField(null=True)),
                ('post_cnt', models.IntegerField(null=True)),
                ('congestion', models.BooleanField(default=False)),
                ('congestion_cnt', models.IntegerField(null=True)),
                ('temp_closure', models.BooleanField(default=False)),
                ('temp_closure_cnt', models.IntegerField(null=True)),
                ('weather_etc', models.BooleanField(default=False)),
                ('weather_etc_cnt', models.IntegerField(null=True)),
                ('weather_heat', models.BooleanField(default=False)),
                ('weather_heat_cnt', models.IntegerField(null=True)),
                ('weather_rain', models.BooleanField(default=False)),
                ('weather_rain_cnt', models.IntegerField(null=True)),
                ('weather_snow', models.BooleanField(default=False)),
                ('weather_snow_cnt', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'PlaceStatus',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restro_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('business_code', models.IntegerField(blank=True, null=True)),
                ('localdata_no', models.CharField(blank=True, max_length=500, null=True)),
                ('restro_name', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('road_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('mapx', models.FloatField(blank=True, null=True)),
                ('mapy', models.FloatField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('tel', models.CharField(blank=True, max_length=255, null=True)),
                ('cat', models.CharField(blank=True, max_length=255, null=True)),
                ('opening_hour', models.CharField(blank=True, max_length=1000, null=True)),
                ('homepage', models.CharField(blank=True, max_length=500, null=True)),
                ('external_link', models.CharField(blank=True, max_length=500, null=True)),
                ('zzinview_id', models.IntegerField(blank=True, null=True)),
                ('zzinview_score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Restaurant',
            },
        ),
        migrations.CreateModel(
            name='RestroStatus',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('check_time', models.DateTimeField(null=True)),
                ('post_cnt', models.IntegerField(null=True)),
                ('congestion', models.CharField(max_length=255, null=True)),
                ('congestion_cnt', models.IntegerField(null=True)),
                ('temp_closure', models.CharField(max_length=255, null=True)),
                ('temp_closure_cnt', models.IntegerField(null=True)),
                ('weather_etc', models.BooleanField(default=False)),
                ('weather_etc_cnt', models.IntegerField(null=True)),
                ('weather_heat', models.BooleanField(default=False)),
                ('weather_heat_cnt', models.IntegerField(null=True)),
                ('weather_rain', models.BooleanField(default=False)),
                ('weather_rain_cnt', models.IntegerField(null=True)),
                ('weather_snow', models.BooleanField(default=False)),
                ('weather_snow_cnt', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'RestroStatus',
            },
        ),
        migrations.CreateModel(
            name='ScheduleInfo',
            fields=[
                ('skd_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('skd_name', models.CharField(max_length=500)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('companion', models.IntegerField()),
                ('theme', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=66, null=True, size=None)),
                ('transport_type', models.IntegerField()),
            ],
            options={
                'db_table': 'ScheduleInfo',
            },
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('place_name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('mapx', models.FloatField()),
                ('mapy', models.FloatField()),
                ('additional_values', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Terminal',
            },
        ),
        migrations.CreateModel(
            name='AccomInfoNaver',
            fields=[
                ('accom', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schedule.accommodation')),
                ('naver_id', models.CharField(max_length=500)),
                ('cat', models.CharField(blank=True, max_length=500, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('road_address', models.CharField(blank=True, max_length=500, null=True)),
                ('opening_hour', models.JSONField(blank=True, null=True)),
                ('tel', models.CharField(blank=True, max_length=500, null=True)),
                ('use_fee', models.JSONField(blank=True, null=True)),
                ('chk_facilities', models.CharField(blank=True, max_length=500, null=True)),
                ('homepage', models.JSONField(blank=True, null=True)),
                ('overview', models.CharField(blank=True, max_length=5000, null=True)),
                ('booking_url', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'AccomInfoNaver',
            },
        ),
        migrations.CreateModel(
            name='PlaceInfoDetail',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schedule.placeinfo')),
                ('accom_count', models.CharField(blank=True, max_length=500, null=True)),
                ('chk_baby_carriage', models.CharField(blank=True, max_length=500, null=True)),
                ('chk_credit_card', models.CharField(blank=True, max_length=500, null=True)),
                ('chk_pet', models.CharField(blank=True, max_length=500, null=True)),
                ('discount_info', models.CharField(blank=True, max_length=500, null=True)),
                ('exp_age_range', models.CharField(blank=True, max_length=500, null=True)),
                ('exp_guide', models.CharField(blank=True, max_length=1500, null=True)),
                ('info_center', models.CharField(blank=True, max_length=500, null=True)),
                ('parking', models.CharField(blank=True, max_length=500, null=True)),
                ('parking_fee', models.CharField(blank=True, max_length=500, null=True)),
                ('rest_date', models.CharField(blank=True, max_length=500, null=True)),
                ('spend_time', models.CharField(blank=True, max_length=500, null=True)),
                ('use_fee', models.CharField(blank=True, max_length=1000, null=True)),
                ('use_time', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'PlaceInfoDetail',
            },
        ),
        migrations.CreateModel(
            name='PlaceInfoNaver',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schedule.placeinfo')),
                ('naver_id', models.CharField(max_length=500)),
                ('cat', models.CharField(blank=True, max_length=500, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('road_address', models.CharField(blank=True, max_length=500, null=True)),
                ('opening_hour', models.CharField(blank=True, max_length=500, null=True)),
                ('tel', models.CharField(blank=True, max_length=500, null=True)),
                ('use_fee', models.JSONField(blank=True, null=True)),
                ('chk_parking', models.IntegerField(blank=True, null=True)),
                ('chk_booking', models.IntegerField(blank=True, null=True)),
                ('chk_wifi', models.IntegerField(blank=True, null=True)),
                ('chk_facilities', models.CharField(blank=True, max_length=500, null=True)),
                ('hashtag', models.CharField(blank=True, max_length=500, null=True)),
                ('homepage', models.JSONField(blank=True, null=True)),
                ('overview', models.CharField(blank=True, max_length=5000, null=True)),
                ('overview_href', models.CharField(blank=True, max_length=500, null=True)),
                ('chk_pet', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PlaceInfoNaver',
            },
        ),
        migrations.CreateModel(
            name='RestroInfoNaver',
            fields=[
                ('restro', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schedule.restaurant')),
                ('naver_id', models.CharField(max_length=500)),
                ('cat', models.CharField(blank=True, max_length=500, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('road_address', models.CharField(blank=True, max_length=500, null=True)),
                ('opening_hour', models.CharField(blank=True, max_length=1000, null=True)),
                ('tel', models.CharField(blank=True, max_length=500, null=True)),
                ('chk_parking', models.IntegerField(blank=True, null=True)),
                ('chk_booking', models.IntegerField(blank=True, null=True)),
                ('chk_wifi', models.IntegerField(blank=True, null=True)),
                ('chk_takeout', models.IntegerField(blank=True, null=True)),
                ('chk_group_seat', models.IntegerField(blank=True, null=True)),
                ('chk_facilities', models.CharField(blank=True, max_length=500, null=True)),
                ('menu', models.JSONField(blank=True, null=True)),
                ('homepage', models.JSONField(blank=True, null=True)),
                ('overview', models.CharField(blank=True, max_length=5000, null=True)),
                ('chk_pet', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'RestroInfoNaver',
            },
        ),
        migrations.CreateModel(
            name='SchedulePlace',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('destination_order_num', models.IntegerField(null=True)),
                ('accom_id', models.ForeignKey(blank=True, db_column='accom_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.accommodation')),
                ('place_id', models.ForeignKey(blank=True, db_column='place_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.placeinfo')),
                ('restro_id', models.ForeignKey(blank=True, db_column='restro_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.restaurant')),
                ('skd_id', models.ForeignKey(db_column='skd_id', on_delete=django.db.models.deletion.CASCADE, to='schedule.scheduleinfo')),
                ('terminal_id', models.ForeignKey(blank=True, db_column='id', db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.terminal')),
            ],
            options={
                'db_table': 'SchedulePlace',
            },
        ),
    ]
