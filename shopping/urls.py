#from django.conf.urls import url, patterns
from django.urls import path, re_path
from shopping import views

"""
urlpatterns = patterns('shopping.views',
    url(r'^add/$', 'add', name='shopping-cart-add'),
    url(r'^remove/$', 'remove', name='shopping-cart-remove'),
    url(r'^show/$', 'show', name='shopping-cart-show'),
)
"""
urlpatterns = [
    re_path(r'^add/$', views.add, name='shopping-cart-add'),
    re_path(r'^remove/$', views.remove, name='shopping-cart-remove'),
    re_path(r'^show/$', views.show, name='shopping-cart-show'),
    ]
