# Generated by Django 4.2.1 on 2023-09-15 14:21

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SNSLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'SNSLikes',
            },
        ),
        migrations.CreateModel(
            name='SNSPost',
            fields=[
                ('post_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=10000, null=True)),
                ('images', django_mysql.models.ListCharField(models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=1000), max_length=1000, null=True, size=None)),
                ('posting_date', models.DateTimeField(null=True)),
                ('likes', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'SNSPost',
            },
        ),
    ]
