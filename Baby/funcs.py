from django.shortcuts import redirect
from Baby.models import BabyEat, HistoryEat
import datetime
import time


def delit(request):
    try:
        BabyEat.objects.all().last().delete()
    except: pass
    return redirect('home_baby')

def up_history(request):
    Eat = [str(x).split(",") for x in BabyEat.objects.all()]
    for n, item in enumerate(Eat):
        if Eat[n][4] == ' True': Eat[n][4] = 1
        if Eat[n][4] == ' False': Eat[n][4] = 0
    total_volume = 0
    total_toilet = 0
    days = str(datetime.timedelta(seconds=(time.time() - 1503002700)))[:7]
    for item in Eat:
        total_toilet += item[4]
        total_volume += (int(item[1]) + int(item[2]) + int(item[3]))
    h = HistoryEat(total_volume=total_volume, total_toilet=total_toilet, days=days)
    h.save()
    BabyEat.objects.all().delete()
    return redirect('history')
