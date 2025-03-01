from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from feed_edu_demo import views, settings

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Feed-Edu Demo')

urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), # Вход / регистрация (django template)
    path('users/', include('users.urls')), # Приложение роботающее с юзерами, ролями TEMPLATE
    path('feedback/', include('feedback.urls')), # Прирложение работающее с опросниками, ответами, типами TEMPLATE
    path('api/feedback/', include('feedback.API_urls')), # Прирложение работающее с опросниками, ответами, типами REST
    path('api/users/', include('users.API_urls')),  # Приложение роботающее с юзерами, ролями REST

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
