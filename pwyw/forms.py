from django import forms

#from .models import UserSplitItem
from django.forms.models import modelformset_factory

# UserSplitItemForm = modelformset_factory(UserSplitItem, fields=('value',))

class UserSplitForm(forms.Form):
    def __init__(self, split_template, *args, **kwargs):
        super(UserSplitForm, self).__init__(*args, **kwargs)
        for product in split_template.products.all():
            self.fields['product_%d' % product.id] = forms.IntegerField(label=product.name)

