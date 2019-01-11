from django.conf.urls import url
from sanfu import views


urlpatterns = [
    url(r'^index/$',views.index,name='index'),

    url(r'^regiest/$',views.regiest,name='regiest'),

    url(r'^login/$', views.login, name='login'),

    url(r'^cart/$', views.cart, name='cart'),

    url(r'^goodsMsg/$', views.goodsMsg, name='goodsMsg'),

    url(r'^goodsList/$', views.goodsList, name='goodsList'),

]