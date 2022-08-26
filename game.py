# game.py -- terminal sliding puzzle game

from puzzle import Puzzle
from enums import *
import click

SOLUTION = [["1", "2", "3", "4"],["5", "6", "7", "8"],["9", "10", "11", "12"],["13", "14", "15", "_"]]

def cli_puzzle(puzzle):
    click.secho("{:^8} {:^8} {:^8} {:^8}".format(puzzle[0][0], puzzle[0][1], puzzle[0][2], puzzle[0][3]), overline=True)
    click.secho()
    click.secho("{:^8} {:^8} {:^8} {:^8}".format(puzzle[1][0], puzzle[1][1], puzzle[1][2], puzzle[1][3]), overline=True)
    click.secho()
    click.secho("{:^8} {:^8} {:^8} {:^8}".format(puzzle[2][0], puzzle[2][1], puzzle[2][2], puzzle[2][3]), overline=True)
    click.secho()
    click.secho("{:^8} {:^8} {:^8} {:^8}".format(puzzle[3][0], puzzle[3][1], puzzle[3][2], puzzle[3][3]), overline=True)

def solver(puzzle):
    c = None
    click.clear()
    click.secho("solving puzzle...")
    click.clear()
    solution = puzzle.solution()
    index = 0
    while c != "x":
        puzzle = solution[index].puzzle
        click.secho("solver mode", blink=True)
        click.secho()
        cli_puzzle(puzzle.puzzle)
        click.secho()
        click.secho(f"step {index+1} of {len(solution)}")
        click.secho("keys w and d - change step")
        click.secho("x - exit solver mode")
        click.secho("ctrl + c - exit game")
        c = click.getchar()
        click.clear()
        if c == 'a':
            if index > 0:
                index -= 1
        elif c == 'd':
            if index < len(solution) - 1:
                index += 1
        else:
            continue
    return solution[index].puzzle

@click.command()
@click.option("--shuffle", "-s", type=int, default=250, help="number of times slide puzzle is shuffled")
def cli(shuffle):
    """A command line implementation of the famous slide/15 puzzle.
    
    controls

        regular:

            w - slide piece below empty into the above space

            a - slide piece to the right of empty into the left space

            s - slide piece above empty into the below space

            d - slide piece to the left of empty into the right space

            x - enter solver mode

            ctrl + c - exit game

        solver:

            w - move to a previous step  d - move to the next step

            x - exit solver mode

            ctrl + c - exit game
    
    about

        solver mode:

            - solves the board and shows each step that must be taken to achieve solution

            - exit to resume game from current step

        moves:

            - the number of moves that have been made

        empty:

            - the empty space in the slide puzzle is denoted by an underscore _

        goal:

            - arrange the pieces of the puzzle in sequential order e.g.

                1   2   3   4

                5   6   7   8

                9   10  11  12

                13  14  15  _
    """
    puzzle = Puzzle()
    puzzle.shuffle(shuffle)
    solver_used = False
    moves = 0
    while puzzle.puzzle != SOLUTION:
        cli_puzzle(puzzle.puzzle)
        click.secho()
        click.secho("keys w, a, s, and d - slide pieces")
        click.secho("x - enter solver mode")
        click.secho("ctrl + c - exit game")
        click.secho(f"moves: {moves}")
        c = click.getchar()
        click.clear()

        if c == "a":
            puzzle.slide(Moves.LEFT)
        elif c == 'd':
            puzzle.slide(Moves.RIGHT)
        elif c == 'w':
            puzzle.slide(Moves.UP)
        elif c == 's':
            puzzle.slide(Moves.DOWN)
        elif c == "x":
            puzzle = solver(puzzle)
            solver_used = True
        else:
            continue
        moves += 1
    
    click.secho(f"Puzzle solved in {moves} moves!")
    if solver_used:
        click.secho(f"Solver was used.")
 
if __name__ == '__main__':
    cli()