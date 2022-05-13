from ast import Delete
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from snippets.models import Snippets
from snippets.serializers import SnippetsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics


@csrf_exempt 
def all_snippets_list(request, format=None):
    print("older snippets list")
    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetsSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = SnippetsSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, 
                status=201,
                safe=False) # if returning list of dict mark it true 
                # other wise it will raise excetion but data will be saved 
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippets_detail(request, pk):
    """
    Retireve, update and delete a code snippets
    """

    try:
        snippet = Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetsSerializer(snippet)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetsSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method=='DELETE':
        snippet.delete()
        return HttpResponse(status=204)

@api_view()
def get_param(request, pk):
    print(pk)
    return JsonResponse({"value": pk}, status=200)

@api_view(["GET" ,"POST"])
def snippets_list(request, pk, format=None):
    # allow the api to handle urls with format given like snippets/4.json
    print("Newer Snippets List")
    if request.method == "GET":
        snippets = Snippets.objects.all()
        serializer = SnippetsSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = SnippetsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST", "PUT"])
def snippets_list(request, pk):
    try:
        snippet = Snippets.objects.get(id=pk)
    except Snippets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = SnippetsSerializer(snippet)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = SnippetsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippets.objects.get(pk=pk)
        except Snippets.DoesNotExist:
            print("Here in 404 error")
            raise Http404
        
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetsSerializer(snippet)
        return Response(serializer.data)


class SnippetDetail(mixins.RetrieveModelMixin, 
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    
    queryset = Snippets.objects.all()
    serializer_class = SnippetsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SnippetsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsSerializer
