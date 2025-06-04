from .models import Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount', 'description']

    def validate_transaction_type(self, value):
        '''
        Check that transaction type is either Deposit or Withdrawal
        '''
        if value not in ['DEPOSIT', 'WITHDRAWAL']:
            raise serializers.ValidationError('Transaction type must be either "DEPOSIT" or "WITHDRAWAL"')
        return value

    def validate_amount(self, value):
        '''
        Check that amount is positive
        '''
        if value <= 0:
            raise serializers.ValidationError('Amount must be positive.')
        return value