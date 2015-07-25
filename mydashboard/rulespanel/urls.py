from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.mydashboard.rulespanel import views

INDEX_URL= r'^$'
ADD_PROVIDER_URL = r'^add'

urlpatterns = patterns('openstack_dashboard.dashboards.mydashboard.rulespanel.views',
    
    url(INDEX_URL, views.IndexView.as_view(), name='index'),
    url(ADD_PROVIDER_URL, views.AddProviderView.as_view(), name='add'),
)
