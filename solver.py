# solver.py -- 15-puzzle solver

from puzzle import Puzzle
from helpers import *
from enums import *
import sys

# the puzzle that will be solved
# edit to contain the puzzle you want solved
PUZZLE = [["1", "2", "3", "4"],
          ["5", "6", "7", "8"],
          ["9", "10", "11", "12"],
          ["13", "14", "15", "_"]]

def display_solution_path(solution):
    for i in range(len(solution)):
        print(f"STEP {i+1} of {len(solution)}")
        print("move: ", Translators.move_to_string(solution[i].move))
        solution[i].puzzle.display()
        print()

if __name__ == '__main__':
    solver_type = "bfs"
    num_of_shuffles = 0

    if len(sys.argv) > 1:
        solver_type = sys.argv[1]
    if len(sys.argv) > 2:
        num_of_shuffles = int(sys.argv[2])

    puzzle = Puzzle(PUZZLE)
    puzzle.shuffle(num_of_shuffles)

    if solver_type == "astar":
        solution = puzzle.astar()
    elif solver_type == "idastar":
        solution = puzzle.idastar()
    else:
        solution = puzzle.best_first_search()
    
    display_solution_path(solution)