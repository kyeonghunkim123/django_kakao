from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def main(request):
    return Response("data1", status=200)


@api_view(['POST'])
def delete(request):
    return Response("data1", status=200)

@api_view(['GET'])
def places(request):
    return Response("data1", status=200)

@api_view(['GET'])
def accoms(request):
    return Response("data1", status=200)


@api_view(['GET']) #/schedule/plan/plans-detail
def plan_detail(request):
    return Response("data1", status=200)



@api_view(['POST']) #/schedule/plan/place/update
def plan_place_update(request):
    return Response("data1", status=200)

@api_view(['POST']) #/schedule/plan/place/delete
def plan_place_delete(request):
    return Response("data1", status=200)

@api_view(['POST']) #/schedule/plan/accom/update
def plan_accom_update(request):
    return Response("data1", status=200)

@api_view(['POST']) #/schedule/plan/accom/delete
def plan_accom_delete(request):
    return Response("data1", status=200)

@api_view(['POST']) #/schedule/plan/title/update
def plan_title_update(request):
    return Response("data1", status=200)

@api_view(['POST']) #/schedule/plan/date/update
def plan_date_update(request):
    return Response("data1", status=200)

@api_view(['POST']) #/schedule/plan/date/delete
def plan_date_delete(request):
    return Response("data1", status=200)

@api_view(['POST']) #/schedule/aiplan
def aiplan(request):
    return Response("data1", status=200)


