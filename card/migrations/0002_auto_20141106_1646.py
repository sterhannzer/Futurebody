# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        (b'card', b'0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name=b'card',
            name=b'name',
            field=models.CharField(default=b'name', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name=b'card',
            name=b'date_of_finish',
            field=models.DateField(default=datetime.datetime(2014, 12, 6, 16, 45, 35, 684106)),
        ),
        migrations.AlterField(
            model_name=b'card',
            name=b'type',
            field=models.CharField(max_length=100, choices=[(b'OPEN', b'Open'), (b'OPEN_16', b'Open do 16')]),
        ),
        migrations.AlterField(
            model_name=b'card',
            name=b'date_of_purchase',
            field=models.DateField(default=datetime.datetime(2014, 11, 6, 16, 45, 35, 684072)),
        ),
    ]
