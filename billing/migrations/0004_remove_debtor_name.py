# Generated by Django 4.0.5 on 2022-06-13 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_debtor_address_debtor_email_debtor_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debtor',
            name='name',
        ),
    ]