from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from DjangoMedicalApp.models import Company
from DjangoMedicalApp.serializer import CompanySerializer


# Creating CompanyViewSet
class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def list(request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={"request": request})
        dict_response = {"error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(dict_response)

    @staticmethod
    def create(request):
        try:
            serializer = CompanySerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Company Data Saved Successfully"}
        except:
            dict_response = {"error": False, "message": "Error During Saving Company Data"}
        return Response(dict_response)

    @staticmethod
    def update(request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Company Data Updated Successfully"}
        except:
            dict_response = {"error": False, "message": "Error During Updating Company Data"}
        return Response(dict_response)


company_list = CompanyViewSet.as_view(actions={"get": "list"})
company_create = CompanyViewSet.as_view(actions={"post": "create"})
company_update = CompanyViewSet.as_view(actions={"put": "update"})
