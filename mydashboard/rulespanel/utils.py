import traceback
import time
from time import mktime
from datetime import datetime
from requests.auth import HTTPBasicAuth
 
from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _
import requests
import json 
from horizon import exceptions
import time
requests.packages.urllib3.disable_warnings()

 
integra_url = "https://146.118.97.140:8000/mydashboard"
json_headers = {'Accept': 'application/json'}
 
class Provider:
    """
    Provider data
    """
 
    def __init__(self, id, name, description, hostname, port, timeout, secured):
        self.id = id
        self.name = name
        self.description = description
        self.hostname = hostname
        self.port = port
        self.timeout = timeout
        self.secured = secured
 
def getProviders(self):
    try:
#        r = requests.get(integra_url + "/providers", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)
#
	filejson = open("/opt/stack/horizon/openstack_dashboard/dashboards/mydashboard/rulespanel/rulesjson.json","r+")
 
        jsonfile = filejson.read()
	providers= []
        instances = json.loads(jsonfile)
        filejson.close()

        for provider in instances:
            providers.append(Provider(provider[u'id'], provider[u'name'], provider[u'description'], provider[u'hostname'], provider[u'port'], provider[u'timeout'], provider[u'secured']))
 
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
def addProvider(self, request, context):
    try:
 
        name = context.get('name')
        description = context.get('description')
        hostname = context.get('hostname')
        port = context.get('port')
        timeout = context.get('timeout')
        secured = context.get('secured')
 	ranNum = time.time()
#this is a hard code, we suppose to use http send info to nova, and nova api should somehow give this info an id
        payload = {'id':ranNum,'name': name, 'description': description, 'hostname': hostname, 'port': port, 'timeout': timeout, 'secured': secured}
#        requests.post(integra_url + "/rulespanel", json=payload, verify=False, auth=HTTPBasicAuth('admin', 'mydashboard'), headers=json_headers)
#	event_json = json.dumps(payload)
	filejson = open("/opt/stack/horizon/openstack_dashboard/dashboards/mydashboard/rulespanel/rulesjson.json","r+")
        json_file = '/opt/stack/horizon/openstack_dashboard/dashboards/mydashboard/rulespanel/rulesjson.json'
#	with open(json_file, 'r') as f:
#		json.dump([], f)	
	jsonfile = filejson.read()
	instances = json.loads(jsonfile)
	
	with open(json_file, 'w') as feedsjson:
    		
    		instances.append(payload)
    		json.dump(instances, feedsjson)
	feedsjson.close()
	filejson.close()
    except:
        print "Exception inside utils.addProvider"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to add provider'))
        return []
 
# id is required for table
def deleteProvider(self, id):
    try:
 
        requests.delete(integra_url + "/providers/" + id, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)
 
    except:
        print "Exception inside utils.deleteProvider"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to delete provider'))
        return False
