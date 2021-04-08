# Generated by Django 3.1.1 on 2021-03-17 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20210317_1024'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='store_id',
            field=models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='stores.store'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_id', models.ForeignKey(db_column='follow_id', on_delete=django.db.models.deletion.CASCADE, related_name='follow', to='accounts.user')),
                ('following_id', models.ForeignKey(db_column='following_id', on_delete=django.db.models.deletion.CASCADE, related_name='following', to='accounts.user')),
            ],
        ),
    ]