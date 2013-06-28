from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^getEventsNearMe/$', 'splash.views.getEventsNearMe'),
    url(r'^getInterestCategories/$', 'splash.views.getInterestCategories'),
    url(r'^getInterestCategoryInterests/$', 'splash.views.getInterestCategoryInterests'),
    url(r'^getEventMessages/$', 'splash.views.getEventMessages'),
    url(r'^getEventUsers/$', 'splash.views.getEventUsers'),
    url(r'^getMyInterests/$', 'splash.views.getMyInterests'),
    url(r'^getMyEvents/$', 'splash.views.getMyEvents'),
    # url(r'^loop/', include('loop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
