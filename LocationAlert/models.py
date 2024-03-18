from django.db import models
from  User.models import User
# Create your models here.
class Locationalert(models.Model):
    location_alert_id = models.AutoField(db_column='location alert_id', primary_key=True)  # Field renamed to remove unsuitable characters.
   # user_id = models.IntegerField()
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    alert = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'locationalert'
