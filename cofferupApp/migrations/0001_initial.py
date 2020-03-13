# Generated by Django 3.0.4 on 2020-03-13 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('description', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContributorCoffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cofferupApp.Coffer')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cofferupApp.Contributor')),
            ],
        ),
        migrations.CreateModel(
            name='ContributorCofferTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_contribution', models.BooleanField()),
                ('description', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('contributor_coffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cofferupApp.ContributorCoffer')),
            ],
        ),
        migrations.AddField(
            model_name='coffer',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cofferupApp.Contributor'),
        ),
    ]
