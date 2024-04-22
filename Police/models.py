from django.db import models

# Create your models here.
class Police(models.Model):
    police_id = models.AutoField(primary_key=True)
    police_name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    # username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'police'

