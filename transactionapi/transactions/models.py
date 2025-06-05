from django.db import models

class Transaction(models.Model):
    class TransactionTypes(models.TextChoices):
        DEPOSIT = "DEPOSIT", "Deposit"
        WITHDRAWAL = "WITHDRAWAL", "Withdrawal"

    transaction_type = models.CharField(choices=TransactionTypes, max_length=10)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=18, blank=True, default='')

    def __str__(self):
        return f"{self.transaction_type} {self.amount}"