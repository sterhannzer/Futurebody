# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'users', b'0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name=b'user',
            name=b'barcode',
            field=models.IntegerField(default=b'00001'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name=b'user',
            name=b'surname',
            field=models.CharField(default=b'surname', max_length=32),
            preserve_default=False,
        ),
    ]
