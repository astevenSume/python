# Generated by Django 2.0.4 on 2018-05-06 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180506_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='category',
            new_name='category_id',
        ),
    ]