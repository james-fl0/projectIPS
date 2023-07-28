# Generated by Django 4.2.3 on 2023-07-27 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appMedicalHistory', '0001_initial'),
        ('appPatients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastHistory',
            fields=[
                ('pastHistoryID', models.AutoField(primary_key=True, serialize=False)),
                ('ingressDate', models.DateTimeField()),
                ('file', models.BinaryField()),
                ('medicalHistoryID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appMedicalHistory.medicalhistory')),
                ('patientID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPatients.patients')),
            ],
        ),
    ]
