import datetime

from django import forms

from .models import Author, BookInstance

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).", widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.date.today(), 'max': datetime.date.today() + datetime.timedelta(weeks=4)}))

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
        widgets = {

            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'max': datetime.date.today()}),
            'date_of_death': forms.DateInput(attrs={'type': 'date', 'max': datetime.date.today() + datetime.timedelta(days=1)}),
            }

class BookInstanceForm(forms.ModelForm):

    class Meta:
        model = BookInstance
        fields = ['borrower', 'book', 'imprint', 'due_back', 'status']
        widgets = {

            'due_back': forms.DateInput(attrs={'type': 'date', 'min': datetime.date.today(), 'max': datetime.date.today() + datetime.timedelta(weeks=4)}),
            }
