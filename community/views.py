from rest_framework.decorators import api_view
from rest_framework.response import Response

# MAIN
@api_view(['GET'])
def main(request):
    return Response("data1", status=200)


# FEED
## 3 functions -> feed_myfeeds, feed_write,
@api_view(['GET'])
def feed_myfeeds(request):
    return Response("data1", status=200)


@api_view(['POST'])
def feed_write(request):
    return Response("data1", status=200)


@api_view(['GET','POST'])
def feed_myfeed_update(request):
    if request.method == 'GET':
        return Response("data1", status=200)
    elif request.method == 'POST':
        return Response("data2", status=201)



# TRAVELREVIEWS & PLANS
## 5 functions -> travelreviews, plans, travelreview_write, travelreview_detail, travelreview_update

@api_view(['GET'])
def travelreviews(request):
    return Response("data1", status=200)


@api_view(['GET'])
def plans(request):
    return Response("data1", status=200)



@api_view(['POST'])
def travelreview_write(request):
    return Response("data1", status=200)



@api_view(['GET'])
def travelreview_detail(request):
    return Response("data1", status=200)


@api_view(['POST'])
def travelreview_update(request):
    return Response("data1", status=200)


# COMMUNITY -> SEARCH -> AFTERTRAVEL
## 1 functions -> search_aftertravel
@api_view(['GET'])
def search_aftertravel(request):
    return Response("data1", status=200)


