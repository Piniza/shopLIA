# Generated by Django 4.1.7 on 2023-11-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_produit_date_alter_produit_id_alter_produit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
