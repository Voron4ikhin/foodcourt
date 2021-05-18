# Generated by Django 3.2.3 on 2021-05-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfc',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userfc',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userfc',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6),
        ),
    ]
