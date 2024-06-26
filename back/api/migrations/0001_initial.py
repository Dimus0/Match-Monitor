# Generated by Django 4.2.11 on 2024-04-21 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('coach', models.CharField(max_length=100)),
                ('stadium_into_training', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('goal_score_home_team', models.IntegerField()),
                ('goal_score_away_team', models.IntegerField()),
                ('name_of_referee', models.CharField(max_length=100)),
                ('away_team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='api.team')),
                ('home_team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='api.team')),
            ],
        ),
    ]
