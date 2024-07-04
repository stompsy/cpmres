from django.urls import path
from directory.views import index, AgencyListView, AgencyDetailView

urlpatterns = [
    path("", index, name="index"),
    path("agencies/", AgencyListView.as_view(), name="agencies"),
    path("agency/<int:pk>", AgencyDetailView.as_view(), name="agency_detail"),
]
