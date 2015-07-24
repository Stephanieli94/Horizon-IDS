from django.utils.translation import ugettext_lazy as _

import horizon


class Mydashboard(horizon.Dashboard):
    name = _("Mydashboard")
    slug = "mydashboard"
    panels = ()  # Add your panels here.
    default_panel = ''  # Specify the slug of the dashboard's default panel.


horizon.register(Mydashboard)
