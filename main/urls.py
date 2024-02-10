from django import views
from django.urls import path
from .views import *

urlpatterns = [
   path("", say_hello),
   path("profile/", user_profile),
   path("filter_queries/<int:query_id>/",filter_queries),
   path("queries/", Queryview.as_view(), name="query-view"),
]