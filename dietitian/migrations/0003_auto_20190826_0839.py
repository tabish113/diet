# Generated by Django 2.2.4 on 2019-08-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietitian', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.FileField(default='', upload_to='blog'),
        ),
    ]
