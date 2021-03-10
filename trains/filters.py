from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='氏名', lookup_expr='contains')
    memo = filters.CharFilter(label='説明', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('route', 'route'),
        ),
        field_labels={
            'name': '氏名',
            'route': '所属路線開業時期',
        },
        label='並び順'
    )

    class Meta:

        model = Item
        fields = ('name', 'route', 'memo')