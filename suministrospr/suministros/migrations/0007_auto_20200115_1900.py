# Generated by Django 2.2.9 on 2020-01-15 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("suministros", "0006_auto_20200115_1746"),
    ]

    operations = [
        migrations.RemoveField(model_name="suministro", name="created_date",),
        migrations.RemoveField(model_name="suministro", name="modified_date",),
    ]
