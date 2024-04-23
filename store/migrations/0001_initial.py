# Generated by Django 5.0.4 on 2024-04-23 17:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=1000)),
                ('product_description', models.CharField(max_length=10000)),
                ('product_price', models.IntegerField()),
                ('product_discount', models.IntegerField(default=0, null=True)),
                ('product_manufacturing_date', models.DateTimeField()),
                ('product_upload_time', models.DateTimeField(default=None)),
                ('product_cover_photo', models.ImageField(upload_to='')),
                ('product_extra_photos', models.ImageField(null=True, upload_to='')),
                ('product_category', models.CharField(default=None, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
