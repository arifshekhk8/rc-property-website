from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("gallery/", views.gallery, name="gallery"),
    path("visit/", views.virtual_visit, name="virtual_visit"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("inquiry/", views.inquiry, name="inquiry"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
]
