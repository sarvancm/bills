# Generated by Django 4.0.5 on 2022-06-15 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_documents_checkleafcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='file',
        ),
        migrations.AlterField(
            model_name='documents',
            name='additionaldocumentsname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='DocumentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='mydocs/')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.documents')),
            ],
        ),
    ]
