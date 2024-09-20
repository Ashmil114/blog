# Generated by Django 4.2.16 on 2024-09-19 06:51

import app.blog.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=app.blog.models.image_path)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('no_of_views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.tb_category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='authentication.tb_user')),
            ],
        ),
    ]