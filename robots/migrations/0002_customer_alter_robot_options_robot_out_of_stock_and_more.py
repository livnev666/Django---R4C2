# Generated by Django 4.2.6 on 2023-10-08 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
            },
        ),
        migrations.AlterModelOptions(
            name='robot',
            options={'verbose_name': 'Робот', 'verbose_name_plural': 'Роботы'},
        ),
        migrations.AddField(
            model_name='robot',
            name='out_of_stock',
            field=models.BooleanField(default=False, verbose_name='Нет в наличии'),
        ),
        migrations.AddField(
            model_name='robot',
            name='stock',
            field=models.IntegerField(default=1, verbose_name='Наличие на складе'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='model',
            field=models.CharField(max_length=2, verbose_name='модель'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='serial',
            field=models.CharField(max_length=5, verbose_name='серия'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='version',
            field=models.CharField(max_length=2, verbose_name='версия'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robot_serial', models.CharField(max_length=5, verbose_name='серийный номер робота')),
                ('model', models.CharField(max_length=2, null=True, verbose_name='модель')),
                ('version', models.CharField(max_length=2, null=True, verbose_name='версия')),
                ('customer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='robots.customer', verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='robot',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='robots.customer', verbose_name='Заказчик'),
        ),
        migrations.AddField(
            model_name='robot',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='robots.order', verbose_name='Заказ'),
        ),
    ]
