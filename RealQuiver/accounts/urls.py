from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin #<----                     !!!!! Uncomment
from . import views

admin.autodiscover()
urlpatterns = [
    url(r'^', include('addproject.urls')),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^homescreen/$', views.homescreen),
    url(r'^blog/$', views.Blog),
    url(r'^register/$', views.Register),
    url(r'^reg_success/$', views.Success),
    url(r'^error/$', views.login_error),
    url(r'^admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
