"""django docstring"""
from django.contrib import admin
from django.urls import path, include
from employee import views
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show),
    path('emp', views.emp),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path("accounts/", include("django.contrib.auth.urls")),
]
