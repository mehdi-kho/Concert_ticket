from django import forms
from ticketSales.models import ConcertModel


class SearchForm(forms.Form):
    searchText = forms.CharField(max_length=100, label="نام کنسرت مورد نظر را وارد کنید", required=False)


class ConcertForm(forms.ModelForm):
    class Meta:
        model = ConcertModel
        fields = ['name', 'singer_name', 'length', 'poster']
        # fields = ['name', 'singer_name', 'length']
        # exclude = ['poster'] # خط فوق را این طور هم می شود نوشت
