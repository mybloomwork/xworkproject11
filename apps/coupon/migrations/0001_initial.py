# Generated by Django 3.0.9 on 2020-08-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('value', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('num_available', models.IntegerField(default=1)),
                ('num_used', models.IntegerField(default=0)),
            ],
        ),
    ]
