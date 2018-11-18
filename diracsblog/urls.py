from django.contrib import admin
from django.conf.urls import url
import posts.views
import sitepages.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', posts.views.home, name='home'),
    url(r'^posts/(?P<post_id>[1-9]+)/$', posts.views.post_details, name='post_details'),
    url(r'^about', sitepages.views.about, name='about'),
    url(r'^contact$',  sitepages.views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
