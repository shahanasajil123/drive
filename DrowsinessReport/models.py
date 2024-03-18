from django.db import models

# Create your models here.
class Drowsinessreport(models.Model):
    drowsinessreportid = models.AutoField(primary_key=True)
    report = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'drowsinessreport'
