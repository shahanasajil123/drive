from django.db import models

# Create your models here.
class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    hospital_name = models.CharField(db_column='hospital name', max_length=45)  # Field renamed to remove unsuitable characters.
    address = models.CharField(max_length=45)
    contact_number = models.IntegerField(db_column='contact number')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'hospital'
