# Generated by Django 3.0.3 on 2020-03-02 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200303_0204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '장고 사용자', 'verbose_name_plural': '장고 사용자'},
        ),
    ]
