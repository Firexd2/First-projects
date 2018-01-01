from django.shortcuts import render, redirect
from Baby.forms import EatForm, WeightForm
from Baby.models import HistoryEat, BabyEat, BabyWeight
from datetime import datetime
from django.contrib.auth.decorators import login_required
import re


@login_required
def home_baby(request):
    Eat = [(str(x).split(","))[:-1] for x in BabyEat.objects.all()]
    total_volume = 0
    for n, item in enumerate(Eat):
        if Eat[n][4] == ' True': Eat[n][4] = '+'
        if Eat[n][4] == ' False': Eat[n][4] = '-'
        total_volume += (int(item[1]) + int(item[2]) + int(item[3]))

    if Eat:
        now_time = str(datetime.now())[11:16].split(':')
        last_time = re.split(':|-', Eat[-1][0])
        now_min = int(now_time[0]) * 60 + int(now_time[1])
        last_min = int(last_time[0]) * 60 + int(last_time[1]) if int(last_time[0]) <= int(now_time[0]) else int(last_time[0]) * 60 + int(last_time[1]) - 1440
        time_to_eat = [(now_min - last_min) // 60, (now_min - last_min) % 60]
        hours_time = str(time_to_eat[0]).zfill(2)
        min_time = str(time_to_eat[1]).zfill(2)
        last_min_anticipated = int(last_time[0]) * 60 + int(last_time[1])
        time_anticipated_min = last_min_anticipated + 180 if last_min_anticipated + 180 <= 1440 else last_min_anticipated + 180 - 1440
        time_anticipated = [time_anticipated_min // 60, time_anticipated_min % 60]
        houts_time_anticipated = str(time_anticipated[0]).zfill(2)
        min_time_anticipated = str(time_anticipated[1]).zfill(2)
    else:
        hours_time = '--'
        min_time = '--'
        houts_time_anticipated = '--'
        min_time_anticipated = '--'

    form = EatForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('home_baby')
    return render(request, 'home_baby.html', locals())

def history(request):
    History = [str(x).split(",") for x in HistoryEat.objects.all()][::-1]
    return render(request, 'history.html', locals())

def history_weight(request):
    weights_list = [str(x).split(",") for x in BabyWeight.objects.all()][::-1]
    form = WeightForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('history_weight')

    return render(request, 'history_weight.html', locals())