# Generated by Django 4.2.2 on 2023-07-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=400)),
                ('password1', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
            ],
        ),
    ]
