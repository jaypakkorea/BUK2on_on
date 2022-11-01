# Generated by Django 3.2.13 on 2022-11-01 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recommends.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('1', 'Seoul'), ('2', 'Busan'), ('3', 'etc.')], max_length=20)),
                ('adress', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=200)),
                ('stars', models.IntegerField()),
                ('bestMenu', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=1000)),
                ('mainImage', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=recommends.models.get_image_filename)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='recommends.restaurant')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
