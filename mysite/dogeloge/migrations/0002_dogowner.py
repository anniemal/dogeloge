# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogeloge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogOwner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('emergency_contact', models.CharField(max_length=64)),
                ('contact_phone', models.CharField(max_length=64)),
                ('vet_name', models.CharField(max_length=64)),
                ('vet_phone', models.CharField(max_length=64)),
                ('dogwalker', models.ForeignKey(to='dogeloge.DogWalker')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
