from django.conf.urls import patterns, include, url

from django.contrib import admin
from ecommerce import views

#url
urlpatterns = patterns('',
    url(r'^$', views.catalog, name ="catalog"),
    url(r'^cart/$', views.cart, name ="cart"),
    url(r'^cart/remove/$', views.removefromcart),
    url(r'^cart/checkout/$', views.checkout, name="checkout"),
    url(r'^cart/checkout/complete/$', views.completeOrder, name="complete_order"),
    url(r'^admin-login/$', views.adminLogin, name="admin_login"),
    url(r'^admin-panel/$', views.adminDashboard, name="admin"),
)
