from rest_framework.decorators import api_view
from rest_framework.response import Response

# MAIN
@api_view(['GET'])
def main(request):
    return Response("data1", status=200)


# REVIEW
## 2 functions -> myreviews, travelreviews
@api_view(['GET'])
def myreviews(request):
    return Response("data1", status=200)

@api_view(['GET'])
def travelreviews(request):
    return Response("data1", status=200)

# DIBS
## 3 functions -> dibs, dibs_create, dibs_delete
@api_view(['GET'])
def dibs(request):
    return Response("data1", status=200)

@api_view(['POST'])
def dibs_create(request):
    return Response("data1", status=200)

@api_view(['POST'])
def dibs_delete(request):
    return Response("data1", status=200)


# MYREVIEWS
## 2 functions -> myreview_detail, myreview_save
@api_view(['GET'])
def myreview_detail(request):
    return Response("data1", status=200)

@api_view(['POST'])
def myreview_save(request):
    return Response("data1", status=200)



# PROFILE
## 2 functions -> profile, profile_update
@api_view(['GET'])
def profile(request):
    return Response("data1", status=200)

@api_view(['POST'])
def profile_update(request):
    return Response("data1", status=200)



# CONFIGS
## 2 functions -> configs, config_update
@api_view(['GET'])
def configs(request):
    return Response("data1", status=200)

@api_view(['POST'])
def config_update(request):
    return Response("data1", status=200)



# NOTICE
## 2 functions -> notices, notice_detail
@api_view(['GET'])
def notices(request):
    return Response("data1", status=200)

@api_view(['GET'])
def notice_detail(request):
    return Response("data1", status=200)


# NOTICE
## 1 functions -> terms
@api_view(['GET'])
def terms(request):
    return Response("data1", status=200)
