from django.db import models


class UserData(models.Model):
    ip = models.CharField(max_length=200)
    is_routable = models.BooleanField()

    class Meta:
        db_table = 'users_data'