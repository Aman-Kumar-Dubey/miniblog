# Generated by Django 4.2.3 on 2023-08-28 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_post_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
