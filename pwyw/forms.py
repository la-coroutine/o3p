from django import forms

from .models import UserSplitItem
from django.forms.models import modelformset_factory

UserSplitItemForm = modelformset_factory(UserSplitItem, fields=('value',))

class UserSplitForm(forms.Form):
    def __init__(self, split_template, *args, **kwargs):
        super(UserSplitForm, self).__init__(*args, **kwargs)
        for item in split_template.items.all():
            self.fields['item_%d' % item.id] = forms.IntegerField(label=item.label, initial=item.default)

