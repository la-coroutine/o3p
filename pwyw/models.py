from django.db import models
from django.contrib.auth.models import User

from shop.models import Product

class SplitTemplate(models.Model):
   label = models.CharField(max_length=255,
                            blank=True,
                            null=True)

   products = models.ManyToManyField(Product)

   def __unicode__(self):
       return self.label

# class SplitItemTemplate(models.Model):
#     label = models.CharField(max_length=255,
#                              blank=True,
#                              null=True)

#     min = models.PositiveIntegerField()
#     max = models.PositiveIntegerField()
#     default = models.PositiveIntegerField()

#     split_template = models.ForeignKey(SplitTemplate, related_name='items')

#     def __unicode__(self):
#         return self.label



class UserSplit(models.Model):
    template = models.ForeignKey(SplitTemplate)
    items = models.ManyToManyField(Product) #,
                                   # through='UserSplitItem')
    user = models.ForeignKey(User)

    created_on = models.DateTimeField(auto_now_add=True)

    @property
    def amount(self):
        return sum([item.value for item in self.splititems.all()])
    
    def __unicode__(self):
        return u"%s for %s" % (self.user,
                               self.template)

#class UserSplitItem(models.Model):
#    usersplit = models.ForeignKey(UserSplit, related_name='splititems')
#    splititem_template = models.ForeignKey(SplitItemTemplate)
#    value = models.PositiveIntegerField()
    

    
