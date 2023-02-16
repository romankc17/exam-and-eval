from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("exam.urls")),
    path("accounts/", include("authentication.urls")),
]
