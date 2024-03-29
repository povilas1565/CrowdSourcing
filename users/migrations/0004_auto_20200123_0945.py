
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200123_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='certificates',
            field=models.FileField(default='Attach Certs', upload_to='freelancer_certs', validators=[users.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(default='Attach Resume', upload_to='freelancer_docs', validators=[users.validators.validate_file_extension]),
        ),
    ]
