from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.models import Employe
from api.serializer import EmpSerializer

# Create your views here.

class EmpView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Employe.objects.all()
        serializer=EmpSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employe.objects.get(id=id)
        serializer=EmpSerializer(qs)
        return Response(data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=Employe.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"})

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employe.objects.get(id=id)
        serializer=EmpSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)