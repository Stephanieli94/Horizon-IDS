# provide table to the dashboard

from django.utils.translation import ugettext_lazy as _

from horizon import tables
from openstack_dashboard.dashboards.mydashboard.rulespanel import utils

class MyFilterAction(tables.FilterAction):
    name = "myfilter"

'''class InstancesTable(tables.DataTable):
    name = tables.Column("name", verbose_name=_("Name"))
    status = tables.Column("status", verbose_name=_("Status"))
    zone = tables.Column('availability_zone',
                          verbose_name=_("Availability Zone"))
    image_name = tables.Column('image_name', verbose_name=_("Image Name"))
    class Meta:
        name = "instances"
        verbose_name = _("Instances")
        table_actions = (MyFilterAction,)
'''

class AddTableData(tables.LinkAction):
    name = "add"
    verbose_name = _("Add Rules")
    url = "horizon:mydashboard:rulespanel:add"
    classes = ("btn-launch", "ajax-modal")
 
class DeleteTableData(tables.DeleteAction):
    data_type_singular = _("Rulespanel")
    data_type_plural = _("Rulespanel")
 
    def delete(self, request, obj_id):
        utils.deleteProvider(self, obj_id)

 
class FilterAction(tables.FilterAction):
    def filter(self, table, providers, filter_string):
        filterString = filter_string.lower()
        return [provider for provider in providers
                if filterString in provider.title.lower()]
 
class UpdateRow(tables.Row):
    ajax = True
 
    def get_data(self, request, post_id):
        pass
 
class ProviderTable(tables.DataTable):
#    id = tables.Column("id",
#			  verbose_name=_("id"))
    action = tables.Column("action",
			  verbose_name=_("Action"))    

    protocal = tables.Column("protocal",
                          verbose_name=_("Protocal"))
 
    sourceIP = tables.Column("sourceIP",
                          verbose_name=_("SourceIP"))
 
    sourcePort = tables.Column("sourcePort",
                          verbose_name=_("SourcePort"))
 
    direction = tables.Column("direction",
                          verbose_name=_("Direction"))
 
    destinationIP = tables.Column("destinationIP",
                          verbose_name=_("DestinationIP"))
 
    destinationPort = tables.Column("destinationPort",
                          verbose_name=_("DestinationPort"))
    
    description = tables.Column("description",
                          verbose_name=_("Description"))
    priority = tables.Column("priority",
			  verbose_name=_("Priority")) 
    class Meta:
        name = "mydashboard"
        verbose_name = _("Rulespanel")
        row_class = UpdateRow
        table_actions = (AddTableData,
			 DeleteTableData,
                         FilterAction)
        row_actions = ()
