# Generated by Django 4.0.2 on 2022-03-27 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(default='empty', upload_to='{title}'),
        ),
    ]
