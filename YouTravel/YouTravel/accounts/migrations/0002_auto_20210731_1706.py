# Generated by Django 3.2.5 on 2021-07-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelprofile',
            name='about_me',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='travelprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]