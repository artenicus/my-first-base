# Generated by Django 2.2.5 on 2020-07-22 07:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200720_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Autor', models.CharField(max_length=200)),
                ('Treść', models.TextField()),
                ('Data_Utworzenia', models.DateTimeField(default=django.utils.timezone.now)),
                ('Zatwierdzony_Komentarz', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post')),
            ],
        ),
    ]
