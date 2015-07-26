from django.utils.translation import ugettext_lazy as _

from horizon import tables

class MyFilterAction(tables.FilterAction):
    name = "myfilter"



class AddTableData(tables.LinkAction):
    name = "add"
    verbose_name = _("Add Rules")
    icon = "plus"
    url = "horizon:mydashboard:snortrules:add"
    classes = ("btn-launch", "ajax-modal")


class UpdateRow(tables.Row):
    ajax = True
 
    def get_data(self, request, post_id):
        pass

class ProviderTable(tables.DataTable):
    id = tables.Column("id",
                          verbose_name=_("Id"))

    name = tables.Column("Description",
                          verbose_name=_("Description"))

    description = tables.Column("SignatureCount",
                          verbose_name=_("SignatureCount"))


class InstancesTable(tables.DataTable):
    name = tables.Column("Description",
                         verbose_name=_("Description"))
    signaturecount = tables.Column("SignatureCount",verbose_name=_("SignatureCount"))
    #salary = tables.Column("salary", verbose_name=_("Salary in Rs"))
    #addr = tables.Column("addr",
    #                    verbose_name=_("Address"))
 
    class Meta:
        name = "emptable"
        verbose_name = _("Info Table")
        row_class = UpdateRow
        table_actions = (MyFilterAction,AddTableData,)
