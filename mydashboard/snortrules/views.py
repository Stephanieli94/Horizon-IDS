import operator

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator  # noqa
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters  # noqa


from horizon import views
from django.shortcuts import render
from horizon import tables
from .tables import InstancesTable
import json 
from .ruleBean import ruleBean
import subprocess 
from horizon import exceptions
from horizon import forms

from openstack_dashboard.dashboards.mydashboard.snortrules \
    import forms as project_forms

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class = InstancesTable
    template_name = 'mydashboard/snortrules/index.html'

    def get_data(self):
        # Add data to the context here...


         filejson = open("/opt/stack/rules.json","r+")
	 jsonfile = filejson.read()
	  
	 instances = json.loads(jsonfile)
         filejson.close()
         ret = []
         for inst in instances:
                ret.append(ruleBean(inst['id'],inst['Description'],inst['SignatureCount']))

         return ret


class AddRulesView(forms.ModalFormView):
      template_name = 'mydashboard/snortrules/add.html'
      modal_header = _("Add Rule")
      form_id = "add_rule_form"
      form_class = project_forms.AddRuleForm
      submit_label = _("Add Rule")
      submit_url = reverse_lazy("horizon:mydashboard:snortrules:add")
      success_url = reverse_lazy('horizon:mydashboard:snortrules:index')

      page_title=_("Add Rule")
