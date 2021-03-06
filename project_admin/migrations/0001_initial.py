# Generated by Django 2.1.5 on 2019-01-28 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import project_admin.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=50)),
                ('project_name', models.CharField(max_length=50)),
                ('objective', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('file', models.FileField(upload_to=project_admin.models.user_directory_path)),
                ('status', models.BooleanField(default=False)),
                ('programmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='project_admin.Project')),
            ],
        ),
    ]
