from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^api/getinterestcategories/$', 'interests.api.get_interestcategories'),
    url(r'^api/getinterestcategoryinterests/$', 'interests.api.get_interestcategory_interests_nearme'),    
    url(r'^api/getmyinterests/$', 'interests.api.get_myinterests'),
    url(r'^api/geteventinterests/$', 'interests.api.get_eventinterests'),

    url(r'^api/geteventsnearme/$', 'events.api.get_events_nearme'),
    url(r'^api/geteventmessages/$', 'events.api.get_eventmessages'),
    url(r'^api/getmyevents/$', 'events.api.get_myevents'),
    url(r'^api/getinteresteventsnearme/$', 'events.api.get_interestevents_nearme'),

    url(r'^api/geteventusers/$', 'accounts.api.get_eventusers'),
    url(r'^api/getinterestusers/$', 'accounts.api.get_interestusers'),
    # url(r'^loop/', include('loop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
