from django.db import models

# Create your models here.
class Drowsinessalert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    alert = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'drowsinessalert'
