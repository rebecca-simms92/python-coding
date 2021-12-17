# Game-of-Life Challenge

# Day 4 - Rebecca and Josh

The Game of Life (an example of a cellular automaton) is played on an infinite two-dimensional rectangular grid of cells. Each cell can be either alive or dead.
The status of each cell changes each turn of the game (also called a generation) depending on the statuses of that cell's 8 neighbours. Neighbours of a cell are cells that touch that cell,
either horizontal, vertical, or diagonal from that cell.

The “game” is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial
configuration and observing how it evolves, or, for advanced “players”, by creating patterns with particular properties. The initial pattern is the first generation. The second generation
evolves from applying the rules simultaneously to every cell on the game board, i.e. births and deaths happen simultaneously. Afterwards, the rules are iteratively applied to create
future generations. For each generation of the game, a cell's status in the next generation is determined by a set of rules.

## The Rules

Start with our Game of Life board. This will be a n-by-n square grid of "cells", each of which can be either "alive" or "dead". A given cell's neighbours are those directly above, below,
left or right of the cell, plus any cells diagonally adjacent to it (the cells touching its diagonals). This can also be understood as any cells belonging to the eight-location neighbourhood of the cell.

At each step, we count the number of neighbour cells that are alive and:

Any live cell with fewer than two live neighbours dies, as if caused by under-population.

Any live cell with two or three live neighbours lives on to the next generation.

Any live cell with more than three live neighbours dies, as if by overcrowding.

Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

 C   N                 new C
 1   0,1             ->  0  # Lonely
 1   4,5,6,7,8       ->  0  # Overcrowded
 1   2,3             ->  1  # Lives
 0   3               ->  1  # It takes three to give birth!
 0   0,1,2,4,5,6,7,8 ->  0  # Barren
