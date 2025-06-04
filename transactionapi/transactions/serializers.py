from .models import Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_type', 'amount', 'description']

    def validate_amount(self, value):
        '''
        Check that amount is positive
        '''
        if value <= 0:
            raise serializers.ValidationError('Amount must be positive.')
        return value