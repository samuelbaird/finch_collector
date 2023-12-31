# Generated by Django 4.2.3 on 2023-07-27 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_beak_shape_finch_beak_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='sighting date')),
                ('location', models.CharField(choices=[('1', 'Baltra'), ('2', 'Bartolomé'), ('3', 'Darwin'), ('4', 'Hood'), ('5', 'Fernandina'), ('6', 'Floreana'), ('7', 'Genovesa'), ('8', 'Isabela'), ('9', 'Marchena'), ('10', 'North Seymour'), ('11', 'Pinzón'), ('12', 'Pinta'), ('13', 'Rábida'), ('14', 'San Cristóbal'), ('15', 'Santa Cruz'), ('16', 'Santa Fe'), ('17', 'Santiago'), ('18', 'Wolf')], default='1', max_length=2)),
                ('finch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.finch')),
            ],
        ),
    ]
