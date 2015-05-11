from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^$', 'convergence.views.home', name='home'),
	# url(r'^convergence/', include('convergence.foo.urls')),

	url(r'^$', 'blog.views.home', name='home'),
	url(r'^article/(?P<postid>\w+)/', 'blog.views.article', name='article'),

	# Admin Pages
	url(r'^admin/home', 'blog.views.admin', name='admin'),
	url(r'^admin/posts/edit', 'blog.views.admin_edit_posts', name='edit_posts'),

	# login Pages
	url(r'^user/register', 'blog.views.user_register', name='user.register'),
)
