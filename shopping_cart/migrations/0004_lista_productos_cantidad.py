# Generated by Django 4.0.5 on 2022-07-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista_productos',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
    ]
