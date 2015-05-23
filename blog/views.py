from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from models import Post, User
import datetime
import uuid
import re
# from django.contrib.auth.hashers import make_password, check_password

# from .forms import EditPosts

# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-last_update')
    context = {'title': 'Convergence', 'posts': posts}
    return render_to_response(
        'index.html',
        context,
        context_instance=RequestContext(request))


def article(request, postid):
    posts = Post.objects.get(post_url=postid)
    context = {'title': 'Convergence | Post', 'post': posts}
    return render_to_response(
        'post.html',
        context,
        context_instance=RequestContext(request))


def admin(request):
    context = {'title': 'Convergence | Admin'}
    return render_to_response(
        'admin/index.html',
        context,
        context_instance=RequestContext(request))


def admin_edit_posts(request):
    if request.method == 'POST' or request.method == 'FILES':
        # save new post
        title = request.POST['title']
        # print(request.POST[all])
        admin_username = 'anistark'
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
        context_instance=RequestContext(request))


# def admin_edit_posts(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST' or request.method == 'FILES':
#         # create a form instance and populate it with data from the request:
#         form = EditPosts(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('admin.edit_posts')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = EditPosts()

#     context = {'title': 'Convergence | Edit Post', 'form': form}
#     return render_to_response(
#         'admin/edit_posts.html',
#         context,
#         context_instance=RequestContext(request))


def user_register(request):
    if request.method == 'POST' or request.method == 'FILES':
        if(re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', request.POST['email'])):
            user_password = request.POST['password']
            user = User()
            user.email = request.POST['email']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.username = request.POST['user_name']
            user.password = user_password
            user.signuptime = datetime.datetime.now()
            user.save()
        else:
            print 'email is invalid'
    user = User.objects.all()
    context = {'title': 'Convergence | Welcome', 'user': user}
    return render_to_response(
        'index.html',
        context,
        context_instance=RequestContext(request))


def user_login(request):
    if request.method == 'POST':
        input_email = request.POST['email']
        if(re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', input_email)):
            user_password = request.POST['password']
            user = User.objects.get(email=input_email)
            if(user):
                if(user.password != user_password):
                    # false
                    context = {'title': 'Convergence | Welcome'}
                    return render_to_response(
                        'index.html',
                        context,
                        context_instance=RequestContext(request))
                else:
                    # login
                    context = {'title': 'Convergence | Welcome ', 'user': user}
                    return redirect('user.profile', user.username)
                    # return render_to_response(
                    #     'user/profile.html',
                    #     context,
                    #     context_instance=RequestContext(request))
            else:
                print 'email is invalid'


def user_profile(request, username):
    user = User.objects.get(username=username)
    context = {'title': 'Convergence | My Profile', 'user': user}
    return render_to_response(
        'user/profile.html',
        context,
        context_instance=RequestContext(request))
