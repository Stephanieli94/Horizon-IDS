from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.mydashboard import dashboard

class Snortrules(horizon.Panel):
    name = _("Snortrules")
    slug = "snortrules"


dashboard.Mydashboard.register(Snortrules)
