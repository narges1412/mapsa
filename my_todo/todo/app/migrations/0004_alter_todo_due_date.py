# Generated by Django 4.0.4 on 2022-05-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_profile_password_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
