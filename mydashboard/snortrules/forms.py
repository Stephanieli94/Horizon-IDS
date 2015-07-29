import collections
import logging

import django
from django.conf import settings
from django.forms import ValidationError  # noqa
from django import http
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_variables  # noqa

from horizon import exceptions
from horizon import forms
from horizon import messages
from horizon.utils import functions as utils
from horizon.utils import validators

from openstack_dashboard import api


class AddRuleForm():

    domain_id = forms.CharField(label=_("Domain ID"),
                                required=False,
                                widget=forms.HiddenInput())
    domain_name = forms.CharField(label=_("Domain Name"),
                                  required=False,
                                  widget=forms.HiddenInput())
   # name = forms.CharField(max_length=255, label=_("User Name"))
    Description = forms.CharField(widget=forms.widgets.Textarea(
                                  attrs={'rows': 4}),
                                  label=_("Description"),
                                  required=False)
    
    # description = forms.CharField(
    #     label = _("Description"),
    #    required=True,
    #     max_length=120,
    #    help_text=_("Description"))
    SignatureCount = forms.CharField(
      
         required=False,
         label=_("SignatureCount"))
    #email = forms.EmailField(
    #    label=_("Email"),
    #    required=False)
    #project = forms.DynamicChoiceField(label=_("Primary Project"),
    #                                   required=PROJECT_REQUIRED,
    #                                   add_item_link=ADD_PROJECT_URL)
    #role_id = forms.ChoiceField(label=_("Role"),
    #                              required=PROJECT_REQUIRED)
    enabled = forms.BooleanField(label=_("Enabled"),
                                 required=False,
                                 initial=True)


    def __init__(self, *args, **kwargs):
        #roles = kwargs.pop('roles')
        #super(CreateUserForm, self).__init__(*args, **kwargs)
        # Reorder form fields from multiple inheritance
        ordering = ["domain_id", "domain_name",
                    "Description", "SignatureCount" 
                    "enabled"]

