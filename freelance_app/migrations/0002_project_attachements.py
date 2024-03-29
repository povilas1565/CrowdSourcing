

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='attachements',
            field=models.FileField(default='Attach Workdone', upload_to='tasks_docs', validators=[users.validators.validate_file_extension]),
        ),
    ]
