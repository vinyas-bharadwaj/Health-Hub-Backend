# Generated by Django 5.1.3 on 2024-11-15 14:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='reports/')),
                ('patients', models.ManyToManyField(related_name='reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
