from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('patients.views',
    url(r'^$', 'patient_list'),
    url(r'^patients/edit/(?P<pk>\d+)/$', 'edit'),
    url(r'^patients/add/$', 'add'),
)




