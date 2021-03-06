# Generated by Django 3.1.2 on 2020-10-09 13:56

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
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rating', models.PositiveIntegerField(default=5)),
                ('genre', models.IntegerField(blank=True, choices=[(0, 'Unknown'), (1, 'Horror'), (2, 'Sci-Fi'), (3, 'Drama'), (4, 'Comedy'), (5, 'Fantasy'), (6, 'Other')], null=True)),
                ('amount_sites', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=128, null=True)),
                ('user', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
