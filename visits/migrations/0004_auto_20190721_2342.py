# Generated by Django 2.2.3 on 2019-07-21 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0003_remove_visit_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='visits.Visit'),
        ),
    ]
