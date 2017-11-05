from django.db import models

class BabyEat(models.Model):
    time = models.CharField(max_length=5)
    volume = models.IntegerField()
    data = models.CharField(max_length=10)
    toilet = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.time, self.volume, self.toilet, self.data)

    class Meta:
        verbose_name = 'Таблица питания'
        verbose_name_plural = 'Таблица питания'

class HistoryEat(models.Model):
    total_volume = models.IntegerField()
    total_toilet = models.IntegerField()
    data = models.DateField(auto_now=True)
    days = models.CharField(max_length=7)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.data, self.days, self.total_volume, self.total_toilet)

    class Meta:
        verbose_name = 'История питания'
        verbose_name_plural = 'История питания'

class BabyWeight(models.Model):
    week = models.IntegerField()
    weight = models.IntegerField()
    lenght = models.IntegerField()

    def __str__(self):
        return '%s, %s, %s' % (self.week, self.lenght, self.weight)

    class Meta:
        verbose_name = 'Развитие малыша'
        verbose_name_plural = 'Развитие малыша'






