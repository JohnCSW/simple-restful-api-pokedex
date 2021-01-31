from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        type_names_str = self.request.query_params.get('types')
        if type_names_str:
            type_names = type_names_str.strip().split(',')
            for type_name in type_names:
                type_name = type_name.strip()
                queryset = queryset.filter(types__name=type_name)

        return queryset

    def destroy(self, request, *args, **kwargs):
        pokemon = self.get_object()
        if pokemon.devolution:
            return Response(
                {"error": f"This pokemon is an evolution of {pokemon.devolution.name}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        pokemon_data = PokemonSerializer(pokemon).data
        pokemon.delete()
        return Response(data=pokemon_data)

    @action(detail=True, methods=['put', 'delete'])
    def evolution(self, request, pk=None):
        pokemon = self.get_object()
        try:
            evolved_pokemon = self.get_or_create_pokemon(request.data)

            if request.method == 'PUT':
                pokemon.evolutions.add(evolved_pokemon)
            else:
                if not (evolved_pokemon in pokemon.evolutions.all()):
                    raise AttributeError
                pokemon.evolutions.remove(evolved_pokemon)

            return Response(
                data=PokemonSerializer(pokemon).data
            )
        except AttributeError:
            return Response(
                {"error": "Invalid input"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def get_or_create_pokemon(self, data):
        try:
            return Pokemon.objects.get(number=data.get('number'))
        except Pokemon.DoesNotExist:
            serializer = PokemonSerializer(data=data)
            if serializer.is_valid():
                return serializer.save()
            raise AttributeError
