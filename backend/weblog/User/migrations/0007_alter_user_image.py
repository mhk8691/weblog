# Generated by Django 5.0 on 2024-04-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_user_image_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='images/User/UserDefult.png', upload_to='images/User/'),
        ),
    ]
