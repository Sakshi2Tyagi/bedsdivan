# Generated by Django 3.0.8 on 2021-04-01 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('currencies', '0006_increase_name_max_length'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/users/')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='currencies.Currency')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
