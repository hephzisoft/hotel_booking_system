# Generated by Django 4.2.3 on 2023-07-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_miramar', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=255)),
                ('message', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Enquiries',
            },
        ),
    ]
