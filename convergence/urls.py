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
	url(r'^admin/', 'blog.views.admin', name='admin'),
)
