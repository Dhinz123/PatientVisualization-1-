# Generated by Django 4.1.6 on 2023-02-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_patientdata_jul_mood_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientdata',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='patientdata',
            old_name='name',
            new_name='Name',
        ),
        migrations.AlterField(
            model_name='collectivepatientdata',
            name='months_of_treatment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='collectivepatientdata',
            name='severity_rate',
            field=models.IntegerField(default=0),
        ),
    ]