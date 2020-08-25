# Generated by Django 3.1 on 2020-08-24 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_img', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=42)),
                ('text', models.CharField(max_length=280)),
                ('overview', models.CharField(blank=True, max_length=64, null=True)),
                ('slug', models.SlugField(blank=True, max_length=42, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1_article.article')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1_article.language')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1_article.category'),
        ),
    ]