from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='facebook_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='twitter_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='instagram_url',
            field=models.URLField(blank=True),
        ),
    ]
