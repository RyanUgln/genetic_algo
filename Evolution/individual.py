

class Individual:
    '''
    One individual of the population
    '''


    def __init__(self, directions_x, directions_y, generation, fitness):
        
        self.x=50 # Starting positions
        self.y=50
        
        self.fitness=fitness
    
        self.directions_x=directions_x # Directions x array
        self.directions_y=directions_y # Directions x array
        
        self.generation=generation # Its generation
        
        self.life=True #is he alive or not
        
        
    def update_positions(self, i):
        self.x+=self.directions_x[i]
        self.y+=self.directions_y[i]