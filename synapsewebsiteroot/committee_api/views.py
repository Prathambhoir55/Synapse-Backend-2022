from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
# Create your views here.

class CoreAPI(APIView):
    def get (self, request):
        core_objs = CoreCommittee.objects.all()
        dicty = {1:'Chair person',2:'Co-chair person',3:'Admin & secretary',4:'ML Head',5:'Tech Head',6:'Creative Head',7:'Events & PR Head',8:'Marketing Head'}
        for i in core_objs:
            if i.Position in dicty:
                i.Position = dicty[i.Position]
        _data = CoreCommitteeSerilalizer(core_objs, many = True)
        return Response({'status':200, 'payload': _data.data})

class ExMemberAPI(APIView):
    def get (self, request):
        excore_objs = Exmembers.objects.all()
        dicty = {1:'Chair person',2:'Co-chair person',3:'Admin & secretary',4:'ML Head',5:'Tech Head',6:'Creative Head',7:'Events & PR Head',8:'Marketing Head',9:'Founder'}
        for i in excore_objs:
            if i.Position in dicty:
                i.Position = dicty[i.Position]
        _data = ExMemberbersSerilalizer(excore_objs, many = True)
        return Response({'status':200, 'payload': _data.data})

class FacultyAPI(APIView):
    def get (self, request):
        fac_objs = Faculty.objects.all()
        _data = FacultySerilalizer(fac_objs, many = True)
        return Response({'status':200, 'payload': _data.data})