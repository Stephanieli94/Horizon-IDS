
from horizon import views
from django.shortcuts import render
from horizon import tables
from .tables import InstancesTable
from .tables import InstancesTable2
import json 
from .CountBean import CountBean , CountBean2 , CountBean3
#from .CountBean2 import CountBean2
import subprocess 
import time
from django.utils.translation import ugettext_lazy as _
from openstack_dashboard.dashboards.mydashboard.mypanel \
     import tables as project_tables
class IndexView(tables.MultiTableView):
#    tab_group_class = mydashboard_tabs.MypanelTabs
    table_classes = (project_tables.InstancesTable,
                     project_tables.InstancesTable2,
                     project_tables.InstancesTable3,)
    template_name = 'mydashboard/mypanel/index.html'
    page_title = _("Alert Dashboard")
    def get_instances1_data(self):
#	 subprocess.call(["ls"])
	 subprocess.call(["python", "/opt/stack/h-script/priority.py"])
#        strobj = '[{"id": 111, "name": "emp1", "salary": 1000, "addr": "kolkata"}, {"id": 222, "name": "emp2", "salary": 5000, "addr": "bangalore"}]'
#         strobj = '[{"id": 1, "ToCount": 11111}]'
#         instances2 = json.loads(strobj)
	 time.sleep(1)
	 filejson = open("/opt/stack/h-json/priority.json","r+")
	 jsonfile = filejson.read()
	  
	 instances = json.loads(jsonfile)
         filejson.close()
         ret = []
         rat = []
         for inst in instances:
            #ret.append(Employee(inst['id'], inst['name'], inst['addr'], inst['salary']))

           ret.append(CountBean(inst['cid'],inst['sig_priority'],inst['timestamp']))
#         for i in instances2:  
#           rat.append(CountBean2(i['id'],i['ToCount']))
#	    print(Employee(inst['TotCount'])

#        db = MySQLdb.connect(user='root', db='snort', passwd='password', host='localhost')
#        cursor = db.cursor()
#        cursor.execute("SELECT VERSION()")
#        data = cursor.fetchone()
#        print "Database version : %s " % data
#        db.close()
#        hello()        
         return ret   

    def get_instances2_data(self):
         #        subprocess.call(["ls"])
#         subprocess.call(["python", "/opt/stack/h-script/triggering.py"])
#        strobj = '[{"id": 111, "name": "emp1", "salary": 1000, "addr": "kolkat$
#         strobj = '[{"id": 1, "ToCount": 11111}]'
#         instances2 = json.loads(strobj)
         time.sleep(1)
         filejson = open("/opt/stack/h-json/triggering.json","r+")
         jsonfile = filejson.read()

         instances = json.loads(jsonfile)
         filejson.close()
         ret = []
         rat = []
         for inst in instances:
            #ret.append(Employee(inst['id'], inst['name'], inst['addr'], inst['$

           ret.append(CountBean2(inst['id'],inst['ip_src'],inst['count']))
#         for i in instances2:
#           rat.append(CountBean2(i['id'],i['ToCount']))
#           print(Employee(inst['TotCount'])

#        db = MySQLdb.connect(user='root', db='snort', passwd='password', host=$
#        cursor = db.cursor()
#        cursor.execute("SELECT VERSION()")
#        data = cursor.fetchone()
#        print "Database version : %s " % data
#        db.close()
#        hello()
         return ret
 


    def get_instances3_data(self):
         storebj = '[{"id": 1, "TCount": 11122}]'
         instances3 = json.loads(storebj)
         r = []
         for i in instances3:
           r.append(CountBean3(i['id'],i['TCount']))
         return r
