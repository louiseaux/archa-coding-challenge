from .models import Transaction
from rest_framework import viewsets

from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions on transactions
    '''
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer