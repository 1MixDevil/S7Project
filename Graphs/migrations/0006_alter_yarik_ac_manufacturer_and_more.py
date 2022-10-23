# Generated by Django 4.1.2 on 2022-10-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Graphs', '0005_alter_yarik_engine_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yarik',
            name='ac_manufacturer',
            field=models.CharField(blank=True, choices=[('AIRBUS', 'AIRBUS'), ('EMBRAER', 'EMBRAER'), ('BOEING', 'BOEING')], max_length=15, null=True, verbose_name='ac manufacturer'),
        ),
        migrations.AlterField(
            model_name='yarik',
            name='aircraft_family',
            field=models.CharField(blank=True, choices=[('A320', 'A320'), ('EMBRAER RJ', 'EMBRAER RJ'), ('B737', 'B737')], max_length=15, null=True, verbose_name='aircraft family'),
        ),
        migrations.AlterField(
            model_name='yarik',
            name='aircraft_grp',
            field=models.CharField(blank=True, choices=[('A320-214', 'A320-214'), ('EMBRAER-170-100', 'EMBRAER 170-100'), ('B737-83N', 'B737-83N'), ('B737-8LP', 'B737-8LP'), ('A321-211', 'A321-211'), ('B737-8Q8', 'B737-8Q8'), ('B737-8ZS', 'B737-8ZS'), ('B737-8GJ', 'B737-8GJ'), ('B737-BCF', 'B737-BCF')], max_length=15, null=True, verbose_name='aircraft grp'),
        ),
        migrations.AlterField(
            model_name='yarik',
            name='aircraft_type',
            field=models.CharField(blank=True, choices=[('A320-200', 'A320-200'), ('ERJ170', 'ERJ170'), ('B737-800', 'B737-800'), ('A321-200', 'A321-200')], max_length=15, null=True, verbose_name='aircraft type'),
        ),
        migrations.AlterField(
            model_name='yarik',
            name='engine_family',
            field=models.CharField(blank=True, choices=[('CFM56-5B', 'CFM56-5B'), ('CF34-8E', 'CF34-8E'), ('CFM56-7', 'CFM56-7')], max_length=15, null=True, verbose_name='engine family'),
        ),
        migrations.AlterField(
            model_name='yarik',
            name='flight_phase',
            field=models.CharField(choices=[('TAKEOFF', 'TAKEOFF'), ('CRUISE', 'CRUISE')], max_length=15, verbose_name='flight_phase'),
        ),
        migrations.AlterField(
            model_name='yarik',
            name='manufacturer',
            field=models.CharField(blank=True, choices=[('CFM', 'CFM INTERNATIONAL'), ('GE_AIR', 'GE AIRCRAFT ENGINES')], max_length=15, null=True, verbose_name='manufacturer'),
        ),
    ]
