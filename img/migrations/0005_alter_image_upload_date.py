# Generated by Django 5.0.1 on 2024-01-09 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0004_alter_image_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
