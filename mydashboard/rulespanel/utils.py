import traceback
import time
from time import mktime
from datetime import datetime
from requests.auth import HTTPBasicAuth
import subprocess
from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _
import requests
import json 
from horizon import exceptions
import time
#import math
import random
requests.packages.urllib3.disable_warnings()

 
integra_url = "https://146.118.97.140:8000/mydashboard"
json_headers = {'Accept': 'application/json'}
json_file = '/opt/stack/h-json/test.json' 
json_rules_script = '/opt/stack/h-script/jsonToSnort.py'
class Provider:
 
    def __init__(self, id, action, protocal , sourceIP, sourcePort, direction, destinationIP, destinationPort, description, priority):
        self.id = id
	self.action = action
        self.protocal = protocal
        self.description = description
        self.sourceIP = sourceIP
        self.sourcePort = sourcePort
        self.direction = direction
        self.destinationIP = destinationIP
 	self.destinationPort = destinationPort
	self.priority = priority

def getProviders(self):
    try:
#        r = requests.get(integra_url + "/providers", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)
	subprocess.call(["python", json_rules_script])
#

	

#        subprocess.call(["python", "opt/stack/h-script/jsonToSnort.py"])

	filejson = open(json_file,"r+")
# 	filejson = open("/opt/stack/jsontorules.json","r+")
        jsonfile = filejson.read()
	providers= []
        instances = json.loads(jsonfile)
        filejson.close()

        for provider in instances:
            providers.append(Provider(provider[u'id'],provider[u'action'],provider[u'protocal'], provider[u'sourceIP'], provider[u'sourcePort'], provider[u'direction'], provider[u'destinationIP'], provider[u'destinationPort'], provider[u'description'], provider[u'priority']))
 
        return providers
 
    except:
        exceptions.handle(self.request,
                          _('Unable to get providers'))
        return []


def getProviderActions(self):
    try:
 
        r = requests.get(integra_url + "/provider_actions/" + id, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)
 
        providerActions = []
        for providerAction in r.json()['providerActions']:
            providerActions.append(ProviderAction(providerAction[u'id'], providerAction[u'name'], providerAction[u'description']))
 
        return providerActions
 
    except:
        exceptions.handle(self.request,
                          _('Unable to retrieve list of posts.'))
        return []
 
# request - horizon environment settings
# context - user inputs from form
''' when user enter inputs , they will be stored in a json file 
    which could be displayed on the dashboard  '''
def addProvider(self, request, context):



    try:
	action = context.get('action') 
        protocal = context.get('protocal')
        description = context.get('description')
        sourceIP = context.get('sourceIP')
        sourcePort = context.get('sourcePort')
        direction = context.get('direction')
        destinationIP = context.get('destinationIP')
        destinationPort = context.get('destinationPort')
        priority = context.get('priority')
       
 	# ranNum = str(time.time())
	ranNum = str(random.randint(5000005, 5999999))

#this is a hard code, we suppose to use http send info to nova, and nova api should somehow give this info an id
        payload ={'id':ranNum,'action':action,'protocal': protocal, 'description': description, 'sourceIP': sourceIP, 'sourcePort': sourcePort, 'direction': direction, 'destinationIP': destinationIP , 'destinationPort' : destinationPort ,'priority':priority}
#        requests.post(integra_url + "/rulespanel", json=payload, verify=False, auth=HTTPBasicAuth('admin', 'mydashboard'), headers=json_headers)
#	event_json = json.dumps(payload)
	filejson = open(json_file,"r+")
#	with open(json_file, 'r') as f:
#		json.dump([], f)	
	jsonfile = filejson.read()
	instances = json.loads(jsonfile)
	
	with open(json_file, 'w') as feedsjson:
    		
    		instances.append(payload)
    		json.dump(instances, feedsjson)
	feedsjson.close()
	filejson.close()
	subprocess.call(["python", json_rules_script])
    except:
        print "Exception inside utils.addProvider"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to add provider'))
        return []
 
# id is required for table
def deleteProvider(self, id):
    try:
 
#        requests.delete(integra_url + "/providers/" + id, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)
	filejson = open(json_file,"r+")
	instances  = json.load(filejson)
# Iterate through the objects in the JSON and pop (remove)                      
# the obj once we find it.                                                      
	for i in xrange(len(instances)):
    		if instances[i]["id"] == id:
			print(id)
        		instances.pop(i)
        		break

# Output the updated file with pretty JSON                                      
        with open(json_file, 'w') as feedsjson:
                json.dump(instances, feedsjson)
        feedsjson.close()
        filejson.close()
    except:
        print "Exception inside utils.deleteProvider"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to delete provider'))
        return False
