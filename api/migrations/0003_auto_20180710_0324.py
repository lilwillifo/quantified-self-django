# Generated by Django 2.0.7 on 2018-07-10 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_meal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
