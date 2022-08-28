from enums import *
from collections import deque

class State:

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
        y1, x1 = start
        y2, x2 = end 
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def overall_manhattan_distance(puzzle):
        solution_hash = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (0, 3),
                         "5": (1, 0), "6": (1, 1), "7": (1, 2), "8": (1, 3),
                         "9": (2, 0), "10": (2, 1), "11": (2, 2), "12": (2, 3),
                         "13": (3, 0), "14": (3, 1), "15": (3, 2), "_": (3, 3)}
        overall = 0
        for i in range(4):
            for j in range(4):
                key = puzzle[i][j]
                overall += Heuristics.manhattan_distance((i, j), solution_hash[key])
        return overall

class Translators:

    @staticmethod
    def puzzle_to_string(puzzle):
        ret_string = ""
        for i in range(4):
            for j in range(4):
                ret_string += f"{puzzle[i][j]}."
        return ret_string
    
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

class Helpers:

    @staticmethod
    def a_star_contains(state, closed):
        state_string = Translators.puzzle_to_string(state.puzzle.puzzle)
        for i in range(len(closed)):
            if Translators.puzzle_to_string(closed[i].puzzle.puzzle) == state_string:
                return i
        return False

    @staticmethod
    def state_tree(state):
        tree = deque([state])
        while state.parent:
            tree.appendleft(state.parent)
            state = state.parent
        return tree