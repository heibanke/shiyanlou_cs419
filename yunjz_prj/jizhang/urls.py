#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin


from jizhang import views

admin.autodiscover()

urlpatterns = patterns('',
    # items
    url(r'^$', views.items, name="items"),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_item, name='edit_item'),
    url(r'^new/$',views.new_item,name='new_item'),

    #categorys
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/(?P<pk>\d+)/$', views.show_category, name='show_category'),    
    url(r'^categories/(?P<pk>\d+)/edit/$', views.edit_category, name='edit_category'),
    url(r'^categories/new/$',views.new_category,name='new_category'),   
)
