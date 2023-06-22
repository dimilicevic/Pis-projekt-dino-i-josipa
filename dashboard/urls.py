from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "dashboard"

urlpatterns = [
    path("offer/edit/<int:pk>/", views.OfferUpdateView.as_view(), name="edit-offer"),
    path("offer/create/", views.OfferCreateView.as_view(), name="create-offer"), 
    path("offer/createFirm/", views.FirmCreateView.as_view(), name="create-Firm"),
    path(
        "offer/delete/<int:pk>/", views.OfferDeleteView.as_view(), name="delete-offer"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
