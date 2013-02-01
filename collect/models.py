from django.db import models
from django.contrib.auth.models import User

from shop.models import Product

class Collect(models.Model):
    label = models.CharField(max_length=255)
    deadline = models.DateTimeField(blank=True,
                                    null=True)

    products = models.ManyToManyField(Product,
                                      help_text="Products raising this collect")

    @property
    def collected_amount(self):
        return sum([contribution.amount for contribution in self.contributions.all()])
    
    @property
    def target_amount(self):
        return sum([product_collect.amount for product_collect in self.product_collects.all()])

    def __unicode__(self):
        return self.label
    

class CollectItem(models.Model):
    collect = models.ForeignKey(Collect)
    label = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()

class Contribution(models.Model):
    collect = models.ForeignKey(Collect, related_name='contributions')
    user = models.ForeignKey(User)
    amount = models.PositiveIntegerField()
