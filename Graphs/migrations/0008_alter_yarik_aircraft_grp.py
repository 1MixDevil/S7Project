# Generated by Django 4.1.2 on 2022-10-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Graphs', '0007_alter_yarik_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yarik',
            name='aircraft_grp',
            field=models.CharField(blank=True, choices=[('A320-214', 'A320-214'), ('EMBRAER 170-100', 'EMBRAER 170-100'), ('B737-83N', 'B737-83N'), ('B737-8LP', 'B737-8LP'), ('A321-211', 'A321-211'), ('B737-8Q8', 'B737-8Q8'), ('B737-8ZS', 'B737-8ZS'), ('B737-8GJ', 'B737-8GJ'), ('B737-BCF', 'B737-BCF')], max_length=15, null=True, verbose_name='aircraft grp'),
        ),
    ]