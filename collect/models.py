from django.db import models
from django.contrib.auth.models import User

class Collect(models.Model):
    label = models.CharField(max_length=255)
    deadline = models.DateTimeField(blank=True,
                                    null=True)
    
    @property
    def collected_amount(self):
        return sum([contribution.amount for contribution in self.contributions.all()])
    
    @property
    def target_amount(self):
        return sum([item.amount for item in self.items.all()])

    def __unicode__(self):
        return self.label
    
class CollectItem(models.Model):
    collect = models.ForeignKey(Collect, related_name='items')
    label = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()

    def __unicode__(self):
        return self.label

class Contribution(models.Model):
    collect = models.ForeignKey(Collect, related_name='contributions')
    user = models.ForeignKey(User)
    amount = models.PositiveIntegerField()
