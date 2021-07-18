from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from B2Blue import settings
from core import views

urlpatterns = [
                  path('', views.MovieTemplateView.as_view(), name='course_list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
