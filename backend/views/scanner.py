from backend.decorators import token_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.decorators import token_required


@api_view(['POST'])
@token_required
def scanner_photo(request):
    print(request)
    return Response({
        "message": "employee found",
        "data":
        {
            "id": "<employee_id>",
            "employee_name": "<employee_name>",
            "department_id": "<department_id>",
            "department_name": "<department_name>",
        },
    })
