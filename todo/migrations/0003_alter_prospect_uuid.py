# Generated by Django 5.0.8 on 2024-08-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_id_prospect_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='uuid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
