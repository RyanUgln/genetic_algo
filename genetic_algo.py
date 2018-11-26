from individual import Individual
from random import randint
from goal import Goal
from obstacle import Obstacle


def generate_population(generation):
    
    population = []
    directions_x=[]
    directions_y=[]
    
    for i in range(50): # we create 50 indivuduals 
        
        del directions_x[:] # we delete each element of directions for each iteration
        del directions_y[:]        
                
        for i in range(200): # we create the random directions array 
            
            directions_x.append(randint(-1,1))
            directions_y.append(randint(-1,1))
        
        population.append(Individual(directions_x,directions_y,generation, 0))
    
    return population
    
    
    
###################################### 
    
    
population = generate_population(1); # first generation created



###print(population[1].directions_x[1])
###print(population[1].directions_x[2])
###print(population[1].directions_x[3])
###print(population[1].directions_x[4])


######################################


def checkMove(individual):
    
    directions = []
    #NORTH

    
    
    