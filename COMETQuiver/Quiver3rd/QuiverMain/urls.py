from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views


admin.autodiscover()
urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^homescreen/$', views.homescreen, name='home'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_view, name='login page'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.view_profile, name='user profile'),
    url(r'^editprofile/$', views.edit_profile, name='update profile'),
    url(r'^project/$', views.add_project_view, name='project page'),
    url(r'^portfolio/$', views.portfolio_view, name='portfolio page'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)