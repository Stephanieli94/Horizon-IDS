from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.mydashboard.eventspanel.views \
    import IndexView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
)
