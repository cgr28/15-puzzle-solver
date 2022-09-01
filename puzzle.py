from enums import *
import random
from helpers import Helpers, Heuristics, State, Translators
import sys

SOLUTION = [["1", "2", "3", "4"],["5", "6", "7", "8"],["9", "10", "11", "12"],["13", "14", "15", "_"]]

class Puzzle:
    """Represents the 15 puzzle.
    """
    def __init__(self, board=[["1", "2", "3", "4"],["5", "6", "7", "8"],["9", "10", "11", "12"],["13", "14", "15", "_"]], empty=None):
        self.board = board
        if not empty:
            self.empty = Puzzle.__find_empty(board)
        else:
            self.empty = empty

    @staticmethod
    def __find_empty(board):
        """Returns the position of the empty spot in the board.

        Args:
            board: The board to be searched.
        """
        for i in range(4):
            for j in range(4):
                if board[i][j] == "_":
                    return (i, j)

    def __can_move(self, pos):
        """Verifies whether position is acceptable.

        Args:
            pos: The position that needs to be checked.
        """
        row, col = pos

        if row < 0 or row > 3:
            return False
        
        if col < 0 or col > 3:
            return False
        
        return True
    
    def __swap_peek(self, pos1, pos2):
        """Returns a board with two elements swapped.

        Args:
            pos1: Position of the first element.
            pos2: Position of the second element.
        """
        board = [list(row) for row in self.board]
        board[pos1[0]][pos1[1]], board[pos2[0]][pos2[1]] = board[pos2[0]][pos2[1]], board[pos1[0]][pos1[1]]
        return board

    
    def __slide_left(self):
        row, col = self.empty
        new_col = col + 1
        if not self.__can_move((row, new_col)):
            return False
        self.empty = (row, new_col)
        self.board[row][col], self.board[row][new_col] = self.board[row][new_col], self.board[row][col]
        return True

    def __slide_right(self):
        row, col = self.empty
        new_col = col - 1
        if not self.__can_move((row, new_col)):
            return False
        self.empty = (row, new_col)
        self.board[row][col], self.board[row][new_col] = self.board[row][new_col], self.board[row][col]
        return True

    def __slide_down(self):
        row, col = self.empty
        new_row = row - 1
        if not self.__can_move((new_row, col)):
            return False
        self.empty = (new_row, col)
        self.board[row][col], self.board[new_row][col] = self.board[new_row][col], self.board[row][col]
        return True

    def __slide_up(self):
        row, col = self.empty
        new_row = row + 1
        if not self.__can_move((new_row, col)):
            return False
        self.empty = (new_row, col)
        self.board[row][col], self.board[new_row][col] = self.board[new_row][col], self.board[row][col]
        return True

    def possible_states(self, state):
        """Returns a list of states to be searched.

        Args:
            state: The parent state for the soon to be generated children states.
        """
        new_states = []
        row, col = self.empty
        if row > 0:
            new_puzzle = Puzzle(self.__swap_peek((row, col), (row-1, col)))
            new_state = State(state.g + 1, Heuristics.overall_manhattan_distance(new_puzzle.board), new_puzzle, state, Moves.UP)
            new_states.append(new_state)
        if row < 3:
            new_puzzle = Puzzle(self.__swap_peek((row, col), (row+1, col)))
            new_state = State(state.g + 1, Heuristics.overall_manhattan_distance(new_puzzle.board), new_puzzle, state, Moves.DOWN)
            new_states.append(new_state)
        if col > 0:
            new_puzzle = Puzzle(self.__swap_peek((row, col), (row, col-1)))
            new_state = State(state.g + 1, Heuristics.overall_manhattan_distance(new_puzzle.board), new_puzzle, state, Moves.LEFT)
            new_states.append(new_state)
        if col < 3:
            new_puzzle = Puzzle(self.__swap_peek((row, col), (row, col+1)))
            new_state = State(state.g + 1, Heuristics.overall_manhattan_distance(new_puzzle.board), new_puzzle, state, Moves.RIGHT)
            new_states.append(new_state)
        return new_states

    def copy(self):
        return Puzzle([list(row) for row in self.board], self.empty)
    
    def slide(self, dir):
        """Slides an adjacent puzzle piece into empty.

        Args:
            dir: The direction the piece originates from.
        """
        if dir == Moves.RIGHT:
            return self.__slide_right()
        elif dir == Moves.LEFT:
            return self.__slide_left()
        elif dir == Moves.UP:
            return self.__slide_up()
        elif dir == Moves.DOWN:
            return self.__slide_down()
    
    def shuffle(self, num=250):
        """Shuffles the board at random.

        Args:
            num (int, optional): Number of times to shuffle the board. Defaults to 250.
        """
        for _ in range(num):
            moved = False
            dirs = [Moves.RIGHT, Moves.LEFT, Moves.UP, Moves.DOWN]
            while not moved:
                if not len(dirs):
                    return None
                dir = dirs.pop(random.randrange(len(dirs)))
                moved = self.slide(dir)

    def display(self):
        """Displays the current board.
        """
        for i in range(4):
            print("{:^8} {:^8} {:^8} {:^8}\n".format(self.board[i][0], self.board[i][1], self.board[i][2], self.board[i][3]))

    def best_first_search(self):
        """Generates a best first search solution to the puzzle.  Not guaranteed to provide the optimal solution.
        """
        search = [State(0, Heuristics.overall_manhattan_distance(self.board), self, None)]
        vis = []
        while search:
            low_state_index = 0
            for i in range(1, len(search)):
                if search[i].h < search[low_state_index].h:
                    low_state_index = i

            state = search.pop(low_state_index)
            vis.append(state)

            if state.h == 0:
                return Helpers.state_tree(state)

            for new_state in state.puzzle.possible_states(state):
                contains = False

                for i in range(len(vis)):
                    if vis[i].puzzle.board == new_state.puzzle.board:
                        contains = True
                        break

                if contains:
                    continue

                search.append(new_state)
        return None


    
    def astar(self):
        """Generates an A* solution to the puzzle.  Guaranteed to provide an optimal solution.  May take a while to complete.
        """
        open = [State(0, Heuristics.overall_manhattan_distance(self.board), self)]
        closed = []
        while open:
            low_state_index = 0
            for i in range(1, len(open)):
                if open[i].f < open[low_state_index].f:
                    low_state_index = i
                    
            state = open.pop(low_state_index)

            closed.append(state)

            if state.h == 0:
                return Helpers.state_tree(state)

            for new_state in state.puzzle.possible_states(state):
                contains = False
                temp_state_index = False

                for i in range(len(closed)):
                    if closed[i].puzzle.board == new_state.puzzle.board:
                        contains = True
                        break

                if contains:
                    continue
                
                for i in range(len(open)):
                    if open[i].puzzle.board == state.puzzle.board:
                        temp_state_index = i
                        break

                if temp_state_index == False:
                    open.append(new_state)
                else:
                    orig = open[temp_state_index]
                    if orig.g < new_state.g:
                        open[temp_state_index].new_parent(state)
        return None

    def idastar(self):
        """Generates an IDA* solution to the puzzle.  Guaranteed to provide an optimal solution.  May take a while to complete.
        """
        root = State(0, Heuristics.overall_manhattan_distance(self.board), self)
        thresh = root.h
        while True:
            found, temp = Helpers.idastar_search(root, thresh)
            if found == True:
                return temp
            if temp == sys.maxsize:
                return None
            thresh = temp


