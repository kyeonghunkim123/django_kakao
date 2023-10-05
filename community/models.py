from django.db import models
from django_mysql.models import ListCharField


# Create your models here.
class SNSPost(models.Model):
    post_id = models.CharField(max_length=255, primary_key=True)
    user_id = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE, db_column='user_id', null=True,
                                db_constraint=False)
    place_id = models.ForeignKey('schedule.PlaceInfo', on_delete=models.CASCADE, db_column='place_id', null=True,
                                 db_constraint=False)
    restro_id = models.ForeignKey('schedule.Restaurant', on_delete=models.CASCADE, db_column='restro_id', null=True,
                                  db_constraint=False)
    accom_id = models.ForeignKey('schedule.Accommodation', on_delete=models.CASCADE, db_column='accom_id', null=True,
                                 db_constraint=False)
    content = models.CharField(max_length=10000, null=True)
    images = ListCharField(models.CharField(max_length=1000, db_collation='utf8mb3_general_ci', blank=True), null=True,
                           max_length=1000)
    posting_date = models.DateTimeField(null=True)
    likes = models.IntegerField(null=True)

    class Meta:
        db_table = 'SNSPost'

    def save(self, *args, **kwargs):
        if not self.post_id:
            # 새로운 객체인 경우에만 기본 키 생성
            user_id = self.user_id.user_id
            id_number = SNSPost.objects.filter(user_id=self.user_id).count() + 1
            padding_length = 6
            post_id = f'{str(user_id)}-{id_number:0{padding_length}}'
            self.post_id = post_id
        super().save(*args, **kwargs)


class SNSLikes(models.Model):
    post_id = models.ForeignKey('SNSPost', on_delete=models.CASCADE, db_column='post_id')
    user_id = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE, db_column='user_id', null=True)

    class Meta:
        db_table = 'SNSLikes'
        unique_together = [('post_id', 'user_id')]


