# Generated by Django 4.0.5 on 2022-09-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0009_alter_contributor_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='user_id',
            field=models.IntegerField(verbose_name='contributors'),
        ),
    ]
