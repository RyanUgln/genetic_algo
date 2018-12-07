from individual import Individual
from goal import Goal
from obstacle import Obstacle
from population import Population
import time
from tkinter import *

 

window = Tk()

can = Canvas(window, width=500, height=500, bg='white')
can.master.title("Genetic Algorithm")
can.pack(side=TOP, padx=0, pady=0) 


goal = Goal(500/2 - 4,40)
goal_graph=can.create_oval(goal.x, goal.y, goal.x+16, goal.y+16,outline='green', fill='green')

obstacle = Obstacle(50, 500/2 - 6, 500 - 50*2, 16 )
can.create_rectangle(obstacle.x, obstacle.y, obstacle.x + obstacle.width, obstacle.y + obstacle.height, outline='blue', fill='blue')

b1 = Button(window, text='Start', command=lambda:print("start"), bg='white' , fg='blue')
b1.pack(side=LEFT, padx=5, pady=5)

b2 = Button(window, text='Quit', command=window.destroy, bg='white' , fg='blue')
b2.pack(side=RIGHT, padx=5, pady =5)

tex1 = Label(window, text="Generation n°", bg='white' , fg='blue') # Incrémenter le numéro de la génération ici
tex1.pack(padx=0, pady=11)


population=Population(0)

k=0
window.update()

for n in range(len(population.tab_of_individuals[0].directions_x)):
    individu_graph=[]
    for i in range(len(population.tab_of_individuals)):
        
        individu_graph.append(can.create_oval(population.tab_of_individuals[i].x, population.tab_of_individuals[i].y,population.tab_of_individuals[i].x+16, population.tab_of_individuals[i].y+16, outline='red', fill='red'))
        print(population.tab_of_individuals[i].x)

        window.update()

        population.tab_of_individuals[i].checkMove(obstacle,goal)
        
        #print (population.tab_of_individuals[i].life)
        
        if (population.tab_of_individuals[i].life==True):
            
            population.tab_of_individuals[i].update_positions(k)
            
        
    for i in range(len(population.tab_of_individuals)):
        can.delete(individu_graph[i])
    window.update()

  
    k=k+1          
    
    
for i in range(len(population.tab_of_individuals)):
      population.tab_of_individuals[i].fitness=population.tab_of_individuals[i].calculate_fitness(goal,50)
         
champion=population.best_fitness()     
print('champion %s' %champion)
window.mainloop()  
