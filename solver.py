# solver.py -- 15-puzzle solver

from puzzle import Puzzle
from helpers import *
from enums import *

# the puzzle that will be solved
# edit to contain the puzzle you want solved
PUZZLE = [["1", "2", "3", "4"],
          ["5", "6", "7", "8"],
          ["9", "10", "11", "12"],
          ["13", "14", "15", "_"]]

puzzle = Puzzle(PUZZLE)

# uncomment below to have puzzle shuffled automatically
# puzzle.shuffle(100)

solution = puzzle.astar()

for i in range(len(solution)):
    print(f"STEP {i+1} of {len(solution)}")
    print("move: ", solution[i].move)
    solution[i].puzzle.display()
    print()