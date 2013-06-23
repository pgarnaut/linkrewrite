'''
    Created on Jun 22, 2013

    @author:  pgarnaut
'''
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from models import Link

@csrf_exempt
def index(request, link_name=None):

    if request.method == "POST":
        print "create new link"
        # TODO:
        link = Link()
        print request.META
        link.redirect = request.META.get('HTTP_REDIRECT_URL', '')
        link.save()
        print link.link_name
        print request.POST.dict()
        return HttpResponse(content=link.link_name, status=200)
    
    
    elif request.method == "GET":
        if not link_name:
            return HttpResponse(400)
        
        print "get existing link"
        print "request: " + request.get_full_path()
        print "link requested: " + link_name
        
        obj = Link.objects.get(link_name=link_name)
        if not obj:
            return HttpResponse("invalid link", status=404)
        
        obj.save() # update access time
        
        if obj.redirect:
            resp = HttpResponseRedirect(obj.redirect)
        else:
            resp = HttpResponse(status=200)
            
        resp.content = obj.data
        return resp

    else:
        return HttpResponse(status=400)