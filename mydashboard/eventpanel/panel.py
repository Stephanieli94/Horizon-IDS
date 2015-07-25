from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.mydashboard import dashboard

class Eventpanel(horizon.Panel):
    name = _("Events")
    slug = "eventpanel"


dashboard.Mydashboard.register(Eventpanel)
