# Generated by Django 4.0.5 on 2022-07-24 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping_cart', '0004_lista_productos_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=30)),
                ('num_exterior', models.CharField(max_length=20)),
                ('num_tel', models.IntegerField()),
                ('domicio', models.CharField(max_length=255)),
                ('cp', models.IntegerField()),
                ('intrucciones', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shopping_cart.direccion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lista_productos',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping_cart.ticket'),
        ),
    ]