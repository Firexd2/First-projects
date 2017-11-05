from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', blog_home, name='blog_home'),
    url(r'^/post/(?P<name_url>\w+)$', post, name='post'),
    url(r'new_post/', new_post, name='new_post'),
    url(r'^/delete_post/(?P<name_url>\w+)$', delete_post, name='delete_post'),
    url(r'^/edit_post/(?P<name_url>\w+)$', edit_post, name='edit_post'),
    url(r'^/category/(?P<category>\w+)$', filter_to_category, name='filter_to_category'),
    url(r'^/image$', image, name='image')
]