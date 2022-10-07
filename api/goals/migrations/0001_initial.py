# Generated by Django 4.0.7 on 2022-09-09 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goalType', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField(verbose_name='date published')),
                ('createdBy', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('startsOn', models.TimeField()),
                ('endsOn', models.TimeField()),
                ('percentageCompleted', models.IntegerField(default=0)),
                ('assignedBy', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.goal')),
            ],
        ),
    ]
