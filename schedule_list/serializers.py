from rest_framework import serializers
from .models import GuestSpace

class ScheduleListSerializer(serializers.ModelSerializer):
    host_id = serializers.SerializerMethodField()
    guest_id = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    memo = serializers.SerializerMethodField()

    class Meta:
        model = GuestSpace
        fields = (
            'host_id',
            'guest_id',
            'date',
            'memo'
        )
        
    @staticmethod
    def get_host_id(obj):
        return obj.schedule.host_id
    
    @staticmethod
    def get_guest_id(obj):
        return obj.schedule.guest_id
    
    @staticmethod
    def get_date(obj):
        return obj.schedule.date
    
    @staticmethod
    def get_memo(obj):
        return obj.schedule.memo