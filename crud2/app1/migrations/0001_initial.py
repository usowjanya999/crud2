# Generated by Django 3.0.5 on 2020-08-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('salary', models.FloatField()),
            ],
        ),
    ]
