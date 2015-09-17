from django.utils.translation import ugettext_lazy as _

from horizon import tables

class MyFilterAction(tables.FilterAction):
    name = "myfilter"

class InstancesTable(tables.DataTable):
   # event = tables.Column("Event",
   #                      verbose_name=_("Event"))
    sig_priority = tables.Column("sig_priority",
                         verbose_name=_("Priority"))
    timestamp = tables.Column("timestamp",
                         verbose_name=_("Timestamp"))
    #salary = tables.Column("salary", verbose_name=_("Salary in Rs"))
    #addr = tables.Column("addr",
    #                    verbose_name=_("Address"))
    class Meta(object):
         name = "instances1"
         hidden_title = False
         verbose_name = _("Latest High Priority Alerts")

 
class InstancesTable2(tables.DataTable):
    ip_src = tables.Column("ip_src",
                         verbose_name=_("IP"))
    count = tables.Column("count",
                         verbose_name=_("Event Count"))   
    class Meta(object):
         name = "instances2"
         hidden_title = False
         verbose_name = _("Top Offending IPs")
         table_actions = (MyFilterAction,)

class InstancesTable3(tables.DataTable):
    name = tables.Column("TCount" ,
                         verbose_name=_("Event"))
     
    class Meta(object):
        name = "instances3"
        hidden_title = False
        verbose_name = _("Top Alerts Count")
        table_actions = (MyFilterAction,)
