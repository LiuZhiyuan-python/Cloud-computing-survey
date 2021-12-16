# Generated by Django 4.0 on 2021-12-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stu_id', models.CharField(max_length=12)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0)),
                ('age', models.IntegerField()),
                ('question1', models.TextField()),
                ('question2', models.TextField()),
            ],
        ),
    ]