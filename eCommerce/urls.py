from django.conf.urls import patterns, include, url

from django.contrib import admin
from ecommerce import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpleECommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.catalog, name ="catalog"),
    url(r'^cart/$', views.cart, name ="cart"),
    url(r'^cart/remove/$', views.removefromcart),
    url(r'^cart/checkout/$', views.checkout, name="checkout"),
    url(r'^cart/checkout/complete$', views.completeOrder, name="complete_order")
)
