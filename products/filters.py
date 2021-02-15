from django_filters import FilterSet, CharFilter
from .models import Products


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    class Meta:
        model = Products
        fields = ['name','type']