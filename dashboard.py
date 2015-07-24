
from django.utils.translation import ugettext_lazy as _

import horizon

class Rulegroup(horizon.PanelGroup):
    slug = "rulegroup"
    name = _("Rules")
    panels = ('rulespanel',) #this is the path of rulesPanel folder

class Mygroup(horizon.PanelGroup):
    slug = "mygroup"
    name = _("Report")
    panels = ('mypanel','eventspanel',)


class Mydashboard(horizon.Dashboard):
    name = _("IDSaaS")
    slug = "mydashboard"
    panels = (Mygroup,Rulegroup)  # Add your panels here.
    default_panel = 'mypanel'  # Specify the slug of the default panel.


horizon.register(Mydashboard)
