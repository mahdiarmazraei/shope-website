# Generated by Django 4.2.4 on 2023-11-20 11:46

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.IntegerField()),
                ('username', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('is_active', models.IntegerField(null=True)),
            ],
            managers=[
                ('empAuth_object', django.db.models.manager.Manager()),
            ],
        ),
    ]
