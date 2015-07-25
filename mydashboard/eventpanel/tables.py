from django.utils.translation import ugettext_lazy as _

from horizon import tables

class MyFilterAction(tables.FilterAction):
    name = "myfilter"

class InstancesTable(tables.DataTable):
    name = tables.Column("IPSource",
                         verbose_name=_("IPSource"))
    signaturecount = tables.Column("SignatureCount",verbose_name=_("SignatureCount"))
    #salary = tables.Column("salary", verbose_name=_("Salary in Rs"))
    #addr = tables.Column("addr",
    #                    verbose_name=_("Address"))
 
    class Meta:
        name = "emptable"
        verbose_name = _("Info Table")
        table_actions = (MyFilterAction,)
