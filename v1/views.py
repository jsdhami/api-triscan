from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    # redirect to https://triscan.jsdhami.com.np for now
    # return HttpResponse('<script>window.location.href="https://triscan.jsdhami.com.np"</script>')
    return HttpResponse("Hello, This is the Triscan API. Please visit https://triscan.jsdhami.com.np for more information.")   


class CheckPlagiarismView(APIView):
    def post(self, request):
        text = request.data.get('text')
        # Implement plagiarism checking logic here
        result = {'similarity': 0.95}  # Dummy response
        return Response(result, status=status.HTTP_200_OK)

class ReportView(APIView):
    def get(self, request, id):
        # Retrieve the report by id
        report = {'id': id, 'similarity': 0.95}  # Dummy response
        return Response(report, status=status.HTTP_200_OK)


