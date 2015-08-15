import traceback

from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.mydashboard.rulespanel import utils


class SetProviderDetailsAction(workflows.Action):
    
    action = forms.CharField(
	 label=_("Action"),
	 required=True,
	 max_length=80,
	 )

    protocal = forms.CharField(
        label=_("Protocal"),
        required=True,
        max_length=80,
	help_text=_("Protocal"))
	
    sourceIP = forms.CharField(
        label=_("SourceIP"),
        required=True,
        max_length=80,
	help_text=_("SourceIP"))
	
    sourcePort = forms.CharField(
        label=_("SourcePort"),
        required=True,
        max_length=80,
        help_text=_("SourcePort"))
	
    direction = forms.CharField(
        label=_("Direction"),
        required=True,
        max_length=80,
        help_text=_("Direction"))
	
    destinationIP = forms.CharField(
        label=_("DestinationIP"),
        required=True,
        max_length=80,
        help_text=_("DestinationIP"))
	
    destinationPort = forms.CharField(
        label=_("DestinationPort"),
        max_length=80,
        required=True,
        help_text=_("DestinationPort"))

    	
    description = forms.CharField(
        label=_("Description"),
        max_length=80,
        required=True,
        help_text=_("Description"))
	
    priority = forms.CharField(
        label=_("Priority"),
        max_length=80,
        required=True,
	
        help_text=_("Priority"))

    class Meta:
        name = _("Details")

    def __init__(self, request, context, *args, **kwargs):
               
       
        self.request = request
        self.context = context
        super(SetProviderDetailsAction, self).__init__(
            request, context, *args, **kwargs)

class SetProviderDetails(workflows.Step):
    action_class = SetProviderDetailsAction
    contributes = ("action","protocal", "sourceIP", "sourcePort", "direction", "destinationIP", "destinationPort","description","priority")

    def contribute(self, data, context):
        if data:
	    context['action'] = data.get("action","")
            context['protocal'] = data.get("protocal", "")
            context['sourceIP'] = data.get("sourceIP", "")
            context['sourcePort'] = data.get("sourcePort", "")
            context['direction'] = data.get("direction", "")
            context['destinationIP'] = data.get("destinationIP", "")
            context['destinationPort'] = data.get("destinationPort", "")
            context['description'] = data.get("description", "")
            context['priority'] = data.get("priority", "")
        return context

class AddProvider(workflows.Workflow):
    slug = "add"
    name = _("Add")
    finalize_button_name = _("Add")
    success_message = _('Added provider "%s".')
    failure_message = _('Unable to add provider "%s".')
    success_url = "horizon:mydashboard:rulespanel:index"
    failure_url = "horizon:mydashboard:rulespanel:index"
    default_steps = (SetProviderDetails,)

    def format_status_message(self, message):
         return message % self.context.get('name', 'unknown provider')

    def handle(self, request, context):
        try:
            utils.addProvider(self, request, context)
            return True
        except Exception:
            print traceback.format_exc()
            exceptions.handle(request, _("Unable to add provider"))
	    return False
