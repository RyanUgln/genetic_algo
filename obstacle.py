'''
Created on 26 nov. 2018

@author: L
'''

class Obstacle:
    '''
    Obstacles to create
    '''

    # ON PEUT PEUT ETRE CREER PLUSIEURS CONSTRUCTEURS EN FONCTION DU TYPE D'OBSTACLE QUE L'ON VEUT (RECTANGLE? CERCLE...)

    def __init__(self, x, y, width, height): # (x,y) are the coordinates of the top left corner of the rectangle
        self.x = x
        self.y = y
        self.width = width
        self.height = height