# Generated by Django 4.0.4 on 2022-05-26 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_alter_manufacturer_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of this paper stock', max_length=45)),
                ('resin_coated', models.BooleanField(blank=True, help_text='Whether the paper is resin-coated', null=True)),
                ('colour', models.BooleanField(blank=True, help_text='Whether this is a colour paper', null=True)),
                ('finish', models.CharField(blank=True, choices=[('Matt', 'Matt'), ('Gloss', 'Gloss'), ('Satin', 'Satin'), ('Semi gloss', 'Semi gloss'), ('Pearl', 'Pearl'), ('Lustre', 'Lustre')], help_text='The finish of the paper surface', max_length=25, null=True)),
                ('manufacturer', models.ForeignKey(blank=True, help_text='Manufacturer of this paper stock', null=True, on_delete=django.db.models.deletion.CASCADE, to='schema.manufacturer')),
            ],
            options={
                'verbose_name_plural': 'paper stocks',
                'ordering': ['manufacturer', 'name'],
            },
        ),
    ]
