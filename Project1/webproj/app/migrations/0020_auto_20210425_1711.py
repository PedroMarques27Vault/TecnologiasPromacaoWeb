# Generated by Django 3.2 on 2021-04-25 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20210425_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.FloatField(default=0.0)),
                ('user_id', models.CharField(default=0, max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentDate',
            field=models.DateField(default=datetime.datetime(2021, 4, 25, 17, 11, 43, 965710)),
        ),
    ]
