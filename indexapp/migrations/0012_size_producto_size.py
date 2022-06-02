# Generated by Django 4.0.4 on 2022-05-31 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0011_categoria_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.producto')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.size')),
            ],
        ),
    ]
