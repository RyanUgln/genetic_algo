'''
Created on 26 nov. 2018

@author: L
'''

class Obstacle:
    '''
    Obstacles to create
    '''

    # ON PEUT PEUT ETRE CREER PLUSIEURS CONSTRUCTEURS EN FONCTION DU TYPE D'OBSTACLE QUE L'ON VEUT (RECTANGLE? CERCLE...)

    def __init__(self, w,x,y,z): #4 positions to be able to create rectangles and squares 
        self.w=w
        self.x=x
        self.y=y
        self.z=z
