from horizon import views
from horizon import exceptions, tables, workflows, forms, tabs
 
from openstack_dashboard.dashboards.mydashboard.rulespanel.tables import ProviderTable
from openstack_dashboard.dashboards.mydashboard.rulespanel import utils
#from openstack_dashboard.dashboards.integra.providers.workflows.add_provider import AddProvider
from .add_provider import AddProvider

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class = ProviderTable
    template_name = 'mydashboard/rulespanel/index.html'

    def get_data(self):
        # Add data to the context here...
        return utils.getProviders(self)


class AddProviderView(workflows.WorkflowView):
      workflow_class = AddProvider

      def get_initial(self):
          initial = super(AddProviderView,self).get_initial()
          return initial
