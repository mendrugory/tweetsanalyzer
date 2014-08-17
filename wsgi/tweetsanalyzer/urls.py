from django.conf.urls import patterns, include, url

from django.contrib import admin
import tweetsanalyzer.views as views
import tweetsanalyzer.source_research.views as source_views

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tweetsanalyzer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^source_research$', source_views.source_research),
    url(r'^admin/', include(admin.site.urls)),
)
