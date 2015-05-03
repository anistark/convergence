from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def home(request):
       context = {'title':'Convergence'}
       return render_to_response('index.html', context, context_instance=RequestContext(request))

def post(request):
       context = {'title':'Convergence | Post'}
       return render_to_response('post.html', context, context_instance=RequestContext(request))
