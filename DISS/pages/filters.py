import django_filters
from .models import *

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name']