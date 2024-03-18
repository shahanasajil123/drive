from django.db import models
from Police.models import Police
# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
   # police_id = models.IntegerField()
    Police=models.ForeignKey(Police,on_delete=models.CASCADE)
    notification = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'notification'
