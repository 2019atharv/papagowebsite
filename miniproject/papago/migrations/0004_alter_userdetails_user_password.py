# Generated by Django 3.2.8 on 2021-11-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papago', '0003_auto_20211103_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='user_password',
            field=models.TextField(),
        ),
    ]