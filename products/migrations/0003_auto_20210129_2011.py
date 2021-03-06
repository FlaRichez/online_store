# Generated by Django 3.1.5 on 2021-01-29 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210120_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbouTus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=500)),
                ('face', models.TextField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='products_file',
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, default='default_product_image.png', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('In process', 'In process'), ('Delivered', 'Delivered'), ('Not Delivered', 'Not Delivered')], default=1, max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.products')),
            ],
        ),
    ]
