# Generated by Django 4.2.8 on 2023-12-11 18:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BarangWishlist",
            new_name="Note",
        ),
    ]
