from django.urls import path
from .views import (
    book_property,
    create_property,
    properties_detail,
    properties_list,
    property_reservations,
    toggle_favorite,
)

urlpatterns = [
    path("", properties_list),
    path("create/", create_property),
    path("<uuid:pk>/", properties_detail),
    path("<uuid:pk>/book/", book_property),
    path("<uuid:pk>/reservations/", property_reservations),
    path("<uuid:pk>/toggle_favorite/", toggle_favorite),
]
