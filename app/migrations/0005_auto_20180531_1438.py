# Generated by Django 2.0.5 on 2018-05-31 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_cliente_cli_rg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cli_nome', models.CharField(max_length=50)),
                ('cli_rg', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
