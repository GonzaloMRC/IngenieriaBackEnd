# Generated by Django 4.2.3 on 2023-07-21 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17)),
                ('brand', models.CharField(max_length=11)),
                ('model', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=4)),
                ('bodywork', models.CharField(max_length=16, null=1)),
                ('plate', models.CharField(max_length=7, null=1)),
                ('fuel', models.CharField(max_length=18, null=1)),
                ('displacement', models.CharField(max_length=5, null=1)),
                ('wheel_drive', models.CharField(max_length=9, null=1)),
                ('gas_tank', models.CharField(max_length=14, null=1)),
                ('net_weight', models.IntegerField(null=1)),
                ('goss_weight', models.IntegerField(null=1)),
                ('rows_seats', models.IntegerField(null=1)),
                ('mileage_km', models.IntegerField(null=1)),
                ('original_tire_code', models.CharField(max_length=9, null=1)),
                ('installed_tire_code', models.CharField(max_length=9, null=1)),
                ('car_use', models.CharField(max_length=18, null=1)),
                ('extra_charge', models.CharField(max_length=25, null=1)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('dni_ruc', models.CharField(max_length=11)),
                ('phone_number', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=30, null=1)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correlative', models.IntegerField()),
                ('status', models.CharField(max_length=11)),
                ('registration_date', models.DateField()),
                ('development', models.CharField(max_length=12)),
                ('request_reason', models.CharField(max_length=100)),
                ('aplication', models.CharField(max_length=100)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='DesignedSpring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osis_code', models.IntegerField()),
                ('selected', models.BooleanField(default=0)),
                ('l_inst', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('l_charg', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('l_max', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('l_4', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('raw_material', models.CharField(default='-', max_length=20)),
                ('weight', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('transition_point', models.IntegerField(null=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('lda', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ProducedSpring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osis_code', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Spring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wire', models.DecimalField(decimal_places=2, max_digits=4)),
                ('diam_ext1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('diam_ext2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('diam_int1', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('diam_int2', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('length', models.DecimalField(decimal_places=2, max_digits=6)),
                ('coils', models.DecimalField(decimal_places=3, max_digits=6)),
                ('coil_direction', models.CharField(max_length=20)),
                ('end1', models.CharField(default='-', max_length=50)),
                ('luz1', models.IntegerField()),
                ('detail1_end1', models.CharField(default='-', max_length=15)),
                ('detail2_end1', models.CharField(default='-', max_length=15)),
                ('detail3_end1', models.CharField(default='-', max_length=15)),
                ('eccentricity1', models.DecimalField(decimal_places=3, default='-', max_digits=6)),
                ('end2', models.CharField(default='-', max_length=50)),
                ('luz2', models.IntegerField()),
                ('detail1_end2', models.CharField(default='-', max_length=15)),
                ('detail2_end2', models.CharField(default='-', max_length=15)),
                ('detail3_end2', models.CharField(default='-', max_length=15)),
                ('eccentricity2', models.DecimalField(decimal_places=3, default='-', max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='SpringPointsDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coils', models.DecimalField(decimal_places=3, max_digits=6)),
                ('include_point', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SampleSpring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spring_type', models.CharField(max_length=10)),
                ('spring_position', models.CharField(max_length=9)),
                ('suspension_type', models.CharField(max_length=16)),
                ('source', models.CharField(max_length=15)),
                ('coil_spacer', models.CharField(max_length=20)),
                ('spacer_height', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.car')),
                ('spring', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='queryapp.spring')),
            ],
        ),
        migrations.CreateModel(
            name='QualityControlReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_number', models.CharField(max_length=15)),
                ('production_requirement', models.CharField(max_length=15)),
                ('work_order', models.CharField(max_length=15)),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.design')),
                ('designed_spring', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.designedspring')),
                ('produced_spring', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.producedspring')),
            ],
        ),
        migrations.AddField(
            model_name='producedspring',
            name='spring',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.spring'),
        ),
        migrations.AddField(
            model_name='designedspring',
            name='spring',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='queryapp.spring'),
        ),
        migrations.AddField(
            model_name='design',
            name='sample_spring',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.samplespring'),
        ),
        migrations.CreateModel(
            name='CargoControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('f2', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('f3', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('f4', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('f5', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('f6', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('f7', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('f8', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('f9', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('f10', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l1', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l2', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l3', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l4', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l5', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l6', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l7', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l8', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l9', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('l10', models.DecimalField(decimal_places=2, max_digits=6, null=1)),
                ('spring', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='queryapp.spring')),
            ],
        ),
    ]
