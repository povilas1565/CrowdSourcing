
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(choices=[('1', 'Admin'), ('2', 'Freelancer'), ('3', 'Project Owner')], default='Freelancer', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('phone_number', models.CharField(default='DEFAULT VALUE', max_length=14, unique=True)),
                ('email', models.EmailField(default='DEFAULT EMAIL', max_length=254, unique=True)),
                ('location', models.CharField(default='DEFAULT VALUE', max_length=30)),
                ('Age', models.PositiveIntegerField(default=0)),
                ('skills', models.TextField(default='DEFAULT VALUE', max_length=100)),
                ('experience', models.TextField(default='DEFAULT VALUE', max_length=100)),
                ('resume', models.FileField(default='DEFAULT VALUE', upload_to='freelancer_docs')),
                ('certificates', models.FileField(default='DEFAULT VALUE', upload_to='freelancer_certs')),
                ('interested_grades', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Grade One'), ('2', 'Grade Two'), ('3', 'Grade Three'), ('4', 'Grade Four')], default=1, max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
