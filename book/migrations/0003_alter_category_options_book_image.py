# Generated by Django 4.2.3 on 2023-07-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Catgories'},
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='test.png', upload_to='book_images'),
            preserve_default=False,
        ),
    ]
