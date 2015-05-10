from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post, User
import datetime
import uuid

# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {'title': 'Convergence', 'posts': posts}
    return render_to_response(
        'index.html',
        context,
        context_instance=RequestContext(request)
      )


def post(request):
    posts = Post.objects.all()
    context = {'title': 'Convergence | Post', 'posts': posts}
    return render_to_response(
        'post.html',
        context,
        context_instance=RequestContext(request)
      )


def admin(request):
    context = {'title': 'Convergence | Admin'}
    return render_to_response(
        'admin/index.html',
        context,
        context_instance=RequestContext(request)
      )


def admin_edit_posts(request):
    if request.method == 'POST' or request.method == 'FILES':
        # save new post
        title = request.POST['title']
        # print(request.POST[all])
        post = Post(title=title)
        post.author = request.POST['author']
        post.last_update = datetime.datetime.now()
        post.content = request.POST['content']
        post.title_image = request.FILES['titleimgfile']
        post.post_url = str(uuid.uuid4().get_hex().upper()[0:16])
        post.save()
    context = {'title': 'Convergence | Edit Post'}
    return render_to_response(
        'admin/edit_posts.html',
        context,
        context_instance=RequestContext(request)
      )


def user_register(request):
    if request.method == 'POST' or request.method == 'FILES':
        user = User()
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.password = request.POST['password']
        user.signuptime = datetime.datetime.now()
        user.save()
    posts = Post.objects.all()
    context = {'title': 'Convergence | Welcome', 'posts': posts}
    return render_to_response(
        'index.html',
        context,
        context_instance=RequestContext(request)
      )
