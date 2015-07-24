

class SetAddDetailsAction(workflows.Action):
 
    providerActionsChoices = [(providerAction.id, providerAction.name) for providerAction in providerActions]
    providerChoices = [(provider.id, provider.name) for provider in providers]
 
    name = forms.CharField(
        label=_("Name"),
        required=True,
        max_length=80,
        help_text=_("Name"))
 
    description = forms.CharField(
        label=_("Description"),
        required=True,
        max_length=120,
        help_text=_("Description"))
 
    provider = forms.ChoiceField(
        label=_("Providers"),
        choices=providerChoices,
        required=True,
        help_text=_("Providers"))
 
    action = forms.ChoiceField(
        label=_("Provider Actions"),
        choices=providerActionsChoices,
        required=True,
        help_text=_("Provider Actions"))
