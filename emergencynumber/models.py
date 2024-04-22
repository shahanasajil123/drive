from django.db import models

# Create your models here.
class Emergencynumber(models.Model):
    emergency_number_id = models.AutoField(primary_key=True)  # Field renamed to remove unsuitable characters.
    emergency_no = models.IntegerField()  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'emergencynumber'
