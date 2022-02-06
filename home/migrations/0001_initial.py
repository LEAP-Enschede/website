# Generated by Django 3.2.9 on 2022-01-05 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_page_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=200, null=True)),
                ('route', models.CharField(max_length=20, null=True)),
                ('order', models.IntegerField()),
                ('page_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.menuitem')),
            ],
        ),
    ]