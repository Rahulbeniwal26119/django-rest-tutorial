from django.urls import path 
from .views import ExampleView, \
    function_based_throttle_example, \
    custom_scope_throttle_view, \
    CustomScopeThrottleView, \
    random_rate_throttler_example_view


urlpatterns = [
    path('example/', ExampleView.as_view(),
        name='example_throttle'),
    path('example/function/', function_based_throttle_example,
        name='function_based_throttle_example'),
    path('example/custom-scope/', custom_scope_throttle_view, 
        name='custom_scope_throttle_view'),
    path('example/custom-scope/class/', CustomScopeThrottleView.as_view(), 
        name='custom_scope_throttle_view'),
    path('example/random-rate-throttler/', random_rate_throttler_example_view,
    name="random_rate_throttler_example_view")
]