from django.shortcuts import render

from pagination.pagination_helper import \
    SmallResultsSetPagination, SmallResultLimitOffSetPagination, \
    SmallResultCursorBasedPagination, CustomSmallPageNumberPagination
from pagination.models import Billing 
from pagination.serializers import BillingSerializer
from rest_framework import generics
# from django.core.paginator import Paginator
# Create your views here.

class BillingRecordsPageNumberView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    # SmallResultsSetPagination.page_size = 1  
    pagination_class = \
        SmallResultsSetPagination

    # {
        # "count": 8,
        # "next": "http://localhost:8000/pagination/bill/list/?page=4",
        # "previous": "http://localhost:8000/pagination/bill/list/?page=2",
        # "results": [
            # {
                # "id": 5,
                # "name": "test 4",
                # "amount": 104,
                # "date": "2020-01-04",
                # "description": "test 4",
                # "created_at": "2022-06-01T15:31:09.750414Z",
                # "updated_at": "2022-06-01T15:31:09.750478Z"
            # },
            # {
                # "id": 6,
                # "name": "test 5",
                # "amount": 105,
                # "date": "2020-01-05",
                # "description": "test 5",
                # "created_at": "2022-06-01T15:31:23.764897Z",
                # "updated_at": "2022-06-01T15:31:23.764937Z"
            # }
        # ]
    # }


class BillingRecordsLimitOffsetView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    # SmallResultsSetPagination.page_size = 1  
    pagination_class = \
        SmallResultLimitOffSetPagination

    # {
        # "count": 8,
        # "next": "http://127.0.0.1:8000/pagination/bill/list/limit-offset/?limit=2&offset=6",
        # "previous": "http://127.0.0.1:8000/pagination/bill/list/limit-offset/?limit=2&offset=2",
        # "results": [
            # {
                # "id": 5,
                # "name": "test 4",
                # "amount": 104,
                # "date": "2020-01-04",
                # "description": "test 4",
                # "created_at": "2022-06-01T15:31:09.750414Z",
                # "updated_at": "2022-06-01T15:31:09.750478Z"
            # },
            # {
                # "id": 6,
                # "name": "test 5",
                # "amount": 105,
                # "date": "2020-01-05",
                # "description": "test 5",
                # "created_at": "2022-06-01T15:31:23.764897Z",
                # "updated_at": "2022-06-01T15:31:23.764937Z"
            # }
        # ]
    # }


class BillingRecordCursorView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    # SmallResultsSetPagination.page_size = 1  
    pagination_class = \
        SmallResultCursorBasedPagination

    # 
    # {
        # "next": "http://localhost:8000/pagination/bill/list/cursor/?cursor=cD0yMDIyLTA2LTAxKzE1JTNBMzIlM0E0OS42NTU5MTklMkIwMCUzQTAw",
        # "previous": null,
        # "results": [
            # {
                # "id": 8,
                # "name": "test 7",
                # "amount": 107,
                # "date": "2020-01-07",
                # "description": "test 7",
                # "created_at": "2022-06-01T15:33:10.041184Z",
                # "updated_at": "2022-06-01T15:33:10.041223Z"
            # },
            # {
                # "id": 7,
                # "name": "test 6",
                # "amount": 106,
                # "date": "2020-01-06",
                # "description": "test 6",
                # "created_at": "2022-06-01T15:32:49.655866Z",
                # "updated_at": "2022-06-01T15:32:49.655919Z"
            # }
        # ]
    # }


class BillingRecordCustomPageNumberView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    # SmallResultsSetPagination.page_size = 1  
    pagination_class = \
        CustomSmallPageNumberPagination