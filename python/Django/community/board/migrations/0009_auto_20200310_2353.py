# Generated by Django 3.0.3 on 2020-03-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20200310_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='description',
            field=models.TextField(verbose_name='내용'),
        ),
    ]
