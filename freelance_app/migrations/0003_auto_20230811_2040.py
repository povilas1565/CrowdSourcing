

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0002_project_attachements'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='attachements',
            new_name='attachments',
        ),
        migrations.AddField(
            model_name='task',
            name='task_attachments',
            field=models.FileField(default='Attach Workdone', upload_to='tasks_docs', validators=[users.validators.validate_file_extension]),
        ),
    ]
