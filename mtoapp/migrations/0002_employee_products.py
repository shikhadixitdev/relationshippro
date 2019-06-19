# Generated by Django 2.2.2 on 2019-06-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100)),
                ('emploc', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pcost', models.IntegerField()),
                ('employee', models.ManyToManyField(to='mtoapp.Employee')),
            ],
        ),
    ]