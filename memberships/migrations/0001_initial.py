# Generated by Django 2.2.5 on 2019-09-30 08:28

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
            name='IdDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(choices=[('Passport', 'Passport'), ('National Id', 'National Id'), ('Id', 'Id')], max_length=25)),
                ('id_no', models.CharField(max_length=25)),
                ('f_name', models.CharField(max_length=25)),
                ('l_name', models.CharField(max_length=25)),
                ('expiry_date', models.DateField(null=True)),
                ('issue_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='memberships.IdDocuments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
