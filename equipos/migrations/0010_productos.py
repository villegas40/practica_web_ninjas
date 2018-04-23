# Generated by Django 2.0.1 on 2018-04-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0009_perfil_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cantitad', models.IntegerField()),
            ],
        ),
    ]