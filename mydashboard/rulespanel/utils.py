# Copyright 2015 ANU Hermes Team, Jerome Wang & Stephine Lee
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import traceback
import subprocess
import requests
import json 
import random

from horizon import exceptions
from requests.auth import HTTPBasicAuth
from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.mydashboard.rulespanel.workflow import constants

requests.packages.urllib3.disable_warnings()
 
#contants defination
json_headers = constants.json_headers
json_file = constants.json_file
json_rules_script = constants.json_rules_script


class Provider:
 
    def __init__(self, id, action, protocal , sourceip, sourceport, direction, destinationip, destinationport, msg, priority,rev):
        self.id = id
	self.action = action
        self.protocal = protocal
        self.msg = msg
        self.sourceip = sourceip
        self.sourceport = sourceport
        self.direction = direction
        self.destinationip = destinationip
 	self.destinationport = destinationport
	self.priority = priority
	self.rev = rev
def getProviders(self):
    try:
# the following is for HTTP requests sending json data, currently using local file read/write,
#subprocess call should be removed once snort are able to receive requests

#        r = requests.get(url_of_host + "/providers", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)
#	subprocess.call(["python", json_rules_script])

	filejson = open(json_file,"r+")
        jsonfile = filejson.read()
	providers= []
        instances = json.loads(jsonfile)
        filejson.close()

        for provider in instances:
            providers.append(Provider(provider[u'id'],provider[u'action'],provider[u'protocal'], provider[u'sourceip'], provider[u'sourceport'], provider[u'direction'], provider[u'destinationip'], provider[u'destinationport'], provider[u'msg'], provider[u'priority'], provider[u'rev']))
 
        return providers
 
    except:
        exceptions.handle(self.request,
                          _('Unable to get rules'))
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
        msg = context.get('msg')
        sourceip = context.get('sourceip')
        sourceport = context.get('sourceport')
        direction = context.get('direction')
        destinationip = context.get('destinationip')
        destinationport = context.get('destinationport')
        priority = context.get('priority')
#currently setting ID as random number, need to be changed later 
	ranNum = str(random.randint(5000005, 5999999))
	rev = 1
        payload ={'id':ranNum,'action':action,'protocal': protocal, 'msg': msg, 'sourceip': sourceip, 'sourceport': sourceport, 'direction': direction, 'destinationip': destinationip , 'destinationport' : destinationport ,'priority':priority, 'rev':rev}
#HTTP request below
#        requests.post(integra_url + "/rulespanel", json=payload, verify=False, auth=HTTPBasicAuth('admin', 'mydashboard'), headers=json_headers)
	filejson = open(json_file,"r+")
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

#HTTP request below 
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
