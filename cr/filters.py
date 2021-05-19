from django.forms import widgets
import django_filters
from django_filters import DateFromToRangeFilter
from .models import Task


class TaskFilter(django_filters.FilterSet):
    filter_date = DateFromToRangeFilter(field_name='cr_date', label="")
    class Meta:
        model = Task
        fields = ['cr_date']
        exclude = ['cr_date']

