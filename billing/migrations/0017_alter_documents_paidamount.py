# Generated by Django 4.0.5 on 2022-06-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0016_documents_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='paidamount',
            field=models.CharField(default='0', max_length=100),
        ),
    ]