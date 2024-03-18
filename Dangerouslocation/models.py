from django.db import models

# Create your models here.
class DangerousLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'dangerous_location'
