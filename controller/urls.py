from django.urls import path

from . import views

urlpatterns = [
    path("", views.connection_success, name="connection")
    # path("connect", views.connecton_establishment_with_frontend, name="connection_establishment"),
    # path("predict", views.post_data_and_predict, name="post_request")
]
