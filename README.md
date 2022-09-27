# 15 Puzzle Solver
Multiple implementations of a 15 puzzle solver and a 15 puzzle terminal game.

1. [ Game ](https://github.com/cgr28/15-puzzle-solver#game)
2. [ Solver ](https://github.com/cgr28/15-puzzle-solver#solver)

## Game
### Installation
```bash
pip install click
```

### Usage
```bash
python3 game.py -s [number of shuffles]
```
### Args
- -s - The number of times the board will be shuffled.
**[Default: 250] [optional] [example: -s 50]**
### Help
```bash
python3 game.py --help
```
### Examples
Start a game with 250 shuffles
```bash
python3 game.py -s 250
```


## Solver
### Usage
1. Edit the [PUZZLE](https://github.com/cgr28/15-puzzle-solver/blob/main/solver.py#L10) variable with your puzzle configuration.
2. Call ```python3 solver.py [astar|idastar|bfs] [number of shuffles]``` to generate a solution.
### Args
- solver - The solver that will be used to solve the 15 puzzle.
**[Options: astar | idastar | bfs] [required] [example: astar]**
- shuffles - The number of time the board will be shuffled.
**[Default: 0] [optional] [example: 50]**
### Solvers
#### [Best First Search](https://github.com/cgr28/15-puzzle-solver/blob/main/puzzle.py#L159)
Generates a solution the fastest. Solution not guranteed to be optimal.
#### [A*](https://github.com/cgr28/15-puzzle-solver/blob/main/puzzle.py#L192)
Takes longer to generate solutinons. Solutions are optimal.
#### [IDA*](https://github.com/cgr28/15-puzzle-solver/blob/main/puzzle.py#L235)
Takes longer to generate solutinons. Solutions are optimal.
### Examples
Solve a puzzle using astar with no shuffles.
```bash
python3 solver.py astar 0
```
Solve a puzzle using idastar with 10 shuffles.
```bash
python3 solver.py idastar 10
```
Solve a puzzle using bfs with 50 shuffles.
```bash
python3 solver.py bfs 50
```

## License
[MIT](https://github.com/cgr28/15-puzzle-solver/blob/main/LICENSE)
