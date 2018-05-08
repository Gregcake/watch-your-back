'''
Written by Greg Tan (726323) & Luis Adjero (762095)
COMP30024: Artificial Intelligence
Project Part B: Watch Your Back!
Last Edited 11/04/2018

PLayer Class
'''
PLACEMENT = 1
MOVE = 2
import random
import time
import sys
from board import Board

class Player:
    '''
    Setup internal representation of player and board class
    Input: Color representation for the game
    Return Value: None
    '''
    def __init__(self, color):
        self.board = Board(color)
        self.strategy = Strategy()
        self.player = self.board.player
        self.enemy = self.board.enemy
        self.totalTurns = 0
        self.isMovement = False

    '''
    Referee calls program to make a move, decide what action to take. Should call update() with action at end to self-update.
    Input: Number of turns that have taken place since start of phase
    Return:(x,y) for placement phase / ((from_x,from_y),(to_x,to_y)) for move phase / None
    '''
    def action(self, turns):
        t = time.time()
        if self.totalTurns < 24:
            return self.strategy.placement(board, t)

        # movement phase
        else:
            return self.strategy.movement(board, t)

        self.totalTurns+= 1



        #check for board shrinkage
        if turns == 127:
            self.board.process_shrink(self.player)
            
    '''
    Referee tells program opponent move, update board class accordingly
    Input: Either player action ((from_x,from_y),(to_x,to_y)), can be player or opponent
    Return: No return value
    '''
    def update(self, action, color = None):
        self.totalTurns += 1 #since opponent completed their turn
        # unless specified, color will refer to enemy color
        if action == None: # no action was made
            return

        # type(action[0]) will return an int if we're in placement phase    
        if (type(action[0]) == int): # we're in the placement phase
            
            self.board.place(self.enemy, action)
        # otherwise, we are in the movement phase
        else:
            self.board.move(self.enemy, action)

