from django.urls import path
from . import views
from .views import redirect_view

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.portfolio_view, name="contact"),
    path("project/<int:id>/", views.project, name="projects"),
    path('redirect/', redirect_view, name="redirect"),
]

