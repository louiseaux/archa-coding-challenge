from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Transaction

class TransactionViewsTestCase(APITestCase):
    def setUp(self):
        self.valid_tx = {
            "transaction_type": "DEPOSIT",
            "amount": 100,
            "description": "Initial deposit"
        }
        self.invalid_amount = {
            "transaction_type": "DEPOSIT",
            "amount": -100,
            "description": "Invalid amount"
        }
        self.invalid_type = {
            "transaction_type": "INVALID",
            "amount": 25,
            "description": "Invalid type"
        }
        self.missing_amount = {
            "transaction_type": "WITHDRAWAL",
            "description": "Missing amount"
        }
        self.missing_type = {
            "amount": 75,
            "description": "Missing amount"
        }
        
    def test_create_transaction_valid(self):
        '''
        Ensure we can create a new transaction object
        '''
        response = self.client.post(reverse('transaction-list'), self.valid_tx, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.get().description, 'Initial deposit')

    def test_create_transaction_invalid_amount(self):
        '''
        Validate negative amount is rejected
        '''
        response = self.client.post(reverse('transaction-list'), self.invalid_amount, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_transaction_invalid_type(self):
        '''
        Validate we cannot create a new transaction object with invalid type
        '''
        response = self.client.post(reverse('transaction-list'), self.invalid_type, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_transaction_missing_amount(self):
        '''
        Validate transaction type is required
        '''
        response = self.client.post(reverse('transaction-list'), self.missing_amount, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_transaction_missing_type(self):
        '''
        Validate amount is required
        '''
        response = self.client.post(reverse('transaction-list'), self.missing_type, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_transactions(self):
        '''
        Ensure we can get a list of all transactions
        '''
        self.client.post(reverse('transaction-list'), self.valid_tx, format='json')
        self.client.post(reverse('transaction-list'), self.valid_tx, format='json')
        response = self.client.get(reverse('transaction-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_transaction_by_id(self):
        '''
        Ensure we can retrieve transactions by their id
        '''
        response = self.client.post(reverse('transaction-list'), self.valid_tx, format='json')
        tx_id = response.data['id']
        response = self.client.get(reverse('transaction-detail', args=[tx_id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'transaction_type': 'DEPOSIT', 'amount': '100.00', 'description': 'Initial deposit'})

    def test_transaction_by_invalid_id(self):
        '''
        Ensure non-existant transactions throw a 404
        '''
        response = self.client.get(reverse('transaction-detail', args=[404]), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)