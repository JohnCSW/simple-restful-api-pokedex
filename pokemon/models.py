from django.db import models


class Pokemon(models.Model):
    number = models.TextField(primary_key=True)
    name = models.CharField(max_length=50)
    types = models.ManyToManyField('PokemonType')
    devolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name="evolutions",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
