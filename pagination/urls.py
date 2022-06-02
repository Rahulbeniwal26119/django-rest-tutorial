from django.urls import path 
from pagination import views
urlpatterns = [
    path('bill/list/page-number/', \
        views.BillingRecordsPageNumberView.as_view()),
    path('bill/list/limit-offset/', \
        views.BillingRecordsLimitOffsetView.as_view()),
    path('bill/list/cursor/', \
        views.BillingRecordCursorView.as_view()),
    path('bill/list/custom/', \
        views.BillingRecordCustomPageNumberView.as_view()),


]