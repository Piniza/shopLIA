# Generated by Django 4.1.7 on 2023-11-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produit',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
