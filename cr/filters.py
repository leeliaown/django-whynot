from django.forms import widgets
import django_filters
from django_filters import DateFilter, DateFromToRangeFilter
from .models import Task


class TaskFilter(django_filters.FilterSet):
    start_date = DateFromToRangeFilter(field_name='cr_date', label="")
    # end_date = DateFromToRangeFilter(field_name='cr_date', lookup_expr="lte", label="End Date")
    class Meta:
        model = Task
        fields = ['cr_date']
        exclude = ['cr_date']

