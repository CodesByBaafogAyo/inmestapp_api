# Generated by Django 5.0.2 on 2024-02-10 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cohort",
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
                ("name", models.CharField(blank=True, max_length=64, null=True)),
                ("description", models.TextField(blank=True, default="N/A", null=True)),
                ("year", models.IntegerField(default=1920)),
                ("start_date", models.DateTimeField(blank=True, null=True)),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_modified", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="IMUser",
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
                ("first_name", models.CharField(blank=True, max_length=64, null=True)),
                ("last_name", models.CharField(blank=True, max_length=64, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("EIT", "Eit"),
                            ("TEACHING_FELLOW", "Teaching Fellow"),
                            ("ADMIN_STAFF", "Admin Staff"),
                            ("ADMIN", "Admin"),
                        ],
                        default="EIT",
                        max_length=20,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_modified", models.DateTimeField(auto_now=True, null=True)),
                ("email", models.EmailField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="CohortMember",
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
                ("is_active", models.BooleanField(default=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "cohort",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cohortmember_cohort",
                        to="users.cohort",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cohormember_author",
                        to="users.imuser",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cohortmember_member",
                        to="users.imuser",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cohort",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cohort_author",
                to="users.imuser",
            ),
        ),
    ]
