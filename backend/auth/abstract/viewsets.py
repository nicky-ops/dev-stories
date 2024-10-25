from rest_framework import viewsets, filters


class AbstractViewSet(viewsets.ModelViewSet):
    '''
    Abstract viewset
    '''
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']