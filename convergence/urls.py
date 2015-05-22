from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^article/(?P<postid>\w+)/', 'blog.views.article', name='article'),

    # Admin Pages
    url(r'^admin/$', 'blog.views.admin', name='admin'),
    url(r'^admin/posts/edit',
        'blog.views.admin_edit_posts',
        name='admin.edit_posts'),

    # login/register Pages
    url(r'^user/register', 'blog.views.user_register', name='user.register'),

    # login/login Pages
    # url(r'^user/login', 'blog.views.user_login', name='user.login'),
    # login/forget password Pages
    # url(r'^user/forgetpasword',
    #     'blog.views.user_forgetpasword',
    #     name='user.forgetpasword'),

    # User Pages
    url(r'^user/(?P<userid>\w+)/',
        'blog.views.user_profile',
        name='user.profile'),
)
