# Generated by Django 3.0.3 on 2020-03-10 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_email'),
        ('board', '0003_auto_20200310_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='writer',
            field=models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='사용자'),
        ),
    ]
