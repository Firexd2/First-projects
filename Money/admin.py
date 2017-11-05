from django.contrib import admin
from Money import models

admin.site.register(models.monthMoney)

admin.site.register(models.Bank)

admin.site.register(models.Costs)

admin.site.register(models.LastAction)

admin.site.register(models.statisticsMonth)