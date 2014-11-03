# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'users', b'0002_auto_20141028_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name=b'user',
            name=b'barcode',
            field=models.IntegerField(),
        ),
    ]
