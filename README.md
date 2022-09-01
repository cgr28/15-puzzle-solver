<h1 align="center">15 Puzzle Solver</h1>
Multiple implementations of a 15 puzzle solver and a 15 puzzle terminal game.

## Solvers
Solves a 15 puzzle using A*, IDA*, or best first search using a manhattan distance heuristic.
### Usage
1. Edit the [PUZZLE](https://github.com/cgr28/15-puzzle-solver/blob/main/solver.py#L10) variable in solver.py with your puzzle configuration.
2. ```python3 solver.py <astar|idastar|bfs> <number of shuffles>```

### Examples
1. Generate a solution using BFS and a board shuffled 100 times.
<br/>

   ```python3 solver.py bfs 100```
<br/>

1. Generate a solution using A* and a board shuffled 0 times.
<br/>

   ```python3 solver.py astar 0```
<br/>

3. Generate a solution using IDA* and a board shuffled 50 times.
<br/>

   ```python3 solver.py idastar 50```

Note: IDA\* and A\* may take a some time to find a optimal solution on more complex puzzles

## Game
A 15 puzzle game played in the terminal.
### Usage
1. ```pip install --editable .```
2. ```15-puzzle```

or

1. ```pip install click```
2. ```python3 game.py```

### How-to
#### Get help
```15-puzzle --help```
<br/>
or
<br/>

```python3 game.py --help```

#### Change number of shuffles
```15-puzzle -s <number of shuffles>```
<br/>
or
<br/>

```python3 game.py -s <number of shuffles>```

### Example
1. Start a game with a board shuffled 100 times.
<br />

   ```15-puzzle -s 100```
<br/>
or
<br/>

   ```python3 game.py -s 100```
