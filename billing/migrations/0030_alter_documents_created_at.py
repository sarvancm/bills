# Generated by Django 4.0.5 on 2022-06-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0029_alter_documentamount_duedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]