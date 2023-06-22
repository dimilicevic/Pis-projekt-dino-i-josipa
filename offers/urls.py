from django.urls import path

from . import views
from dashboard.views import OfferUpdateView,OfferDeleteView,CompanyUpdateView,CompanyDeleteView

app_name = "offers"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("companies/", views.CompaniesListView.as_view(), name="companies-list"),
    path("offer/<int:pk>/", views.OfferDetailView.as_view(), name="offer-detail"),
    path("company/<int:pk>/", views.CompanyDetailView.as_view(), name="company-detail"),
    path(
        "dashboard/offer/edit/<int:offer_id>/", OfferUpdateView.as_view(), name="edit-offer"
    ),
    path(
        "dashboard/offer/delete/<int:offer_id>/", OfferDeleteView.as_view(), name="delete-offer"
    ),
    path(
        "dashboard/offer/edit_company/<int:pk>/", CompanyUpdateView.as_view(), name="edit-company"
    ),
    path(
        "dashboard/offer/delete_company/<int:pk>/", CompanyDeleteView.as_view(), name="delete-company"
    ),
]
