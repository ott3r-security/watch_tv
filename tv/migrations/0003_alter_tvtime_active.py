# Generated by Django 4.2 on 2023-04-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0002_alter_tvtime_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvtime',
            name='active',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], default='y', max_length=5),
        ),
    ]