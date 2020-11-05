from django.contrib import admin
from .models import PokemonSpecies,Pokemon,Types,Trainer

# Register your models here.

admin.site.register(Pokemon)
admin.site.register(PokemonSpecies)
admin.site.register(Types)
admin.site.register(Trainer)


