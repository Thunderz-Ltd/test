# Generated by Django 3.2.3 on 2021-06-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_userprofile_userslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='preferredmaxrent',
            field=models.IntegerField(null=True),
        ),
    ]