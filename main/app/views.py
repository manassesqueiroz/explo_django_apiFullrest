from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@api_view(['GET', 'POST'])
def api_env(request):
    if request.method == 'GET':
        products = User.objects.all()
        serializer = UserSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = make_password(data.get('password'))

        new_user = User.objects.create(
            name=name, email=email, password=password)
        serializer = UserSerializer(new_user)

        return Response(serializer.data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def api_mod(request, id):
    if request.method == 'GET':
        seacherUser = User.objects.get(id=id)
        serializer = UserSerializer(seacherUser)
        return Response(serializer.data, status=200)

    if request.method == 'PUT':
        user = get_user_or_404(id)
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        
        update_user_attributes(user, name, email)
        return Response('User updated successfully', status=200)

    if request.method == 'DELETE':
        user = get_user_or_404(id=id)       
        user.delete()
        return Response(f'User with ID {id} excluded', status=200)
          
          

def get_user_or_404(id):
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404('User not found')
      
def update_user_attributes(user, name, email):
    if name is not None:
        user.name = name
    if email is not None:
        user.email = email
    user.save()