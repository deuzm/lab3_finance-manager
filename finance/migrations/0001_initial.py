# Generated by Django 3.2.7 on 2021-09-21 16:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('amount', models.FloatField(validators=[django.core.validators.MaxValueValidator(999999999999999), django.core.validators.MinValueValidator(0)])),
                ('currency', models.CharField(choices=[('USD', 'United States Dollar'), ('EUR', 'Euro'), ('RUB', 'Russian Ruble')], default='USD', max_length=5)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.FloatField(validators=[django.core.validators.MaxValueValidator(999999999999999), django.core.validators.MinValueValidator(0)])),
                ('coef', models.FloatField(validators=[django.core.validators.MaxValueValidator(999999999999999), django.core.validators.MinValueValidator(0)])),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('from_balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_balance', to='finance.balance')),
                ('to_balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_balance', to='finance.balance')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.FloatField(validators=[django.core.validators.MaxValueValidator(999999999999999), django.core.validators.MinValueValidator(0)])),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.balance')),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.expense')),
            ],
        ),
    ]
