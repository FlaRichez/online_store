from django_filters import FilterSet, CharFilter, NumberFilter
from .models import Products


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    price_lt = NumberFilter(field_name='price',lookup_expr='lte')
    price_gt = NumberFilter(field_name='price',lookup_expr='gte')



    class Meta:
        model = Products
        fields = ['name','type','price']