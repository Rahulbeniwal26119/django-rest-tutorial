from rest_framework.pagination import \
    PageNumberPagination, LimitOffsetPagination, \
    CursorPagination
from rest_framework.response import Response 

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SmallResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_query' # use page and page_query to get the page number 
    page_size_query_param = 'page_size' # number of item on one page 
    max_page_size = 10 


class SmallResultLimitOffSetPagination(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    default_limit = 2 # same as page_size


class SmallResultCursorBasedPagination(CursorPagination):
    # cannot generate the page number for a cursor based pagination
    ordering = '-updated_at'
    cursor_query_param = 'cursor'
    page_size = 2


class CustomSmallPageNumberPagination(PageNumberPagination):
    page_size = 2 

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'prev': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })