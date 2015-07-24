from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.mydashboard import dashboard

class Eventspanel(horizon.Panel):
    name = _("Events")
    slug = "eventspanel"


dashboard.Mydashboard.register(Eventspanel)
