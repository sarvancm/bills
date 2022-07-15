# Generated by Django 4.0.5 on 2022-06-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_remove_documents_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='percentage',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='documents',
            name='totalamount',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='documents',
            name='additionaldocumentsname',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
    ]