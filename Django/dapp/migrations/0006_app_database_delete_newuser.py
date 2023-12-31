# Generated by Django 4.0.4 on 2023-06-11 13:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapp', '0005_newuser_delete_olduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='app_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
                ('password', models.CharField(max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='NewUser',
        ),
    ]
