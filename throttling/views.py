from threading import get_ident
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.decorators import throttle_classes, api_view
from rest_framework.settings import settings 
from django.conf import settings as django_settings 
import rest_framework.throttling as rest_throttling 
# Create your views here.

#######################################################################
#   UserRateThrottle -> Throttling for both Auth and Non Auth Users   #
#   - Rate is set for only auth users using custom Rate Throttlers    #
#   - so for non auth users 'anon' will fetch from settings           #
#   AnonRateThrottle -> Throttling for Only Non Auth Users Auth       # 
#   - users are free to make inf requests                             #
#######################################################################

class ExampleView(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request, format=None):
        # print(request.META, "request.META")
        print(request.META.get('HTTP_X_FORWARDED_FOR'), "request.META[HTTP_X_FORWARDED_FOR]")
        print(request.META.get('REMOTE_ADDR'), 'request.META[REMOTE_ADDR]')        
        print(settings.__dict__)
        content = {
            'status': 'request was permitted'
        } 

        return Response(content)


class CustomAnonRateThrottle(AnonRateThrottle):
    rate = '2/m'
    # either set rate in settings aur create a custom class 


@api_view(['GET'])
@throttle_classes([CustomAnonRateThrottle])
def function_based_throttle_example(request, format=None):
    print(CustomAnonRateThrottle().get_ident(request))
    content = {
        'status': 'request was permitted from functional views'
    }

    return Response(content)

# we can have multiple scopes with multiple request allowed 
class CustomScopeRateThrottle(UserRateThrottle):
    scope = 'burst'
    rate = '3/m'     


class CustomScopeThrottleView(APIView):
    # throttle_classes = [CustomScopeRateThrottle] # when to override a scope 
    throttle_scope = 'burst'  # take the rate from settings file 
    rate = '3/min'

    def get(self, request):
        content = {
            "status": "Respoing from class based view for custom throttling scope"
        }

        return Response(content)

@api_view(['GET'])
@throttle_classes([CustomScopeRateThrottle])
def custom_scope_throttle_view(request):

    content = {
        "status": "Responsing fror custom_scope_throttle_view"
    }

    return Response(content)




import random 

class RandomRateThrottler(UserRateThrottle):

    def allow_request(self, request, view):
        return random.randint(1,2) != 1 
    
    def wait(self):
        return 5


@api_view(['GET'])
@throttle_classes([RandomRateThrottler])
def random_rate_throttler_example_view(request):
    content = {
        "status": "inside the random rate throttler"
    }

    return Response(content)