from horizon import views


from django.shortcuts import render
from horizon import tables
from .tables import InstancesTable
import json 
from .EventBean import EventBean
import subprocess 
class IndexView(tables.DataTableView):
#    tab_group_class = mydashboard_tabs.MypanelTabs
    table_class = InstancesTable
    template_name = 'mydashboard/eventspanel/index.html'
    def get_data(self):
#	 subprocess.call(["ls"])
#	 subprocess.call(["python", "opt/stack/event.py"])
#        strobj = '[{"id": 111, "name": "emp1", "salary": 1000, "addr": "kolkata"}, {"id": 222, "name": "emp2", "salary": 5000, "addr": "bangalore"}]'
#        strobj = '[{"id": 1, "TotCount": 11111}]'
#	instances = json.loads(strobj)
	 filejson = open("/opt/stack/events.json","r+")
	 jsonfile = filejson.read()
	  
	 instances = json.loads(jsonfile)
         filejson.close()
         ret = []
         for inst in instances:
            #ret.append(Employee(inst['id'], inst['name'], inst['addr'], inst['salary']))

             ret.append(EventBean(inst['id'],inst['IPSource'],inst['SignatureCount']))
#	     print(EventBean(inst['IPSource'])

#        db = MySQLdb.connect(user='root', db='snort', passwd='password', host='localhost')
#        cursor = db.cursor()
#        cursor.execute("SELECT VERSION()")
#        data = cursor.fetchone()
#        print "Database version : %s " % data
#        db.close()
#        hello()        
         return ret 






