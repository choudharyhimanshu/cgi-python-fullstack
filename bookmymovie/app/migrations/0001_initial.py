# Generated by Django 3.0.3 on 2020-02-09 19:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SeatInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=16)),
                ('num_seats', models.IntegerField(blank=True, default=0)),
                ('aisle_seats', models.TextField(blank=True, default='', validators=[django.core.validators.int_list_validator])),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_info', to='app.Screen')),
            ],
            options={
                'ordering': ['row'],
            },
        ),
    ]
