# Generated by Django 4.2.7 on 2023-12-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_description_alter_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='description',
            field=models.TextField(blank=True, default='', max_length=600, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='regular', max_length=100),
        ),
    ]