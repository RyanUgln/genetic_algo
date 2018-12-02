

class Individual:
    '''
    One individual of the population
    '''


    def __init__(self, directions_x, directions_y, generation, fitness):
        
        self.x=50 # Starting positions
        self.y=50
        
        # canvas.create_rectangle(self.x, self.y, self.x+5, self.y+5, outline='red', fill='red')
        
        self.fitness=fitness
        
        self.directions_x=directions_x # Directions x array
        self.directions_y=directions_y # Directions x array
        
        self.generation=generation # Its generation
        
        self.life=True #is he alive or not
    
    
    def checkMove(self, obstacle):                  # Death of the individual
        directions = []
        
        #Check if the individual hit an obstacle
        
        if self.x>=obstacle.w and self.x<=obstacle.x and self.y<=obstacle.y and self.y<=obstacle.z:
            self.life=False
        
        
        #Check if the individual went out of the map
        
        if self.x<=0 or self.x>=SIZEMAP or self.y<=0 or self.y>=SIZEMAP:
            self.life=False
            
            
        return self
    
    
    def update_positions(self, i):
        self.x+=self.directions_x[i]
        self.y+=self.directions_y[i]
    
    