# Generated by Django 4.1 on 2022-08-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_info_pregnancies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='blood_pressure',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='bmi',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='dpf',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='glucose',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='insulin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='result',
            field=models.CharField(choices=[('0', 'Negative'), ('1', 'Positive')], max_length=10),
        ),
        migrations.AlterField(
            model_name='info',
            name='skin_thickness',
            field=models.FloatField(),
        ),
    ]
