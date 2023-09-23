# Generated by Django 4.2.4 on 2023-09-15 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='client_data')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
