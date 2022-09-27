from enums import *
from collections import deque
from puzzle import *
import sys
import json 

class State:
    """Used in the solvers to represent a state
    """

    def __init__(self, g, h, puzzle, parent=None, move=None):
        self.g = g
        self.h = h
        self.f = g + h
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
    
    def new_parent(self, parent):
        self.parent = parent
        self.g = parent.g + 1
        self.f = self.g + self.h

class Heuristics:

    @staticmethod
    def manhattan_distance(start, end):
        """Returns the distance between two points.

        Args:
            start: The position of the starting point.
            end: The position of the end point.
        """
        y1, x1 = start
        y2, x2 = end
        ans = abs(x1 - x2) + abs(y1 - y2)
        return ans

    @staticmethod
    def overall_manhattan_distance(board):
        """Returns the value of how far away each puzzle piece is from its goal position.

        Args:
            board: A 15 puzzle board.
        """

        goal_pos = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (0, 3),
                    "5": (1, 0), "6": (1, 1), "7": (1, 2), "8": (1, 3),
                    "9": (2, 0), "10": (2, 1), "11": (2, 2), "12": (2, 3),
                    "13": (3, 0), "14": (3, 1), "15": (3, 2), "_": (3, 3)}
        overall = 0
        for i in range(4):
            for j in range(4):
                key = board[i][j]
                overall += Heuristics.manhattan_distance((i, j), goal_pos[key])
        return overall


class Translators:
    
    @staticmethod
    def move_to_string(move):
        if move == Moves.UP:
            return "up"
        elif move == Moves.DOWN:
            return "down"
        elif move == Moves.RIGHT:
            return "right"
        else:
            return "left"

    @staticmethod
    def board_to_string(board):
        board_string = ""
        for i in range(len(board)):
            for j in range(len(board[i])):
                board_string += (board[i][j] + "-" )
        return board_string

class Helpers:

    @staticmethod
    def state_tree(state):
        """Returns a list of a given states \"family tree\".

        Args:
            state: The state whose \"family tree\" will be generated.
        """
        tree = deque([state])
        while state.parent:
            tree.appendleft(state.parent)
            state = state.parent
        return tree

    @staticmethod
    def idastar_search(state, thresh):
        if state.f > thresh:
            return False, state.f
        if state.h == 0:
            return True, [state]
        min = sys.maxsize
        for new_state in state.puzzle.possible_states(state):
            found, temp = Helpers.idastar_search(new_state, thresh)

            if found == True:
                return True, [state] + temp
            if temp < min:
                min = temp
        return False, min