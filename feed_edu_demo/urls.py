from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from feed_edu_demo import views, settings

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Feed-Edu Demo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
    path('feedback/', include('feedback.urls')),
    path('api/feedback/', include('feedback.API_urls')),
    path('api/users/', include('users.API_urls')),
    path('swagger/', schema_view),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
