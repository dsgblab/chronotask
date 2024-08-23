from django.db import models

# Create your models here.
class Prospect(models.Model):
    uuid = models.BigIntegerField(primary_key=True)
    form_id = models.SmallIntegerField()
    submission_id = models.IntegerField()
    field_name = models.CharField(max_length=30)
    field_value = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now=False, auto_now_add=False)