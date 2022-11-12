from django.urls import path
from .views import *

urlpatterns = [
    path('core/', CoreAPI.as_view(), name = 'core'),
    path('exmember/', ExMemberAPI.as_view(), name = 'exmember'),
    path('faculty/', FacultyAPI.as_view(), name = 'faculty')
]
