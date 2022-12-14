from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.http import JsonResponse
# Create your views here.
class CoreAPI(GenericAPIView):
    serializer_class = CoreCommitteeSerilalizer
    def get (self, request):
        core_objs = CoreCommittee.objects.all()
        dicty = {1:'Chair person',2:'Co-chair person',3:'Admin & secretary',4:'ML Head',5:'Tech Head',6:'Creative Head',7:'Events & PR Head',8:'Marketing Head'}
        for i in core_objs:
            if i.Position in dicty:
                i.Position = dicty[i.Position]
        _data = CoreCommitteeSerilalizer(core_objs, many = True)
        return JsonResponse({'status':200, 'payload': _data.data})

class ExMemberAPI(GenericAPIView):
    serializer_class = ExMemberbersSerilalizer
    def get (self, request):
        excore_objs = Exmembers.objects.all()
        dicty = {1:'Chair person',2:'Co-chair person',3:'Admin & secretary',4:'ML Head',5:'Tech Head',6:'Creative Head',7:'Events & PR Head',8:'Marketing Head',9:'Founder'}
        for i in excore_objs:
            if i.Position in dicty:
                i.Position = dicty[i.Position]
        _data = ExMemberbersSerilalizer(excore_objs, many = True)
        return JsonResponse({'status':200, 'payload': _data.data})

class FacultyAPI(GenericAPIView):
    serializer_class = FacultySerilalizer
    def get (self, request):
        fac_objs = Faculty.objects.all()
        _data = FacultySerilalizer(fac_objs, many = True)
        return JsonResponse({'status':200, 'payload': _data.data})

class upcomming_events(GenericAPIView):
    serializer_class = EventSerializer
    def get (self, request):
        event_objs = Event.objects.filter(status = False)
        img = {}
        _data = EventSerializer(event_objs, many = True)
        for event in event_objs:
            img_objs = multi_image.objects.filter(event = event.id)
            _image = Multi_imageSerializer(img_objs, many = True)
            i=0
            img_list = []
            while i+1 <= len(_image.data):
                img_list.append(_image.data[i]['image'])
                i = i+1
            img[event.id] = _image.data
            i=0
            while i+1 <= len(_data.data):
                if(_data.data[i]['id'] != event.id):
                    i = i+1
                else:
                    _data.data[i]['images'] = img_list
                    break
        return JsonResponse({'status':200, 'payload': _data.data})

class past_events(GenericAPIView):
    serializer_class = EventSerializer
    def get (self, request):
        event_objs = Event.objects.filter(status = True)
        img = {}
        _data = EventSerializer(event_objs, many = True)
        for event in event_objs:
            img_objs = multi_image.objects.filter(event = event.id)
            _image = Multi_imageSerializer(img_objs, many = True)
            i=0
            img_list = []
            while i+1 <= len(_image.data):
                img_list.append(_image.data[i]['image'])
                i = i+1
            img[event.id] = _image.data
            i=0
            while i+1 <= len(_data.data):
                if(_data.data[i]['id'] != event.id):
                    i = i+1
                else:
                    _data.data[i]['images'] = img_list
                    break
        return JsonResponse({'status':200, 'payload': _data.data})

class ProjectAPI(GenericAPIView):
    serializer_class = ProjectsSerializer
    def get (self, request):
        Project_objs = Project.objects.all()
        img = {}
        _data = ProjectsSerializer(Project_objs, many = True)
        for event in Project_objs:
            img_objs = multi_image.objects.filter(event = event.id)
            _image = Projects_imageSerializer(img_objs, many = True)
            i=0
            img_list = []
            while i+1 <= len(_image.data):
                img_list.append(_image.data[i]['image'])
                i = i+1
            img[event.id] = _image.data
            i=0
            while i+1 <= len(_data.data):
                if(_data.data[i]['id'] != event.id):
                    i = i+1
                else:
                    _data.data[i]['images'] = img_list
                    break
        return JsonResponse({'status':200, 'payload': _data.data})