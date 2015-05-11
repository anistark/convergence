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


def article(request, postid):
    posts = Post.objects.get(post_url=postid)
    context = {'title': 'Convergence | Post', 'post': posts}
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
        admin_username = 'anistark';
        post = Post(title=title)
        post.author = request.POST['author']
        post.last_update = datetime.datetime.now()
        post.content = request.POST['content']
        post.title_image = request.FILES['titleimgfile']
        post.post_url = str(uuid.uuid4().get_hex().upper()[0:16])
        post.added_by = admin_username
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
        user.username = request.POST['user_name']
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


def user_profile(request, userid):
    user = User.objects.get(id=userid)
    context = {'title': 'Convergence | My Profile', 'user': user}
    return render_to_response(
        'user/profile.html',
        context,
        context_instance=RequestContext(request)
      )

