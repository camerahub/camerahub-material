# Generated by Django 4.0.4 on 2022-05-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name'], 'verbose_name_plural': 'manufacturers'},
        ),
        migrations.AddIndex(
            model_name='manufacturer',
            index=models.Index(fields=['slug'], name='schema_manu_slug_fd5a47_idx'),
        ),
        migrations.AddIndex(
            model_name='manufacturer',
            index=models.Index(fields=['country', 'country'], name='schema_manu_country_abce90_idx'),
        ),
    ]
