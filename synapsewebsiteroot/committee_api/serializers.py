from rest_framework import serializers
from .models import *

class ContactInfoSerilalizer(serializers.ModelSerializer):

    class Meta:
        model = Contact_info
        exclude = ['id', ]

class CoreCommitteeSerilalizer(serializers.ModelSerializer):
    fk_contactid = ContactInfoSerilalizer()
    class Meta:
        model = CoreCommittee
        fields = '__all__'

class FacultySerilalizer(serializers.ModelSerializer):
    fk_contactid = ContactInfoSerilalizer()
    class Meta:
        model = Faculty
        fields = '__all__'

class ExMemberbersSerilalizer(serializers.ModelSerializer):
    fk_contactid = ContactInfoSerilalizer()
    class Meta:
        model = Exmembers
        fields = '__all__'


        