# Generated by Django 4.1 on 2022-08-27 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_info_pregnancies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='pregnancies',
            field=models.IntegerField(blank=True),
        ),
    ]
