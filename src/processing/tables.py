from django_tables2 import Column, tables, TemplateColumn
from .models import Batch, File, Item


class BatchList(tables.Table):
    class Meta:
        model = Batch
        template_name = 'django_tables2/bootstrap5.html'
        attrs = {'class': 'table table-sm'}
        fields = ['id', 'name', 'assigned_to']

    review = TemplateColumn(template_name='tables/view_item_list.html', orderable=False)
    assigned_to = Column(attrs={'th': {'class': 'text-decoration-line-through text-muted'}}, orderable=False)
    id = Column(verbose_name='ID')
    name = Column(verbose_name='Batch Name')
    finalize = TemplateColumn(verbose_name='', template_name='tables/finalize.html', orderable=False)


class ItemList(tables.Table):
    review_status = Column(
        attrs={
            'td': {
                'class': lambda value: 'text-success'
                if value == 'Complete'
                else ('text-warning' if value == 'In Progress' else 'text-danger')
            }
        },
        orderable=False,
    )

    class Meta:
        model = Item
        template_name = 'django_tables2/bootstrap5.html'
        attrs = {'class': 'table table-sm'}
        row_attrs = {'review_status': lambda value: value.name}
        fields = [
            'id',
            'date',
            'reporter',
            'title',
            'publish',
            'review_status',
        ]

    id = Column(verbose_name='ID', orderable=False)
    date = Column(orderable=False)
    reporter = Column(orderable=False)
    title = Column(orderable=False)
    publish = Column(orderable=False)
    review = TemplateColumn(template_name='tables/view_item.html', orderable=False)
