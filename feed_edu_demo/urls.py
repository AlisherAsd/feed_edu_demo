from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from feed_edu_demo import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
    path('feedback/', include('feedback.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
