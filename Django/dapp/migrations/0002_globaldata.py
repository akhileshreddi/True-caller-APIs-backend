# Generated by Django 4.0.4 on 2023-06-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=10)),
            ],
        ),
    ]