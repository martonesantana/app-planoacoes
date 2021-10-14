# Generated by Django 3.2.8 on 2021-10-13 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(max_length=100, verbose_name='Ação')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Ação',
                'verbose_name_plural': 'Ações',
            },
        ),
        migrations.AlterModelOptions(
            name='situacao',
            options={'verbose_name': 'Situação', 'verbose_name_plural': 'Situações'},
        ),
        migrations.AlterField(
            model_name='situacao',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='situacao',
            name='periodo',
            field=models.DateField(verbose_name='Período'),
        ),
        migrations.AlterField(
            model_name='situacao',
            name='situacao',
            field=models.CharField(max_length=100, verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='situacao',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor'),
        ),
        migrations.CreateModel(
            name='DetalheAcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalhe', models.CharField(max_length=100, verbose_name='Detalhes')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
                ('acao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.acao')),
            ],
            options={
                'verbose_name': 'Detalhes da Ação',
                'verbose_name_plural': 'Detalhes das Ações',
            },
        ),
        migrations.CreateModel(
            name='Causa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('causas', models.CharField(max_length=100, verbose_name='Causas')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
                ('situacao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.situacao')),
            ],
            options={
                'verbose_name': 'Causa',
                'verbose_name_plural': 'Causas',
            },
        ),
        migrations.AddField(
            model_name='acao',
            name='causas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.causa'),
        ),
    ]
