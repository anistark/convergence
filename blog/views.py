from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post
import datetime
import uuid

# Create your views here.


def make_random_password(self, length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
    "Generates a random password with the given length and given allowed_chars"
    # Note that default value of allowed_chars does not have "I" or letters
    # that look like it -- just to avoid confusion.
    from random import SystemRandom as random
    return ''.join([random().choice(allowed_chars) for i in range(length)])


def home(request):
    posts = Post.objects
    context = {'title': 'Convergence'}
    return render_to_response(
        'index.html',
        {
          'Posts': posts
        },
        context_instance=RequestContext(request)
      )


def post(request):
    context = {'title': 'Convergence | Post'}
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
        # file upload
        
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
