'''
    Created on Jun 22, 2013

    @author:  pgarnaut
'''

from django.db import models
from django.db.models.signals import post_save
import uuid

def gen_uuid():
    return uuid.uuid4().hex

MAX_LINK_COUNT = 5

class Link(models.Model):
    class Meta:
        ordering = ['access_time']
        
    create_time = models.DateTimeField(auto_now=True, db_index=False)
    access_time = models.DateTimeField(auto_now=True, db_index=True)
    link_name = models.CharField(max_length=200, default=gen_uuid, editable=False, db_index=True)
    description = models.CharField(max_length=100, editable=True)
    data = models.CharField(max_length=1000, editable=True)
    redirect = models.CharField(max_length=500, editable=False) 

def prune_links(sender, **kwargs):
    count = Link.objects.count()
    while count > MAX_LINK_COUNT:
        print "we have %d links: pruning" % count
        # i think this wont actually try to get ALL links?
        Link.objects.all()[0].delete()
        count = Link.objects.count()
        
post_save.connect(receiver=prune_links, sender=Link)