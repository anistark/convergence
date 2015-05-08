from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post
import datetime

# Create your views here.

def home(request):
       posts = Post.objects 
       context = {'title':'Convergence'}
       return render_to_response('index.html', {'Posts': posts}, context_instance=RequestContext(request))

def post(request):
       context = {'title':'Convergence | Post'}
       return render_to_response('post.html', context, context_instance=RequestContext(request))

def admin(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       content = request.POST['content']
       #print(request.POST[all])
       post = Post(title=title)
       post.last_update = datetime.datetime.now() 
       post.content = content
       post.save()
       context = {'title':'Convergence | Admin'}
    return render_to_response('admin/index.html',context_instance=RequestContext(request))