from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
# Create your views here.

class CoreAPI(APIView):
    def get (self, request):
        core_objs = CoreCommittee.objects.all()
        for i in core_objs:
            if i.Position == 1:
                i.Position = 'Chair person'
            elif i.Position == 2 : 
                i.Position = 'Co-chair person'
            elif i.Position == 3 : 
                i.Position = 'Admin & secretary'
            elif i.Position == 4 : 
                i.Position = 'ML Head'
            elif i.Position == 5 : 
                i.Position = 'Tech Head'
            elif i.Position == 6 : 
                i.Position = 'Creative Head'
            elif i.Position == 7 : 
                i.Position = 'Events & PR Head'
            elif i.Position == 8 : 
                i.Position = 'Marketing Head'
        _data = CoreCommitteeSerilalizer(core_objs, many = True)
        return Response({'status':200, 'payload': _data.data})

class ExMemberAPI(APIView):
    def get (self, request):
        excore_objs = Exmembers.objects.all()
        for i in excore_objs:
            if i.Position == 1:
                i.Position = 'Chair person'
            elif i.Position == 2 : 
                i.Position = 'Co-chair person'
            elif i.Position == 3 : 
                i.Position = 'Admin & secretary'
            elif i.Position == 4 : 
                i.Position = 'ML Head'
            elif i.Position == 5 : 
                i.Position = 'Tech Head'
            elif i.Position == 6 : 
                i.Position = 'Creative Head'
            elif i.Position == 7 : 
                i.Position = 'Events & PR Head'
            elif i.Position == 8 : 
                i.Position = 'Marketing Head'
            elif i.Position == 9 : 
                i.Position = 'Founder'
        _data = ExMemberbersSerilalizer(excore_objs, many = True)
        return Response({'status':200, 'payload': _data.data})

class FacultyAPI(APIView):
    def get (self, request):
        fac_objs = Faculty.objects.all()
        _data = FacultySerilalizer(fac_objs, many = True)
        return Response({'status':200, 'payload': _data.data})