# Generated by Django 2.2.14 on 2021-03-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210225_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]