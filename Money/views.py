from django.shortcuts import render, redirect
import datetime
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required
def history_costs(request):
    history = [list(x) for x in statisticsMonth.objects.all().values_list()][::-1]
    for item in history:
        item[8] = item[8].split('|')
    for iter in history:
        iter.append(iter[6]/iter[14] * 100)
    return render(request, 'history_costs.html', locals())

@login_required
def comment_money(request):
    form = ActionForm(request.POST or None)
    if request.POST and form.is_valid():
        message = form.cleaned_data['text']
        last = LastAction.objects.latest()
        last_text = str(last).split(',')[1][1:]
        last.delete()
        LastAction(text=last_text + ' Комментарий: ' + message).save()

        return redirect('money')
    return render(request, 'comment_money.html', locals())

@login_required
def moneyhome(request):
    try: amount = monthMoney.objects.all().values_list()[0]
    except: amount = [0, 0, 0, 0, 0, 0, 0, datetime.datetime.date(2017, 10, 6)]

    try: cost = Costs.objects.all().values_list()[0]
    except: cost = [0, 0, 0, 0, 0, 0, 0]

    bank = Bank.objects.all().values_list()[0][1]
    action = LastAction.objects.all().values_list('datetime', 'text')[::-1][0:10]

    now_week = (datetime.date.today() - amount[7]).days // 8
    week = 4 - now_week


    one, two, three, four, five, amount1 = amount[2], amount[3], amount[4], amount[5], amount[6], amount[1]
    one_cost, two_cost, three_cost, four_cost, five_cost, amount1_cost = cost[2], cost[3], cost[4], cost[5], cost[6], cost[1]
    one_diff, two_diff, three_diff, four_diff, five_diff, amount1_diff = amount[2] - cost[2], amount[3] - cost[3], amount[4] - cost[4], amount[5] - cost[5], amount[6] - cost[6], amount[1] - cost[1]
    one_week, two_week, three_week, four_week, five_week, amount1_week = int(one / 4), int(two / 4), int(three / 4), int(four / 4), int(five / 4), int(amount1 / 4)

    amount1_week = one_week + two_week + three_week + four_week # переназначем общую сумму недели для того, чтобы не учитывать большие покупки
    amount1_cost_for_week = one_cost + two_cost + three_cost + four_cost

    one_week_now = int(one_cost - one_week * now_week)
    two_week_now = int(two_cost - two_week * now_week)
    three_week_now = int(three_cost - three_week * now_week)
    four_week_now = int(four_cost - four_week * now_week)
    five_week_now = int(five_cost - five_week * now_week)
    amount1_week_now = int(amount1_cost_for_week - amount1_week * now_week)

    one_procent = int(one_cost / one * 100)
    two_procent = int(two_cost / two * 100)
    three_procent = int(three_cost / three * 100)
    four_procent = int(four_cost / four * 100)
    five_procent = int(five_cost / five * 100)
    amount1_procent = int(amount1_cost / amount1 * 100)

    one_week_diff = one_week - one_week_now
    two_week_diff = two_week - two_week_now
    three_week_diff = three_week - three_week_now
    four_week_diff = four_week - four_week_now
    five_week_diff = five_week - five_week_now
    amount1_week_diff = amount1_week - amount1_week_now

    one_week_procent = int(100 - (one_week_now / one_week * 100))
    two_week_procent = int(100 - (two_week_now / two_week * 100))
    three_week_procent = int(100 - (three_week_now / three_week * 100))
    four_week_procent = int(100 - (four_week_now / four_week * 100))
    five_week_procent = int(100 - (five_week_now / five_week * 100))
    amount1_week_procent = int(100 - (amount1_week_now / amount1_week * 100))

    form_money = MoneyForm(request.POST or None)
    form_create_bank = BankForm(request.POST or None)
    form_cost = CostForm(request.POST or None)

    if request.POST:
        if request.POST.get('amount') and form_money.is_valid():
            Action = LastAction.objects.all()
            first_date = str(list(Action)[0]).split(',')[0][:10]
            last_date = str(list(Action)[-1]).split(',')[0][:10]
            information_cost = ''
            for item in [str(x) for x in Action if 'Совершена' in str(x)]:
                information_cost += '<b>' + item[:19] + '</b>' + ' ' + item[34:] + '|'
            statisticsMonth(one=one_cost, two=two_cost, three=three_cost, four=four_cost, five=five_cost, amount=amount1_cost, date='C ' + first_date + ' по ' + last_date, information=information_cost, one_amount=one, two_amount=two, three_amount=three, four_amount=four, five_amount=five, amount_amount=amount1).save()
            monthMoney.objects.all().delete()
            Bank.objects.all().delete()
            Costs.objects.all().delete()
            LastAction.objects.all().delete()
            Bank(bank=(int(bank) + amount1_diff)).save()
            MoneyForm({'amount': str(int(form_money.cleaned_data['amount']))}).save()
            LastAction(text='Внесена зарплата и обнулен счет. В банк было зачислено ' + str(amount1_diff) + ' неиспользованного остатка за предыдущий месяц.').save()
        elif request.POST.get('bank') and form_create_bank.is_valid():
            Bank.objects.all().delete()
            form_create_bank.save()
            LastAction(text='Корректирован банк на сумму ' + str(request.POST.get('bank')) + ' рублей.').save()
        elif request.POST.get('one_cost') and form_cost.is_valid():
            data = form_cost.cleaned_data
            Costs.objects.all().delete()
            Costs(one_cost=cost[2] + int(data['one_cost']), two_cost=cost[3] + int(data['two_cost']), three_cost=cost[4] + int(data['three_cost']), four_cost=cost[5] + int(data['four_cost']), five_cost=cost[6] + int(data['five_cost'])).save()
            LastAction(text='Совершена покупка на сумму ' + str(sum(data.values())) + ' руб.').save()
            if sum(data.values()) > 100:
                return comment_money(request)

        else: pass

        return redirect('money')

    return render(request, 'money.html', locals())
