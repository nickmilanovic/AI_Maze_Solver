"""
Basic Maze Implementation

API
===
start_state: returns a starting state based on position of c of top row of maze
next_states: returns list of possible next states
is_goal: returns True when the state[1] tuple is the same as the end state coordinates
get_goal_coordinates: returns the coordinates of the 'c' index of the last row of the maze

Nick Milanovic, 000292701 April 2023

"""

import copy, random
from path import *
from prim_maze_generator import *


def start_state(maze):
    """ extract the coordinates of the 'c' index in
    the top row of the maze, return as a tuple"""
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'c':
                return (i, j) # Return the tuple of c coordinate in top row


def is_goal(maze, state):
    """ extract the end state and coordinates of the last row of the maze"""
    end_state = None
    for row_idx, row in enumerate(maze):
        if 'c' in row:
            end_state = (row_idx, row.index('c'))   # Return a tuple of c coordinate in last row
    return state[1] == end_state

def get_goal_coordinates(maze):
    """ extract only the coordinates of the 'c' index of the last row of the maze"""
    end_state = None
    for row_idx, row in enumerate(maze):
        if 'c' in row:
            end_state = (row_idx, row.index('c'))  # Return a tuple of c coordinate in last row
    return end_state


def next_states(state):
    """ returns a list of all states reachable from the given state"""
    maze, current_loc = state
    x, y = current_loc
    children = []

    # Check adjacent cells that are not walls
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_loc = (x + dx, y + dy)
        if (0 <= next_loc[0] < len(maze) and
            0 <= next_loc[1] < len(maze[0]) and
            maze[next_loc[0]][next_loc[1]] != 'w'):
            # Valid move, add new state
            children.append((maze, next_loc))

    return children
