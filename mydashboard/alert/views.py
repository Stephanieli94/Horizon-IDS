#Creater Jerome & Stephine
from horizon import views
from django.shortcuts import render
from horizon import tables
from .tables import InstancesTable
import json 
from .EventBean import EventBean
class IndexView(tables.DataTableView):
    table_class = InstancesTable
    template_name = 'mydashboard/alert/index.html'
    def get_data(self):
	 filejson = open("/opt/stack/events.json","r+")
	 jsonfile = filejson.read()
	  
	 instances = json.loads(jsonfile)
         filejson.close()
         ret = []
         for inst in instances:

             ret.append(EventBean(inst['id'],inst['IPSource'],inst['SignatureCount']))
         return ret 
