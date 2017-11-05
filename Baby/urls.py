from django.conf.urls import url
from Baby import funcs
from . import views


urlpatterns = [
    url(r'^$', views.home_baby, name='home_baby'),
    url(r'/delit', funcs.delit),
    url(r'/up_history', funcs.up_history),
    url(r'^/history$', views.history, name='history'),
    url(r'^/history_weight$', views.history_weight, name='history_weight')
]