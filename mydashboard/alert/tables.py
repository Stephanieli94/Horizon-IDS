from django.utils.translation import ugettext_lazy as _

from horizon import tables

class MyFilterAction(tables.FilterAction):
    name = "myfilter"

class InstancesTable(tables.DataTable):
    name = tables.Column("IPSource",
                         verbose_name=_("IP Source"))
    signaturecount = tables.Column("SignatureCount",verbose_name=_("Signature Count"))
 
    class Meta:
        name = "emptable"
        verbose_name = _("Info Table")
        table_actions = (MyFilterAction,)
