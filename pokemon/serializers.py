from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from pokemon.models import Pokemon, PokemonType


class EvolutedPokemonSerializer(serializers.ModelSerializer):
    types = SlugRelatedField(
        queryset=PokemonType.objects.all(),
        many=True,
        slug_field='name'
    )

    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'types')


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = ('name',)


class PokemonSerializer(serializers.ModelSerializer):
    types = SlugRelatedField(
        queryset=PokemonType.objects.all(),
        many=True,
        slug_field='name'
    )
    evolutions = EvolutedPokemonSerializer(many=True, required=False)

    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'types', 'evolutions')
