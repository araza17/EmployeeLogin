# Generated by Django 2.0.2 on 2018-03-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(blank=True, default='', max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.TextField(blank=True, default='', max_length=200)),
                ('worktype', models.CharField(max_length=200)),
                ('hourly_rate', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
