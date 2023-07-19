import statistics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serlializers import ItemSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.shortcuts import get_object_or_404
from rest_framework import generics

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)

    


@api_view(['POST'])
def add_items(request):
	item = ItemSerializer(data=request.data)

	# validating for already existing data
	if Item.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')
	if item.is_valid():
		item.save()
		return Response({"status": "success", "item": {"data": item.data}}, status=status.HTTP_201_CREATED)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
	    

@api_view(['GET'])
def view_items(request):
	# checking for the parameters from the URL
	if request.query_params:
		items = Item.objects.filter(**request.query_params.dict())
	else:
		items = Item.objects.all()
	# if there is something in items else raise error
	if items:
		serializer = ItemSerializer(items, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

	
	


@api_view(['POST'])
def update_items(request, pk):
	item = Item.objects.get(pk=pk)
	data = ItemSerializer(instance=item, data=request.data)
	if data.is_valid():
		data.save()
		return Response({"status": "ອັບເດດສຳເລັດ", "data": {"data": data.data}}, status=status.HTTP_201_CREATED)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response({"status": "ລຶບອອກສຳເລັດ"},status=status.HTTP_202_ACCEPTED)




@api_view(['GET'])
def details(request, pk):
		item = Item.objects.get(id=pk)
		return Response(item.data)


#Register
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")





