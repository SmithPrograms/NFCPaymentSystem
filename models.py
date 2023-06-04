from django.db import models
import uuid

class LoyaltyCard(models.Model):
    card_number = models.CharField(max_length=100, unique=True)
    loyalty_identifier = models.UUIDField(default=uuid.uuid4, editable=False)
    
    class Meta:
        app_label = 'myapp'
        
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    loyalty_card = models.OneToOneField(LoyaltyCard, on_delete=models.SET_NULL, null=True)

    @property
    def loyalty_number(self):
        if self.loyalty_card:
            return self.loyalty_card.loyalty_identifier
        return None

    
    loyalty_card = models.OneToOneField(LoyaltyCard, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'customer_table'
