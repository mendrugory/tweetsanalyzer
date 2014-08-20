from django.conf.urls import patterns, include, url

from django.contrib import admin
import tweetsanalyzer.views as views
import tweetsanalyzer.source_research.views as source_views
import tweetsanalyzer.lang_research.views as lang_views

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tweetsanalyzer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^source_research$', source_views.source_research),
    url(r'^source_research/(\d{1,2})$', source_views.source_research),
    url(r'^lang_research$', lang_views.lang_research),
    url(r'^lang_research/(\d{1,2})$', lang_views.lang_research),
    url(r'^admin/', include(admin.site.urls)),
)
