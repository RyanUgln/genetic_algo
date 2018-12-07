
import random,time
import numpy
from individual import Individual

class Population:

    def __init__(self, generation):
        self.generation = generation

        self.tab_of_individuals = []
        directions_x=[]
        directions_y=[]
        
        for i in range(50): # we create 50 individuals 
            
            del directions_x[:] # we delete all elements of directions
            del directions_y[:]        
                    
            for i in range(200): # we create a random directions array
                random.seed()
                directions_x.append(random.randint(-3,3))
                print(directions_x[i])
                directions_y.append(random.randint(-8,3))
                
            self.tab_of_individuals.append(Individual(directions_x,directions_y,generation, 0))


        
    def best_fitness(self):               # We search for the best individual in the last population
        best=0                                  
                                                # Use the barrel method in a near future, to return more than one individual 
        for i in range(len(self)):
            if self[i].fitness>best:
                best=self[i].fitness              
                champion=i
        return champion                         # Return the index of the best individual 
    
    
