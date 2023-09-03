# Generated by Django 4.2 on 2023-06-21 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polls', '0003_delete_capture_delete_demandecapture'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeCapture',
            fields=[
                ('id_dc', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_demande', models.CharField(max_length=200)),
                ('interface_reseau', models.CharField(max_length=200)),
                ('Nbr_paquet', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id_c', models.BigAutoField(primary_key=True, serialize=False)),
                ('ip_src', models.CharField(max_length=200)),
                ('ip_dst', models.CharField(max_length=200)),
                ('protocole', models.CharField(max_length=200)),
                ('src_port', models.CharField(max_length=200)),
                ('dst_port', models.CharField(max_length=200)),
                ('id_dc', models.ForeignKey(db_column='id_dc', on_delete=django.db.models.deletion.CASCADE, to='polls.demandecapture')),
            ],
        ),
    ]