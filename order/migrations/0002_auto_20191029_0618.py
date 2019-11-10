# Generated by Django 2.2.6 on 2019-10-29 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
