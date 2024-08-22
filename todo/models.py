from django.db import models

# Create your models here.
class Prospect(models.Model):
    id = models.CharField(primary_key=True,max_length=30)
    form_id = models.CharField(max_length=30)
    submission_id = models.CharField(max_length=30)
    field_name = models.CharField(max_length=30)
    field_value = models.CharField(max_length=30)
    created_at = models.CharField(max_length=30)