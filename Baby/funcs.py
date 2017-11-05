from django.shortcuts import redirect
from Baby.models import BabyEat, HistoryEat
import datetime
import time


def delit(request):
    try:
        last_time, last_volume, last_toilet = (str(list(BabyEat.objects.all())[-1]).split(','))[:-1]
        last_time, last_volume, last_toilet = last_time.lstrip(), last_volume.lstrip(), last_toilet.lstrip()
        BabyEat.objects.filter(time=last_time, volume=last_volume, toilet=last_toilet).delete()
    except: pass
    return redirect('home_baby')

def up_history(request):
    Eat = [str(x).split(",") for x in BabyEat.objects.all()]
    for n, item in enumerate(Eat):
        if Eat[n][2] == ' True': Eat[n][2] = 1
        if Eat[n][2] == ' False': Eat[n][2] = 0
    total_volume = 0
    total_toilet = 0
    days = str(datetime.timedelta(seconds=(time.time() - 1503002700)))[:7]
    for item in Eat:
        total_toilet += item[2]
        total_volume += int(item[1])
    h = HistoryEat(total_volume=total_volume, total_toilet=total_toilet, days=days)
    h.save()
    BabyEat.objects.all().delete()
    return redirect('history')