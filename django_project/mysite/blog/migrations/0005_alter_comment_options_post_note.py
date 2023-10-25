# Generated by Django 4.2.5 on 2023-10-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_comment_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
