import django_filters
from django_filters import DateFilter
from .models import Task


class TaskFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='cr_date', lookup_expr="gte")
    end_date = DateFilter(field_name='cr_date', lookup_expr="lte")
    class Meta:
        model = Task
        fields = ['pm',]
        exclude = ['cr_date']