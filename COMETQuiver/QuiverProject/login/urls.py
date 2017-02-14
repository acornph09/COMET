from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^blog/$', views.Blog),
    url(r'^register/$', views.Register),
    url(r'^admin/', admin.site.urls),
    url(r'^reg_success/$', views.Success),
    url(r'^error/$', views.LogInError)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
