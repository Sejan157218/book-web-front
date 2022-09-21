# Generated by Django 3.2 on 2022-09-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220921_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalPrice',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Processing', 'Order Processing'), ('Order Canceled', 'Order Canceled'), ('Order Completed', 'Order Completed'), ('On the way', 'On the way'), ('Order Received', 'Order Received')], default='Order Received', max_length=100),
        ),
    ]
