

class Individual:
    '''
    One indivudual of the population
    '''


    def __init__(self, directions_x, directions_y, generation, fitness):
        
        x_start=50 # Starting positions
        y_start=50
        self.fitness=fitness
    
        self.directions_x=directions_x # Directions x array
        self.directions_y=directions_y # Directions x array
        self.generation=generation # Its generation
        