from django.shortcuts import render

from django.views.generic import (
    ListView,
    TemplateView
)
#
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView, #Detailview 
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

#
from .models import Person, Reunion
#
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    ReunionSerializer,
    PersonaSerializer3,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonPagination,
    CountReunionserializer,
)

from .managers import ReunionManager


class ListaPersonasListView(ListView):
    template_name = "persona/personas.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()

#JSON   
class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer

    #serializar valores a JSON 
    def get_queryset(self):
        return Person.objects.all()

#lista entregada para ver con vuejs
class PersonListView(TemplateView):
    template_name = "persona/lista.html"


class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        #filtramos datos que recivimos por url a traves de la caja
        kword = self.kwargs['kword']

        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonCreateView(CreateAPIView):
    #POST
    serializer_class = PersonSerializer

class PersonDetailView(RetrieveAPIView):
    #model = PErson # rest ya no usa esto si no queryset
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonUpdateView(UpdateAPIView):
    #PUT
    #model = Person
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonRetriveUpdateView(RetrieveUpdateAPIView):
    #muestra los valores en los campos que seran actualizados, como un placeholder...
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonApiLista(ListAPIView):
    #vista para interactuar con serializadores
    #comentado por el curso 229 serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer2
    
    def get_queryset(self):
        return Person.objects.all()

class ReunionApiLista(ListAPIView):
    #vista para interactuar con serializadores
    #comentado por el curso 229 serializer_class = PersonaSerializer
    serializer_class = ReunionSerializer
    
    def get_queryset(self):
        return Reunion.objects.all()        

class HobbyApiLista(ListAPIView):
    #vista para interactuar con serializadores
    #comentado por el curso 229 serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer3
    
    def get_queryset(self):
        return Person.objects.all()        

class ReunionApiLista2(ListAPIView):
    #vista para interactuar con serializadores
    #comentado por el curso 229 serializer_class = PersonaSerializer
    serializer_class = ReunionSerializer2
    
    def get_queryset(self):
        return Reunion.objects.all()

#link en el serializer
class ReunionApiListaLink(ListAPIView):
    #vista para interactuar con serializadores
    #comentado por el curso 229 serializer_class = PersonaSerializer
    serializer_class = ReunionSerializerLink
    
    def get_queryset(self):
        return Reunion.objects.all()


class PersonPaginationLists(ListAPIView):
    #vista con paginacion
    serializer_class = PersonaSerializer
    pagination_class = PersonPagination
    
    def get_queryset(self):
        return Person.objects.all()


class ReunionByPersonJob(ListAPIView):
    serializer_class = CountReunionserializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()
    