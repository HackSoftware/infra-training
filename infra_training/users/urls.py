from django.urls import path

from infra_training.users.views import (
    cpu_view
)

app_name = "users"
urlpatterns = [
    path("~cpu-view/", view=cpu_view, name="cpu"),
]
