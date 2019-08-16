# Generated by Django 2.2.4 on 2019-08-16 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nearest_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_jobs', to='jobs.Job')),
            ],
        ),
    ]
