# Generated by Django 3.1.2 on 2020-10-07 00:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, verbose_name='タグ名')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='画像')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qiiteru.tag', verbose_name='タグ')),
            ],
        ),
    ]
