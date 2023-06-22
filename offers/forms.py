from dashboard.models import (
    Firma,
)
from django import forms


class DateSortingForm(forms.Form):

    CHOICES = (("1", "Date - Oldest"), ("2", "Date - Newest"))

    order_by = forms.ChoiceField(
        choices=CHOICES,
        required=False,
    )


class SearchForm(forms.Form):

    name = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = False
        self.fields["name"].label = ""
        self.fields["name"].widget.attrs["placeholder"] = "Search by name"


class ApplyForm(forms.ModelForm):

    offer = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Firma
        fields = "__all__"
