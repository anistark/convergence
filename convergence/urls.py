from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^$', 'convergence.views.home', name='home'),
	# url(r'^convergence/', include('convergence.foo.urls')),

	url(r'^$', 'blog.views.home', name='home'),
	url(r'^post/', 'blog.views.post', name='post'),

	# Admin Pages
	url(r'^admin/home', 'blog.views.admin', name='admin'),
	url(r'^admin/posts/edit', 'blog.views.admin_edit_posts', name='edit_posts'),

	# login Pages
	url(r'^login_register/', 'blog.views.login_register', name='login_register'),
)
