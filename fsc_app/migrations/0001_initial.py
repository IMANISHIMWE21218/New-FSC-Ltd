# Generated by Django 5.0.7 on 2024-08-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CompanyInfo",
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
                ("logo", models.ImageField(blank=True, null=True, upload_to="logos/")),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("VATnumber", models.CharField(blank=True, max_length=50, null=True)),
                ("location", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "office_time",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("facebook", models.CharField(blank=True, max_length=200, null=True)),
                ("twitter", models.CharField(blank=True, max_length=200, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=200, null=True)),
                ("pinterest", models.CharField(blank=True, max_length=200, null=True)),
                ("vimo", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OurProjects",
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
                (
                    "project_image",
                    models.ImageField(blank=True, null=True, upload_to="projects/"),
                ),
                (
                    "project_count",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "project_title",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("project_description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Partner",
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
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="partners/"),
                ),
                ("alt_text", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="TeamMember",
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
                ("name", models.CharField(max_length=255)),
                ("position", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="team/")),
                ("facebook", models.URLField(blank=True, null=True)),
                ("twitter", models.URLField(blank=True, null=True)),
                ("linkedin", models.URLField(blank=True, null=True)),
                ("pinterest", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="TestimonialInfo",
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
                (
                    "client_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "client_position",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "client_image",
                    models.ImageField(blank=True, null=True, upload_to="testimonials/"),
                ),
            ],
        ),
    ]