# Generated by Django 4.0.2 on 2022-04-05 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.date(2022, 4, 5)),
        ),
    ]
