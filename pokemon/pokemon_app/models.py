from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Types(models.Model):
    type_name = models.CharField(max_length=100,verbose_name="Type Name")
    def __str__(self):
        return self.type_name

class PokemonSpecies(models.Model):
    species = models.CharField(max_length=100,verbose_name="Species Name")
    types = models.ManyToManyField(Types) 
    
    def __str__(self):
        return self.species +' Type '+ str([a.type_name for a in self.types.all()])

class Pokemon(models.Model):
    name = models.CharField(max_length=100,verbose_name="Name")
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],verbose_name="Level")
    species_name = models.ForeignKey(PokemonSpecies,on_delete=models.CASCADE) 

    def save(self, *args, **kwargs):
        if  self.species_name.id == 1: #Bulbasaur
            if self.level >=16:
                a =  2
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]

        if  self.species_name.id == 2: #Ivysaur
            if self.level < 16:
                a =  1
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            if self.level >=32:
                a = self.species_name.id = 3
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
        if  self.species_name.id == 3: #Venusaur 
            if self.level < 16:
                a =  1
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            if self.level < 32 and self.level >= 16:
                a =  2
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            
            if self.level == 32:
                a = self.species_name.id = 3
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            if self.level > 32:
                a = self.species_name.id = 4
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
                self.level = 1

        if  self.species_name.id == 4: #Charmander (new)
            if self.level >=16:
                a = 5
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]

        if self.species_name.id == 5: #Charmelon
            if self.level < 16:
                a = 4
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            if self.level >=36:
                a = self.species_name.id = 6
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]

        if self.species_name.id == 6: #Charizard 
            if self.level < 16:
                a =  4
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            if self.level < 36 and self.level >= 16:
                a =  5
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            
            if self.level == 36:
                a = self.species_name.id = 6
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            if self.level > 36:
                a = self.species_name.id = 7
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
                self.level = 1
        if  self.species_name.id == 7: #Squirtle (new)
            if self.level >=16:
                a = 8
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
        if self.species_name.id == 8: #Wartolte
            if self.level < 16:
                a = 7
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            if self.level ==36:
                a = self.species_name.id = 9
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]

        if self.species_name.id == 9: #Blatoise 
            if self.level < 16:
                a =  7
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            
            if self.level < 36 and self.level >= 16:
                a =  8
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            
            if self.level == 36:
                a = self.species_name.id = 9
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
            if self.level > 36:
                a = self.species_name.id = 10 #Caterpie (new)
                self.species_name = PokemonSpecies.objects.filter(id=a)[0]
                self.level = 1 
        super(Pokemon,self).save(*args, **kwargs)

    def __str__(self):
        return self.name +' '+ self.species_name.species + ' Level: ' + str(self.level)

class Trainer(models.Model):
    trainer_name = models.CharField(max_length=100, verbose_name="Trainer Name")
    pokemon = models.ManyToManyField(Pokemon) 
    
    def __str__(self):
        return self.trainer_name +' Pokemon: '+ str([a.name for a in self.pokemon.all()])

