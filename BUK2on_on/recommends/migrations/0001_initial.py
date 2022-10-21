# Generated by Django 3.2.13 on 2022-10-21 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=200)),
                ('stars', models.IntegerField()),
                ('bestMenu', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=1000)),
            ],
        ),
    ]
