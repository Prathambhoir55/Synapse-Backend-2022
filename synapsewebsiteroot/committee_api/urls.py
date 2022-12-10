from django.urls import path
from .views import *

urlpatterns = [
    path('core/', CoreAPI.as_view(), name = 'core'),
    path('exmember/', ExMemberAPI.as_view(), name = 'exmember'),
    path('faculty/', FacultyAPI.as_view(), name = 'faculty'),
    path('upcomming_events/', upcomming_events.as_view(), name = 'upcomming_events'),
    path('past_events/', past_events.as_view(), name = 'past_events'),
    path('projects/', ProjectAPI.as_view(), name = 'projects'),
]
