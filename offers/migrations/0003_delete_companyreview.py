# Generated by Django 4.2.2 on 2023-06-20 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("offers", "0002_alter_companyreview_company"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CompanyReview",
        ),
    ]
