from django.contrib import admin
from Baby import models

class BabyEatAdmin(admin.ModelAdmin):
    list_display = ['data', 'time']


    class Meta:
        model = models.BabyEat

admin.site.register(models.BabyEat, BabyEatAdmin)

admin.site.register(models.HistoryEat)

admin.site.register(models.BabyWeight)

