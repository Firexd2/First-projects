from django.db import models

class monthMoney(models.Model):
    amount = models.IntegerField(default=0, blank=True)
    one = models.IntegerField(default=0)
    two = models.IntegerField(default=0)
    three = models.IntegerField(default=0)
    four = models.IntegerField(default=0)
    five = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)


    def save(self, *args, **kwargs):
        self.one = int(self.amount * 0.24)
        self.two = int(self.amount * 0.16)
        self.three = int(self.amount * 0.18)
        self.four = int(self.amount * 0.14)
        self.five = int(self.amount * 0.28)
        super(monthMoney, self).save(*args, **kwargs)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s' % (self.one, self.two, self.three, self.four, self.five, self.amount, self.date)

    class Meta:
        verbose_name = 'Месячные деньги'
        verbose_name_plural = 'Месячные деньги'


class Costs(models.Model):
    amount_cost = models.IntegerField(default=0, blank=True)
    one_cost = models.IntegerField(default=0, blank=True)
    two_cost = models.IntegerField(default=0, blank=True)
    three_cost = models.IntegerField(default=0, blank=True)
    four_cost = models.IntegerField(default=0, blank=True)
    five_cost = models.IntegerField(default=0, blank=True)

    def save(self, *args, **kwargs):
        self.amount_cost = self.one_cost + self.two_cost + self.three_cost + self.four_cost + self.five_cost
        super(Costs, self).save(*args, **kwargs)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.one_cost, self.two_cost, self.three_cost, self.four_cost, self.five_cost, self.amount_cost)

    class Meta:
        verbose_name = 'Трата'
        verbose_name_plural = 'Траты'

class Bank(models.Model):
    bank = models.IntegerField()

    def __str__(self):
        return '%s' % self.bank

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банк'


class LastAction(models.Model):
    text = models.CharField(max_length=400)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s' % (self.datetime, self.text)

    class Meta:
        get_latest_by = 'datetime'
        verbose_name = 'Последнее действие'
        verbose_name_plural = 'Последние действия'


class statisticsMonth(models.Model):
     one = models.IntegerField(default=0)
     two = models.IntegerField(default=0)
     three = models.IntegerField(default=0)
     four = models.IntegerField(default=0)
     five = models.IntegerField(default=0)
     amount = models.IntegerField(default=0)
     date = models.CharField(max_length=20)
     information = models.CharField(max_length=1000)
     one_amount = models.IntegerField(default=0)
     two_amount = models.IntegerField(default=0)
     three_amount = models.IntegerField(default=0)
     four_amount = models.IntegerField(default=0)
     five_amount = models.IntegerField(default=0)
     amount_amount = models.IntegerField(default=0)

     def __str__(self):
         return '%s' % self.date

     class Meta:
         verbose_name = 'Месячная статистика'
         verbose_name_plural = 'Месячная статистика'