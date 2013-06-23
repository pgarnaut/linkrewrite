'''
    Created on Jun 22, 2013

    @author:  pgarnaut
'''
from django.contrib import admin
from permalink.linkrewrite.models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('access_time', 'create_time', 'link_name', 'redirect', 'description', 'data')
    search_fields = ['link_name', 'description']
    
admin.site.register(Link, LinkAdmin)
