# Generated by Django 3.2.3 on 2021-06-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_product_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=255)),
                ('dateofbirth', models.CharField(max_length=255)),
            ],
        ),
    ]
