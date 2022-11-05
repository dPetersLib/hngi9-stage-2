from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['POST'])
def enum(request):
    error = None
    operations = ['addition', 'subtraction', 'multiplication']
    op = request.data["operation_type"]
    x = request.data["x"]
    y = request.data["y"]

    if op not in operations:
        error = 'Invalid operation type'
    if op not in operations:
        error = 'Invalid operation type. Options: <addition | subtraction | multiplication>'
    if type(x) is not int:
        error = 'x operand must be an integer'
    if type(y) is not int:
        error = 'y operand must be an iteger'

    if error:
        return JsonResponse({'msg': error}, status=400)

    if op == 'addition':
        result = x + y
    elif op == 'subtraction':
        result = x + y
    else:
        result = x * y
    return JsonResponse({
        'slackUsername': 'edoka',
        'result': result,
        'operation_type': op,
    }, status=200)
