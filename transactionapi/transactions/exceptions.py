from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first to get standard error response
    response = exception_handler(exc, context)

    # Add HTTP status code to the response
    if response is not None:
        response.data['status_code'] = response.status_code
        
    return response