# Generated by Django 4.2.5 on 2023-10-02 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street', models.CharField(max_length=100, verbose_name='улица')),
                ('house_number', models.CharField(max_length=100, verbose_name='номер дома')),
                ('level', models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], verbose_name='звено сети')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street', models.CharField(max_length=100, verbose_name='улица')),
                ('house_number', models.CharField(max_length=100, verbose_name='номер дома')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('model', models.CharField(max_length=100, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='время создания')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.network', verbose_name='звено сети')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.AddField(
            model_name='network',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.supplier', verbose_name='поставщик'),
        ),
    ]
