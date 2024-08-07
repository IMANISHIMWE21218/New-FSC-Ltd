# Generated by Django 5.0.7 on 2024-08-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fsc_app", "0005_companyinfo_blochure"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="ourprojects",
            name="ChallangeAndSolution",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ourprojects",
            name="ChallangeAndSolutionTitle",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="ourprojects",
            name="category",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="ourprojects",
            name="client",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="ourprojects",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ourprojects",
            name="location",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="ourprojects",
            name="timeline",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="ourprojects",
            name="tags",
            field=models.ManyToManyField(blank=True, to="fsc_app.tag"),
        ),
    ]
