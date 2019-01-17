# Generated by Django 2.1.5 on 2019-01-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments_likeit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='commentarticle',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='commentcontent',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='commenttime',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='commentuser',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='likeit',
            old_name='likeitarticle',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='likeit',
            old_name='likeittime',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='likeit',
            old_name='likeituser',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='commentexist',
        ),
        migrations.RemoveField(
            model_name='likeit',
            name='likeitexist',
        ),
        migrations.AddField(
            model_name='comments',
            name='isdelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='likeit',
            name='isdelete',
            field=models.BooleanField(default=False),
        ),
    ]
