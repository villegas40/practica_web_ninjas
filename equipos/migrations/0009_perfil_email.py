# Generated by Django 2.0.1 on 2018-03-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0008_auto_20180304_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
