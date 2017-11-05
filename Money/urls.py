from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', moneyhome, name='money'),
    url(r'/comment_money', comment_money, name='comment_money'),
    url(r'/history_costs', history_costs, name='history_costs')
]