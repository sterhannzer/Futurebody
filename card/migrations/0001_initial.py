# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name=b'Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'type', models.CharField(max_length=64)),
                (b'price', models.IntegerField()),
                (b'date_of_purchase', models.DateField()),
                (b'date_of_finish', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
