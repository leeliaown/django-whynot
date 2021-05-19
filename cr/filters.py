from django.forms import widgets
import django_filters
from django_filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from .models import Task


class TaskFilter(django_filters.FilterSet):
    filter_date = DateFromToRangeFilter(label="", 
                                        field_name='cr_date', 
                                        widget=RangeWidget(attrs={'placeholder': 'YYYY-MM-DD',
                                                                  'type': 'date'}))
    class Meta:
        model = Task
        fields = ['cr_date']
        exclude = ['cr_date']

