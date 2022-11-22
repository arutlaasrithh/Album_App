from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("",views.home, name='home'),
    path("upload",views.upload, name='upload'),
    path("about",views.about, name='about'),
    path("gallery",views.gallery, name='gallery'),
    path("gallery/<int:pk>",views.delete_image, name='delete_image'),
    path("update",views.update, name='update'),
    path("update/<int:pk>",views.update_image, name='update_image')
]

urlpatterns += staticfiles_urlpatterns()