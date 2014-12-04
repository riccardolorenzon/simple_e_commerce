from django.conf.urls import patterns, include, url

from django.contrib import admin
from ecommerce import urls as app_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpleECommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(app_urls)),

)
