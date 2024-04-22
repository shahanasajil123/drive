from django.db import models
from User.models import User

# Create your models here.
class Drowsinessalert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    alert = models.CharField(max_length=45)
    # user_id = models.IntegerField(blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'drowsinessalert'
