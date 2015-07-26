from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.mydashboard.snortrules import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$',views.AddRulesView.as_view(),name='add'),
)
