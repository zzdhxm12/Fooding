from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    main_category = models.CharField(max_length=100, blank=True, null=True)
    middle_category = models.CharField(max_length=100, blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)
    review_cnt = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Store'


class Menu(models.Model):
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Menu'