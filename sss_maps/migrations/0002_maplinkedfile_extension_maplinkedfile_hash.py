# Generated by Django 5.0.11 on 2025-02-07 00:46
import sss_maps.models
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('sss_maps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maplinkedfile',
            name='extension',
            field=models.CharField(default='pdf', max_length=5),
        ),
        migrations.AddField(
            model_name='maplinkedfile',
            name='hash',
            field=models.CharField(default=sss_maps.models.get_unique_id, max_length=500, null=True),
        )
    ]
