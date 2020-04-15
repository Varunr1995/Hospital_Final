# Generated by Django 2.2.11 on 2020-04-15 07:50

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointmentmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Third Gender')], max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=12)),
                ('email_id', models.EmailField(max_length=250)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('department', models.CharField(choices=[('1', '----------'), ('2', 'Cardiology'), ('3', 'Neurology'), ('4', 'Orthopedics'), ('5', 'Dermatology'), ('6', 'Nephronology'), ('7', 'Gynacologist')], max_length=20)),
                ('reports', models.ImageField(upload_to='reports')),
            ],
        ),
    ]
