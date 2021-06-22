from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import pizza
from .serializers import PizzeSerializer
# Create your views here.



@api_view(['GET'])
def home(request):
    routes= [
        {
            '/api/all/':"all pizza"
        },
        {
            '/api/all/filters?type=typename&size=sizename':"filter pizza by type or size.(type can be either 'regular' or 'square')"
        },
        {
            '/api/create/Type/':"creating pizza Type can be either 'regular' or 'square' "
        },
          {
            '/api/update/id/':"updating pizza , id should be pizza id "
        },
        {
            '/api/delete/id/':"deleting pizza , id should be pizza id "
        },
    ]
    return Response(routes)

@api_view(['POST'])
def createPizza(request,Type):
    if Type:

        if Type == 'regular' or Type =='square':
            data=request.data


            pizzaVar=pizza.objects.create(
                name=data['name'],
                Type=Type,
                size=data['size'],
                toppings=data['toppings']
                )
            print(data)
            serializer=PizzeSerializer(pizzaVar,many=False)
            return Response(serializer.data)
    else:
        return Response('please include a pizza type')
   


@api_view(['PUT'])
def updatePizza(request,id):
    data = request.data
    pizzaVar=pizza.objects.get(id=id)
    
    if data['Type']:
        if data['Type'] == 'regular' or data['Type'] == 'square':
            pizzaVar.name=data['name']
            pizzaVar.size=data['size']
            pizzaVar.toppings=data['toppings']
            pizzaVar.Type=data['Type']

            pizzaVar.save()

            serializer= PizzeSerializer(pizzaVar,many=False)

            return Response(serializer.data)

    else:
        return Response('pizza type can be either regular or square')


@api_view(["DELETE"])
def deletePizza(request,id):
    pizzaVar=pizza.objects.get(id=id)
    pizzaVar.delete()
    return Response('pizza Deleted')


@api_view(['GET'])
def getAllPizza(request):
    allPizza = pizza.objects.all()
    serializer=PizzeSerializer(allPizza,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFilteredPizza(request):

    Type = request.GET.get('type')
    size=request.GET.get('size')
    if Type and size:
        print(size)
        print(Type)

        filteredPizza=pizza.objects.all().filter(Type__icontains=Type).filter(size__icontains=size)
        serializer=PizzeSerializer(filteredPizza,many=True)
        return Response(serializer.data)
    elif Type:
        print(Type)
        filteredPizza=pizza.objects.all().filter(Type__icontains=Type)
        serializer=PizzeSerializer(filteredPizza,many=True)
        return Response(serializer.data)
    elif size:
        print(size)
        filteredPizza=pizza.objects.all().filter(size__icontains=size)
        serializer=PizzeSerializer(filteredPizza,many=True)
        return Response(serializer.data)
    else:

        return Response('filtered pizza')
