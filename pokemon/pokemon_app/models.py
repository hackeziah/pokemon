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
    species_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],verbose_name="Species Number")
    level_evolve = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],verbose_name="Level Evolve")
    evolution = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],verbose_name="Evolution",default=0)
    new_species = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],verbose_name="New Species",default=0)

    
    def __str__(self):
        return self.species +' Type '+ str([a.type_name for a in self.types.all()])

class Pokemon(models.Model):
    name = models.CharField(max_length=100,verbose_name="Name")
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],verbose_name="Level")
    species_name = models.ForeignKey(PokemonSpecies,on_delete=models.CASCADE) 

    def save(self, *args, **kwargs):

        if self.level <= self.species_name.level_evolve or self.level == self.species_name.level_evolve:
            self.species_name = self.species_name

        if self.level > self.species_name.evolution:#new evolution
            self.species_name =  PokemonSpecies.objects.filter(id= self.species_name.new_species)[0]
            self.level = 1
        elif self.level >= self.species_name.level_evolve and self.level <= self.species_name.evolution:
            self.species_name.species_number = self.species_name.species_number + 1
            self.species_name = PokemonSpecies.objects.filter(id=self.species_name.species_number )[0]

        if self.level == self.species_name.evolution:
            self.species_name.species_number = self.species_name.species_number + 1
            self.species_name = PokemonSpecies.objects.filter(id=self.species_name.species_number )[0]

        elif self.level < self.species_name.evolution or self.level >= self.species_name.level_evolve:
            self.species_name.species_number = self.species_name.species_number - 1
            self.species_name = PokemonSpecies.objects.filter(id=self.species_name.species_number )[0]


        # elif self.level == self.species_name.evolution :
        #     self.species_name.species_number = self.species_name.number + 2
        #     self.species_name = PokemonSpecies.objects.filter(id=self.species_name.species_number )[0]
        super(Pokemon,self).save(*args, **kwargs)

    def __str__(self):
        return self.name +' '+ self.species_name.species + ' Level: ' + str(self.level)

class Trainer(models.Model):
    trainer_name = models.CharField(max_length=100, verbose_name="Trainer Name")
    pokemon = models.ManyToManyField(Pokemon) 
    
    def __str__(self):
        return self.trainer_name +' Pokemon: '+ str([a.name for a in self.pokemon.all()])

