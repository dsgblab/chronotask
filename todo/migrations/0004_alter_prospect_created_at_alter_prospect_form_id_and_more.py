# Generated by Django 5.0.8 on 2024-08-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_prospect_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='form_id',
            field=models.SmallIntegerField(max_length=60),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='submission_id',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='uuid',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
