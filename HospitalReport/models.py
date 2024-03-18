from django.db import models

# Create your models here.
class Hospitalreport(models.Model):
    hospital_report_id = models.AutoField(db_column='hospital report_id', primary_key=True)  # Field renamed to remove unsuitable characters.
    report = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'hospitalreport'

