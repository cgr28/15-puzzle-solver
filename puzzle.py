# TODO cleanup
# TODO research IDA*
# TODO push to github
# TODO create README
# TODO discover how to make downloadable through cmd
# TODO cleanup w/ black
# TODO create separate file with only solver
# TODO new heuristics ??
# TODO change to 15-puzzle

from enums import *
import random
from helpers import Helpers, Heuristics, State, Translators
import copy

SOLUTION = [["1", "2", "3", "4"],["5", "6", "7", "8"],["9", "10", "11", "12"],["13", "14", "15", "_"]]

class Puzzle:

    def __init__(self, puzzle=[["1", "2", "3", "4"],["5", "6", "7", "8"],["9", "10", "11", "12"],["13", "14", "15", "_"]], empty=(3, 3)):
        self.puzzle = puzzle
        self.empty = empty

    def __can_move(self, pos):
        row, col = pos

        if row < 0 or row > 3:
            return False
        
        if col < 0 or col > 3:
            return False
        
        return True
    
    def __slide_left(self):
        row, col = self.empty
        new_col = col + 1
        if not self.__can_move((row, new_col)):
            return False
        self.empty = (row, new_col)
        self.puzzle[row][col], self.puzzle[row][new_col] = self.puzzle[row][new_col], self.puzzle[row][col]
        return True

    def __slide_right(self):
        row, col = self.empty
        new_col = col - 1
        if not self.__can_move((row, new_col)):
            return False
        self.empty = (row, new_col)
        self.puzzle[row][col], self.puzzle[row][new_col] = self.puzzle[row][new_col], self.puzzle[row][col]
        return True

    def __slide_down(self):
        row, col = self.empty
        new_row = row - 1
        if not self.__can_move((new_row, col)):
            return False
        self.empty = (new_row, col)
        self.puzzle[row][col], self.puzzle[new_row][col] = self.puzzle[new_row][col], self.puzzle[row][col]
        return True

    def __slide_up(self):
        row, col = self.empty
        new_row = row + 1
        if not self.__can_move((new_row, col)):
            return False
        self.empty = (new_row, col)
        self.puzzle[row][col], self.puzzle[new_row][col] = self.puzzle[new_row][col], self.puzzle[row][col]
        return True

    def copy(self):
        return Puzzle(copy.deepcopy(self.puzzle), self.empty)
    
    def slide(self, dir):
        if dir == Moves.RIGHT:
            return self.__slide_right()
        elif dir == Moves.LEFT:
            return self.__slide_left()
        elif dir == Moves.UP:
            return self.__slide_up()
        elif dir == Moves.DOWN:
            return self.__slide_down()
    
    def shuffle(self, num):
        for _ in range(num):
            moved = False
            dirs = [Moves.RIGHT, Moves.LEFT, Moves.UP, Moves.DOWN]
            while not moved:
                if not len(dirs):
                    return None
                dir = dirs.pop(random.randrange(len(dirs)))
                moved = self.slide(dir)

    def display(self):
        for i in range(4):
            for j in range(4):
                print(self.puzzle[i][j], end="  |  ")
            print("\n--------------------")
    
    def solution(self):
        open = [State(0, Heuristics.overall_manhattan_distance(self.puzzle), self)]
        closed = []
        while open:
            low_state_index = 0
            for i in range(len(open)):
                if open[i].f <= open[low_state_index].f:
                    low_state_index = i
            state = open.pop(low_state_index)
            closed.append(state)

            if state.puzzle.puzzle == SOLUTION:
                return Helpers.state_tree(state)

            for move in [Moves.RIGHT, Moves.LEFT, Moves.UP, Moves.DOWN]:
                temp_puzzle = state.puzzle.copy()
                can_move = temp_puzzle.slide(move)
                temp_state = State(state.g+1, Heuristics.overall_manhattan_distance(temp_puzzle.puzzle), temp_puzzle, state, Translators.move_to_string(move))
                if not can_move:
                    continue
                if Helpers.a_star_contains(temp_state, closed) != False:
                    continue
                
                temp_state_index = Helpers.a_star_contains(temp_state, open)
                if temp_state_index == False:
                    open.append(temp_state)
                else:
                    orig = open[temp_state_index]
                    if orig.g < temp_state.g:
                        open[temp_state_index].new_parent(state)
        print("no solution...")
        return None



