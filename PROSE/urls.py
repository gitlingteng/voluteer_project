from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'auth.views.logout_view'),
    url(r'^$', 'views.landing'),
    url(r'^kidlink/', include('kidlink.urls')),
    url(r'^messages/', include('messaging.urls')),
    url(r'^patient/', include('patients.urls')),
    url(r'^oncall/', include('oncallschedule.urls')),
    url(r'^prefs/', 'messaging.views.edit_message_prefs', name="prefs"),
)