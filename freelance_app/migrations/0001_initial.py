
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.TextField(default=None, max_length=500)),
                ('postedOn', models.DateTimeField(auto_now_add=True)),
                ('isCompleted', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('task_count', models.IntegerField(default=0)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('amount', models.IntegerField(default=0)),
                ('task_description', models.TextField(default=None, max_length=1000)),
                ('task_link', models.URLField(blank=True)),
                ('latest_submission_time', models.DateTimeField(blank=True, null=True)),
                ('isCompleted', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='freelance_app.Project')),
            ],
        ),
    ]
