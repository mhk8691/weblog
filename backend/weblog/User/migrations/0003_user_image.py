# Generated by Django 5.0 on 2024-04-28 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_remove_user_tyoe_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
