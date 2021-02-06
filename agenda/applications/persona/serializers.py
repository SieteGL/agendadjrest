#pagination de rest_framework
from rest_framework import serializers, pagination
from . models import Person, Reunion, Hobby
from django.utils.timezone import now


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


class PersonaSerializer(serializers.Serializer):
    #no pertenece a ni un modelo.
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    #agregamos dato no coincidente con el model Person
    activo = serializers.BooleanField(default=False)

#como el de arriba agregar
class PersonaSerializer2(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=False)
    class Meta:
        model = Person
        fields = ('__all__')
        

class ReunionSerializer(serializers.ModelSerializer):
    
    #FK
    persona = PersonaSerializer()
    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )

class HobbySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hobby
        fields = ('__all__')        

class PersonaSerializer3(serializers.ModelSerializer):
    
    #many2many poner many=true para recuperar datos de un array
    hobbies = HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
        )      


class ReunionSerializer2(serializers.ModelSerializer):
    
    #agregar al fields 
    fecha_hora = serializers.SerializerMethodField()
    #sacado de la web de django rest framework
    days_since_joined = serializers.SerializerMethodField()
    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora',
            'days_since_joined',
        )

    def get_fecha_hora(self, obj):
        #obj igual elementos de la lista
        return str(obj.fecha) + ' - ' + str(obj.hora)

    #devuelde cuantos dias lleva desde que se unio
    #recordar importar now() 
    def get_days_since_joined(self, obj):
        return (now() - obj.persona.created).days       

#ya no eredamos de modelserializer
class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',              
        )
        #extra kwargs para un diccionario
        extra_kwargs = {
            'persona':{
                #quien muesta   #link                #mediante que valor slug pk etc
                'view_name': 'persona_app:detalle', 'lookup_field':'pk'
            }
        }


class PersonPagination(pagination.PageNumberPagination):
    page_size = 5
    #cantidad de memoria pre cargado de archivos
    max_page_size = 50

class CountReunionserializer(serializers.Serializer):
    #no pertenece a ni un modelo.
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()    