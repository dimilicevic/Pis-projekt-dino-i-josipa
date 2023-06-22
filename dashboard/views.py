from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Posao,Firma


class OfferDeleteView(DeleteView):

    model = Posao
    success_url = "/"

class CompanyDeleteView(DeleteView):

    model = Firma
    success_url = "/"

class OfferCreateView(CreateView):

    model = Posao
    fields = [
        "naziv_posla",
        "opis_posla",
        "placa",
        "lokacija",
        "kontakt_osobe",
        "firma",
        "image",
    ]
    template_name = "create.html"
    success_url = "/"

class FirmCreateView(CreateView):

    model = Firma
    fields = [
        "naziv_firme",
        "opis",
        "industrija",
        "image",

    ]
    template_name = "create.html"
    success_url = "/"




class OfferUpdateView(UpdateView):

    model = Posao
    fields = [
        "naziv_posla",
        "opis_posla",
        "placa",
        "lokacija",
        "kontakt_osobe",
        "firma",
        "image",
    ]
    template_name = "update.html"
    success_url = "/"

class CompanyUpdateView(UpdateView):

    model = Firma
    fields = [
        "naziv_firme",
        "opis",
        "industrija",
        "image",

    ]
    template_name = "update.html"
    success_url = "/"