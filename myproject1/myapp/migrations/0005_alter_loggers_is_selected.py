# Generated by Django 4.1.5 on 2024-01-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_loggers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggers',
            name='is_selected',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]