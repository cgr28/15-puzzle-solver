<h1 align="center">15 Puzzle Solver</h1>
A 15 puzzle solver and terminal game.

## Solver
Solves a 15 puzzle of any configuration using A*.
### Usage
1. Edit the ```PUZZLE``` variable in solver.py with your puzzle configuration.
2. ```python3 solver.py```

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