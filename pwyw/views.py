from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404

from .forms import UserSplitItemForm, UserSplitForm

from .models import UserSplit, UserSplitItem, SplitTemplate, SplitItemTemplate


class SplitView(TemplateView):
    template_name = 'pwyw/split.html'

    def post(self, request, id, *args, **kwargs):
        split_template = get_object_or_404(SplitTemplate, id=id)        
        split_form = UserSplitForm(split_template, request.POST)

        usersplit = UserSplit.objects.create(user=request.user,
                                             template=split_template)
        
        if split_form.is_valid():
            for key, value in split_form.cleaned_data.iteritems():
                if key.startswith('item_'):
                    splititem_template_id = key.lstrip('item_')
                    splititem_template = get_object_or_404(SplitItemTemplate, id=splititem_template_id)
                    UserSplitItem.objects.create(splititem_template=splititem_template,
                                                 usersplit=usersplit,
                                                 value=value)

        usersplit.save()

    
    def get_context_data(self, id, *args, **kwargs):
        context = super(SplitView, self).get_context_data(*args, **kwargs)

        split_template = get_object_or_404(SplitTemplate, id=id)
        
        form = UserSplitForm(split_template)

        context['split_form'] = form
        context['split_template'] = split_template
        
        return context
    
