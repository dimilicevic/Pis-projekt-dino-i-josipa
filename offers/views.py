from typing import Any, Dict

from dashboard.models import Posao,Firma
from django.db.models import QuerySet
from django.views.generic import ListView, DetailView
from django.forms import Textarea

from .forms import (
    DateSortingForm,
    SearchForm,
    
)

class HomePageView(ListView):

    model = Posao
    template_name = "home_page.html"
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:

        queryset = super().get_queryset()

        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(naziv_posla__icontains=name)

        positions = self.request.GET.getlist("localization")
        if positions:
            queryset = queryset.filter(firma__in=positions)

        order_by2 = self.request.GET.get("order_by")

        if order_by2:
            if order_by2 == "1":
                queryset = queryset.order_by("datum_izrade")
            if order_by2 == "2":
                queryset = queryset.order_by("-datum_izrade")

 
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context["date_sorting_form"] = DateSortingForm(self.request.GET)
        context["search_form"] = SearchForm(self.request.GET) 

        return context

class CompanyDetailView(DetailView):

    model = Firma
    template_name = "company_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context["object_list"] = Posao.objects.filter(firma=self.kwargs["pk"])
        return context

class OfferDetailView(DetailView):

    model = Posao
    template_name = "offer_detail.html"
    fields = [
        "naziv_posla",
        "opis_posla",
        "placa",
        "lokacija",
        "kontakt_osobe",
        "firma",
        "image",
    ]
    widgets = {
            'text': Textarea(attrs={'rows':5, 'cols':10}),
        }   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompaniesListView(ListView):

    model = Firma
    paginate_by = 10
    template_name = "companies_list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

