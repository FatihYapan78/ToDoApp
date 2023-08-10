from django.contrib import admin
from django.urls import path
from Apptodo.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("filmdelete/<id>", FilmDelete, name="FilmDelete"),
]
