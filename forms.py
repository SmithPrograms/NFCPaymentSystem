from django import forms
from .models import Customer


class LoyaltyCardForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number']


class LoyaltyCardCreationForm(forms.Form):
    card_number = forms.CharField(max_length=100)
    loyalty_identifier = forms.UUIDField()
    # Add more form fields
    
    def save(self):
        # Create a new LoyaltyCard object and save it to the database
        loyalty_card = LoyaltyCard(
            card_number=self.cleaned_data['card_number'],
            loyalty_identifier=self.cleaned_data['loyalty_identifier'],
            # Set other field values from the form data
        )
        loyalty_card.save()
        return loyalty_card
