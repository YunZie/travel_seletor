from django.db import models

class city(models.Model):
    id = models.AutoField(
        primary_key=True
        )
    city = models.CharField(
        max_length = 10,
        )
    district = models.CharField(
        max_length = 10,
    )
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        unique_together = ('city', 'district',)

class items(models.Model):
    id = models.AutoField(
        primary_key=True
        )
    element_name = models.CharField(
        max_length = 20,
        )
    description = models.CharField(
        max_length = 20,
        )
    class Meta:
        unique_together = ('element_name',)

class series(models.Model):
    id = models.AutoField(
        primary_key=True,
        )
    city = models.ForeignKey(
        city,
        on_delete=models.CASCADE,
    )
    items = models.ForeignKey(
        items,
        on_delete=models.CASCADE,
    )
    measure = models.CharField(
        max_length = 10,
    )
    value = models.IntegerField()
    time_unit = models.CharField(
        max_length = 10,
        )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        unique_together = ('city', 'items', 'measure', 'start_time')

class sights(models.Model):
    id = models.AutoField(
        primary_key=True,
        )

    name = models.CharField(
        max_length = 50,
    )

    city = models.CharField(
        max_length = 10,
    )

    district = models.CharField(
        max_length = 10,
    )

    address = models.CharField(
        max_length = 100,
    )

    elong = models.FloatField()

    nlat = models.FloatField()

    introduction = models.TextField()

    target = models.CharField(
        max_length = 30,
    )
    images = models.TextField()
    
    url = models.TextField()

    sourceType = models.IntegerField()

    class Meta:
        unique_together = ('name', 'address')