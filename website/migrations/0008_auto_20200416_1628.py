# Generated by Django 3.0.3 on 2020-04-16 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_resume_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='resume_file',
            new_name='resumefile',
        ),
    ]
