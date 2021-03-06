# Generated by Django 3.2 on 2021-04-24 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('serie', models.IntegerField(max_length=1)),
                ('media1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('media2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('media3', models.DecimalField(decimal_places=2, max_digits=4)),
                ('media4', models.DecimalField(decimal_places=2, max_digits=4)),
                ('media_final', models.CharField(max_length=10)),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'aluno',
            },
        ),
    ]
