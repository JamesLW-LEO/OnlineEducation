# Generated by Django 2.2.4 on 2019-08-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20190822_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(null=True, upload_to='org/%Y%m', verbose_name='封面图'),
        ),
    ]