# Generated by Django 3.2.9 on 2021-11-05 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateTimeField(verbose_name='start')),
                ('end', models.DateTimeField(verbose_name='end')),
            ],
        ),
        migrations.CreateModel(
            name='ActivitySignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_participants', models.IntegerField(verbose_name='max participants')),
                ('start', models.DateTimeField(verbose_name='signup start')),
                ('end', models.DateTimeField(verbose_name='signup end')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.activity')),
            ],
        ),
    ]
