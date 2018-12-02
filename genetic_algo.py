from individual import Individual
from goal import Goal
from obstacle import Obstacle
from population import Population

from tkinter import *



window = Tk()

can = Canvas(window, width=500, height=500, bg='white')
can.master.title("Genetic Algorithm")
can.pack(side=TOP, padx=0, pady=0) 

b1 = Button(window, text='Start', command=lambda:print("hello"), bg='white' , fg='blue')
b1.pack(side=LEFT, padx=5, pady=5)

b2 = Button(window, text='Quit', command=window.destroy, bg='white' , fg='blue')
b2.pack(side=RIGHT, padx=5, pady =5)

tex1 = Label(window, text="Generation n°", bg='white' , fg='blue') # Incrémenter le numéro de la génération ici
tex1.pack(padx=0, pady=11)

window.mainloop()