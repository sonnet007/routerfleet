# Generated by Django 5.0.3 on 2024-04-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router_manager', '0015_alter_routerstatus_status_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='router',
            name='port',
            field=models.IntegerField(default=22),
        ),
    ]