# Generated by Django 3.0.3 on 2020-04-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_delete_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to='files/')),
            ],
        ),
    ]
