# Generated by Django 3.2.3 on 2021-09-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_adminpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlıq')),
                ('content', models.TextField(verbose_name='Mətn')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, verbose_name='Kateqoriya')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, verbose_name='Məkan')),
                ('phone', models.CharField(max_length=50, verbose_name='Əlaqə')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, to='article.Category', verbose_name='Kateqoriya'),
        ),
    ]
