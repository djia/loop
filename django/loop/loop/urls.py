from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^api/getInterestCategories/$', 'interests.api.get_interestcategories'),
    url(r'^api/getInterestCategoryInterests/$', 'interests.api.get_interestcategory_interests'),    
    url(r'^api/getMyInterests/$', 'interests.api.get_myinterests'),

    url(r'^api/getEventsNearMe/$', 'events.api.get_events_nearme'),
    url(r'^api/getEventMessages/$', 'events.api.get_eventmessages'),
    url(r'^api/getMyEvents/$', 'events.api.get_myevents'),

    url(r'^api/getEventUsers/$', 'accounts.api.get_eventusers'),
    url(r'^api/getInterestUsers/$', 'accounts.api.get_interestusers'),
    # url(r'^loop/', include('loop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
