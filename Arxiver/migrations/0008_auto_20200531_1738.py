# Generated by Django 3.0.3 on 2020-05-31 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arxiver', '0007_auto_20200516_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='headImg',
            field=models.ImageField(default='img/default.jpg', upload_to='img/'),
        ),
    ]
