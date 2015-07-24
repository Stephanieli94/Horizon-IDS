from django.utils.translation import ugettext_lazy as _

from horizon import tables

class MyFilterAction(tables.FilterAction):
    name = "myfilter"

class InstancesTable(tables.DataTable):
    name = tables.Column("TotCount",
                         verbose_name=_("TotCount"))
    #salary = tables.Column("salary", verbose_name=_("Salary in Rs"))
    #addr = tables.Column("addr",
    #                    verbose_name=_("Address"))
 
    class Meta:
        name = "emptable"
        verbose_name = _("Info Table")
        table_actions = (MyFilterAction,)
