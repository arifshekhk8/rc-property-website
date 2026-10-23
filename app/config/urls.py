from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from projects.views import project_image
from two_factor.urls import urlpatterns as two_factor_urls
from website.views import health

urlpatterns = [
    path("health/", health, name="health"),
    path("staff/", admin.site.urls),
    path("account/logout/", LogoutView.as_view(), name="logout"),
    path("", include(two_factor_urls)),
    path("i18n/", include("django.conf.urls.i18n")),
    path("images/<uuid:image_id>/", project_image, name="project_image"),
]
urlpatterns += i18n_patterns(path("", include("website.urls")))
