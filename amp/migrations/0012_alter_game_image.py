# Generated by Django 4.2.16 on 2024-12-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amp', '0011_alter_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(default='static/cardgb.jpeg', upload_to=''),
        ),
    ]
