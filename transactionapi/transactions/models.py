from django.db import models

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=10)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=18, blank=True, default='')