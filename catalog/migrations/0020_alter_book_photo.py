# Generated by Django 4.0.2 on 2022-04-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, default='no image', upload_to='books/'),
        ),
    ]