# Generated by Django 4.0.2 on 2022-03-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(default='empty', upload_to='books/'),
        ),
    ]
