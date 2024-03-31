# Generated by Django 4.2.11 on 2024-03-31 19:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('is_external', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.area')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('completed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('bin_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bin_from', to='data.bin')),
                ('bin_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bin_to', to='data.bin')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.item')),
            ],
        ),
    ]
