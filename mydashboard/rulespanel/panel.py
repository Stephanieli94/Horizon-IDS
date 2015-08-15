from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.mydashboard import dashboard

class Rulespanel(horizon.Panel):
    name = _("Rules")
    slug = "rulespanel"


dashboard.Mydashboard.register(Rulespanel)
