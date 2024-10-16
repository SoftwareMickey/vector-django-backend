from django.urls import path

from .views import MyApiView

urlpatterns = [
    path("models/", MyApiView.as_view(), name="connection")
    # path("connect", views.connecton_establishment_with_frontend, name="connection_establishment"),
    # path("predict", views.post_data_and_predict, name="post_request")
]
