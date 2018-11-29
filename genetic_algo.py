from individual import Individual
from random import randint
from goal import Goal
from obstacle import Obstacle


def generate_population(generation):
    
    population = []
    directions_x=[]
    directions_y=[]
    
    for i in range(50): # we create 50 individuals 
        
        del directions_x[:] # we delete all elements of directions
        del directions_y[:]        
                
        for i in range(200): # we create a random directions array
            
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



def best_fitness(population):               # We search for the best individual in the last population
    best=0
                                            # Use the barrel method in a near future, to return more than 
    for i in range(length(population)):
        if population[i].fitness>score:
            best=population[i]
            champion=i
    return champion                         # Return the index of the best individual 



######################################



def checkMove(individual, obstacle):                  # Death of the individual
    directions = []
    
    
    #Check if the individual hit an obstacle
    
    if individual.x>=obstacle.w and individual.x<=obstacle.x and individual.y<=obstacle.y and individual.y<=obstacle.z:
        indivual.life=False
    
    
    #Check if the individual went out of the map
    
    if individual.x<=0 or individual.x>=SIZEMAP or individual.y<=0 or individual.y>=SIZEMAP:
        indivual.life=False
        
        
    return individual
    
    