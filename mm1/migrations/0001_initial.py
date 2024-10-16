from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_number', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=40)),
                ('max_numb_students', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('courses', models.ManyToManyField(to='mm1.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingTime',
            fields=[
                ('pid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('time', models.CharField(choices=[('8:45 - 9:35', '8:45 - 9:35'), ('9:35 - 10:25', '9:35 - 10:25'), ('10:45 - 11:35', '10:45 - 11:35'), ('11:35 - 12:25', '11:35 - 12:25'), ('1:10 - 2:00', '1:10 - 2:00'), ('2:00 - 2:50', '2:00 - 2:50'), ('3:00 - 3:50', '3:00 - 3:50'),('3:50 - 4:40', '3:50 - 4:40')], default='11:30 - 12:30', max_length=50)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_number', models.CharField(max_length=6)),
                ('seating_capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mm1.Course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mm1.Department')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mm1.Instructor')),
                ('meeting_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mm1.MeetingTime')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mm1.Room')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='mm1.Instructor'),
        ),
    ]
