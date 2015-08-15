from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.mydashboard import dashboard

class Alert(horizon.Panel):
    name = _("Alert")
    slug = "alert"


dashboard.Mydashboard.register(Alert)
