from rest_framework.decorators import api_view
from rest_framework.response import Response

# MAIN
## 5 functions -> main, delete, results, more, categories
@api_view(['GET'])
def main(request):
    return Response("data1", status=200)

@api_view(['POST'])
def delete(request):
    return Response("data1", status=200)

@api_view(['GET'])
def results(request):
    return Response("data1", status=200)

@api_view(['GET'])
def more(request):
    return Response("data1", status=200)
@api_view(['GET'])
def categories(request):
    return Response("data1", status=200)


# CREATING A REVIEW
## 3 functions -> category_review_create, category_review_update, category_review_delete
@api_view(['POST'])
def category_review_create(request):
    return Response("data1", status=200)

@api_view(['POST'])
def category_review_update(request):
    return Response("data1", status=200)

@api_view(['POST'])
def category_review_delete(request):
    return Response("data1", status=200)


# ADDING A HEART ICON
## 2 functions -> category_review_heart_create, category_review_heart_delete

@api_view(['POST'])
def category_review_heart_create(request):
    return Response("data1", status=200)

@api_view(['POST'])
def category_review_heart_delete(request):
    return Response("data1", status=200)


# CREATING A REPLY
## 3 functions -> category_review_reply_create, category_review_reply_update, category_review_reply_delete

@api_view(['POST'])
def category_review_reply_create(request):
    return Response("data1", status=200)

@api_view(['POST'])
def category_review_reply_update(request):
    return Response("data1", status=200)

@api_view(['POST'])
def category_review_reply_delete(request):
    return Response("data1", status=200)


# REPORTING AN AUTHOR
## 1 functions -> author_report
@api_view(['POST'])
def author_report(request):
    return Response("data1", status=200)


