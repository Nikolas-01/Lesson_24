# Generated by Django 3.0.5 on 2020-05-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0007_auto_20200518_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyticsinfo',
            name='poet_dictionary_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]