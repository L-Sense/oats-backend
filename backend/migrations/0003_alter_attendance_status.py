# Generated by Django 3.2.7 on 2021-09-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210911_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal'), ('Leave', 'Leave')], default='Normal', max_length=100),
        ),
    ]
