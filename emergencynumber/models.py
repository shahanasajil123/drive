from django.db import models

# Create your models here.
class Emergencynumber(models.Model):
    emergency_number_id = models.AutoField(db_column='emergency number_id', primary_key=True)  # Field renamed to remove unsuitable characters.
    emergency_no = models.IntegerField(db_column='emergency no')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'emergencynumber'
