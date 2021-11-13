# Generated by Django 3.2.8 on 2021-11-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bechelor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('studyYear', models.CharField(choices=[('1ST', 'First Year'), ('2ND', 'Second Year'), ('3RD', 'Third Year')], default='1ST', max_length=3)),
            ],
            options={
                'db_table': 'bechelor_tab',
            },
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('espMark', models.FloatField(verbose_name='End of Study Project Mark')),
            ],
            options={
                'db_table': 'terminal_atb',
            },
        ),
    ]
