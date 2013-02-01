from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'o3p.views.home', name='home'),
    # url(r'^o3p/', include('o3p.foo.urls')),
    url(r'^pay/', include('pwyw.urls')),                       

    url(r'^members/', include('userena.urls')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
                       
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
