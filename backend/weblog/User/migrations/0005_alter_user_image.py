# Generated by Django 5.0 on 2024-04-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='images/User/'),
        ),
    ]