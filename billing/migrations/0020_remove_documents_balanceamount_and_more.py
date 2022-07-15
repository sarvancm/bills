# Generated by Django 4.0.5 on 2022-06-20 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0019_documents_balanceamount_documents_paidamount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='balanceamount',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='paidamount',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='totalamount',
        ),
        migrations.AlterField(
            model_name='documents',
            name='debtor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='billing.debtor'),
        ),
        migrations.AlterField(
            model_name='intrestamount',
            name='amount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.debtor'),
        ),
        migrations.CreateModel(
            name='DocumentAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalamount', models.IntegerField(blank=True, default=0, null=True)),
                ('percentage', models.CharField(blank=True, max_length=100)),
                ('paidamount', models.IntegerField(blank=True, default=0, null=True)),
                ('balanceamount', models.IntegerField(blank=True, default=0, null=True)),
                ('duedate', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('debtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.debtor')),
            ],
        ),
    ]