# Generated by Django 3.2.3 on 2021-07-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='image_url',
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
