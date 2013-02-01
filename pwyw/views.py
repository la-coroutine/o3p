from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse

from .forms import UserSplitForm

from .models import SplitTemplate
from shop.models import Product
from shop.util.cart import get_or_create_cart

class SplitView(TemplateView):
    template_name = 'pwyw/split.html'

    def post(self, request, id, *args, **kwargs):
        split_template = get_object_or_404(SplitTemplate, id=id)        
        split_form = UserSplitForm(split_template, request.POST)

        # Make sure we empty the cart
        cart = get_or_create_cart(request, save=True)
        cart.delete()
        cart = get_or_create_cart(request, save=True)        
        
        if split_form.is_valid():
            for key, product_qtty in split_form.cleaned_data.iteritems():
                if key.startswith('product_'):
                    product_id = key.lstrip('product_')
                    product = get_object_or_404(Product, id=product_id)
                    cart.add_product(product, product_qtty)

        cart.save()

        return redirect(reverse('cart'))

    
    def get_context_data(self, id, *args, **kwargs):
        context = super(SplitView, self).get_context_data(*args, **kwargs)

        split_template = get_object_or_404(SplitTemplate, id=id)
        
        form = UserSplitForm(split_template)

        context['split_form'] = form
        context['split_template'] = split_template
        
        return context
    
