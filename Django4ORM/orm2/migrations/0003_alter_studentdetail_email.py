# Generated by Django 3.2.16 on 2022-12-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm2', '0002_auto_20221205_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='学生邮箱'),
        ),
    ]