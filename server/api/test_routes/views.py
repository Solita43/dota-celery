
# built-in non-REST method
from django.http import JsonResponse

# rest_framework imports in order to use GET, POST, PUT, DELETE
from rest_framework.decorators import api_view
from rest_framework.response import Response

# sample routes
from .routes import routes

"""
Example usage (just to test the route and displaying it with django), navigate to:
    - http://127.0.0.1:8000/api/nonrest
    or
    - http://127.0.0.1:8000/api/rest

Example usage in frontend:
    - create a fetch to either /api/nonrest or /api/rest
    - make sure you .json() your response
    - console.log the json'd response and you shall see the results
"""

def getRoutesNonRestMethod(request):
    """
    This is an example of an HTTP response function (the other way is to use a class) that consumes data to be serialized to JSON.

    It is serialized by using JsonResponse, and safe=False makes it able to accept more than just dictionaries.

    This is NOT an example of using django's rest framework, this is built in using the JsonResponse method from django

    non-REST aka built-in django JsonResponse will display on the page a json response
    """

    routes = [
        '/api/test/1',
        '/api/test/2',
        '/api/test/3',
        '/api/test/4',
        '/api/test/5',
    ]

    print('NON-REST test route successfully hit! 😁😁😁')
    return JsonResponse(routes, safe=False)


@api_view(['GET']) # ['GET', 'POST', 'PUT', 'DELETE'] can all be included in here
def getRoutesRestMethod(request):
    """
    REST will display a neatly styled page that includes other information such as
        - HTTP Code Response (i.e. HTTP 200 OK)
        - Allow: Get, OPTIONS
        - Content-Type: application/json
        - Vary: Accept
        [
            '/api/test/1',
            '/api/test/2',
            '/api/test/3',
            '/api/test/4',
            '/api/test/5',
        ]
    """

    routes = [
        '/api/test/1',
        '/api/test/2',
        '/api/test/3',
        '/api/test/4',
        '/api/test/5',
    ]

    print('REST test route successfully hit! 😁😁😁')
    return Response(routes)

@api_view(['GET'])
def getSingleRouteRestMethod(request, pk):
    """
    Example of returning a specific route based on its id (/api/test/id)

    1. Pass in pk instead of id
        - This is bc python has a function called id
    2. Add new path to test_routes/urls.py and set the id to pk
        - path('test/<str:pk>/', views.getSingleRouteRestMethod, name='singleRoute')
        - pk stands for primary key

    - A more realistic example would be:
        - path('products/<str:pk>/', views.getProduct, name='product')

    """

    singleRoute = None
    for i in routes:
        if i['_id'] == pk:
            singleRoute = i
            break

    return Response(singleRoute)
