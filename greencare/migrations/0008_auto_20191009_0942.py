# Generated by Django 2.2.4 on 2019-10-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greencare', '0007_auto_20191009_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whychooseouragroservices',
            name='picture',
            field=models.ImageField(help_text='preferably 640x420', max_length=1000, upload_to='why-choose-us/', verbose_name='Picture'),
        ),
    ]
