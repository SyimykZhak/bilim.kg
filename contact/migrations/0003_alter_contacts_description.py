# Generated by Django 4.0.2 on 2022-03-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contacts_password_contacts_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание'),
        ),
    ]