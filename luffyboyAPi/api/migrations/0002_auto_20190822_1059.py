# Generated by Django 2.1.1 on 2019-08-22 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='beili',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='money_equivalent_value',
            field=models.FloatField(blank=True, null=True, verbose_name='等值货币'),
        ),
    ]
