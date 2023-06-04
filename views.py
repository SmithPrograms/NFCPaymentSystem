import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoyaltyCardForm
from .models import Customer, LoyaltyCard

def generate_unique_card_number():
    while True:
        card_number = str(random.randint(1000000000000000, 9999999999999999))
        try:
            LoyaltyCard.objects.get(card_number=card_number)
        except LoyaltyCard.DoesNotExist:
            return card_number

def loyalty_card_entry(request):
    if request.method == 'POST':
        form = LoyaltyCardForm(request.POST)
        if form.is_valid():
            # Create a new customer instance but don't save it yet
            customer = form.save(commit=False)

            # Create a new loyalty card and associate it with the customer
            card_number = generate_unique_card_number()
            loyalty_card = LoyaltyCard.objects.create(card_number=card_number)
            customer.loyalty_card = loyalty_card

            # Save the customer instance along with the associated loyalty card
            customer.save()

            # Retrieve the loyalty number associated with the saved card
            loyalty_number = loyalty_card.loyalty_identifier

            return render(request, 'loyalty_card_success.html', {'loyalty_number': loyalty_number})
    else:
        form = LoyaltyCardForm()

    return render(request, 'loyalty_card_entry.html', {'form': form})
