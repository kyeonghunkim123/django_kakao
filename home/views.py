from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def test_hello(request):
    print('This is a file named home/views.py')
    contents = '<h1>Hello</h1>'
    return HttpResponse(contents, content_type='text/html; charset=utf-8')

@api_view(['GET'])
def main(request):
    print('## 13')
    if request.method == 'GET':
        print('This is GET Request')
        return Response("data1", status=201)
    elif request.method == 'POST':
        print('This is POST Request')
        return Response("data2", status=202)

@api_view(['GET'])
def hotspots(request):
    return Response("data", status=200)

@api_view(['GET'])
def hotrestros(request):
    return Response("data", status=200)

@api_view(['GET'])
def hotaccoms(request):
    return Response("data", status=200)


@api_view(['GET'])
def plans(request):
    return Response("data", status=200)

@api_view(['GET'])
def packing_goods(request):
    return Response("data", status=200)

@api_view(['POST'])
def packing_update(request):
    return Response("data", status=200)




