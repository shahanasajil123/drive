from django.db import models
from User.models import User
# Create your models here.
class Secondarynumber(models.Model):
    secondary_number_id = models.AutoField(db_column='secondary number_id', primary_key=True)  # Field renamed to remove unsuitable characters.
    number = models.CharField(max_length=20)
   # user_id = models.IntegerField()
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'secondarynumber'
