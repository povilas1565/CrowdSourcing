
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='certificates',
            field=models.FileField(default='Attach Certs', upload_to='freelancer_certs'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='Enter Email Here...', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='experience',
            field=models.TextField(default='Enter Experience Here...', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Enter location Here...', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='Enter Phone Number', max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(default='Attach Resumer', upload_to='freelancer_docs'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(default='Enter Skills Here...', max_length=100),
        ),
    ]
