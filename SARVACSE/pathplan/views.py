from django.shortcuts import render
from django.views.generic import TemplateView
import json
from django.http import HttpResponse,HttpResponseRedirect
import os

# Create your views here.

class BaseTemplate(TemplateView):
    template_name='pathplan/index.html'

class PathPlan3D(TemplateView):
    template_name='pathplan/3DPathSAR.html'

    def getpath(request):
        # Get the current working directory
        #cwd = os.getcwd()
        # Print the current working directory
        #print("Current working directory: {0}".format(cwd))

        pathfile="./static/data/path_1.json"
        #print("already in python")
        with open(pathfile) as f:
            data=json.load(f)
            if request.method == 'POST':
                context={'data':data,'flag':'success'}
                return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('FAIL!!!!!')
