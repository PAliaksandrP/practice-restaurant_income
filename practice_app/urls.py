from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("income_prediction.urls")),
    path("admin/", admin.site.urls),
]
