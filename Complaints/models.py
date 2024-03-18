from django.db import models
from User.models import User
from Police.models import Police
# Create your models here.

class Complaints(models.Model):
    complains_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    # user_id = models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
   # police_id = models.IntegerField()
    Police=models.ForeignKey(Police,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=45)
    reply = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'complaints'
