from django.conf.urls import patterns, url
from google_maps import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djmaps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.MapView.as_view(), name ='maps'),

)
