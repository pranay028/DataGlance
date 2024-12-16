from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .utils import generate_profiling_report
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
@api_view(['POST'])
def generate_report(request):
    # print(request)
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        print("in generate report")
        print('file')
        try:
            report_html, columns_info = generate_profiling_report(file)
            # print(columns_info)
            return JsonResponse({'report_html': report_html, 'columns_info':columns_info})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return JsonResponse({'error': 'File not provided'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def update_column(request):
    print(request)