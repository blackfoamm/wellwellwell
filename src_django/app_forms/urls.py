from django.urls import path
from .views import login_view


app_name = "app_form"
urlpatterns = [
    path("login/", login_view, name="login"),
]