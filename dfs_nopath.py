"""Implementation of Depth-First Search, Breadth-First Search and Heuristic Search with pruning of visited
nodes. Relies on is_goal and next_states methods that must be imported from
elsewhere.

Sam Scott, Mohawk College, December 2022
Modified by: Nick Milanovic 000292701, April 2023

For the heuristic search I did use the A* algorithm and the f function I have provided
uses the manhattan distance as it is more suitable for grid searching situations, such as
our puzzle. What it is doing is calculating the absolute distances between the current state
and the goal state which is better than euclidean distances. Euclidean distances are straight
line distances between coordinates whereas manhattan are along the axes at right angles, making
it more suitable for the grid-based maze we have printed.

Firstly, I use my start_state and my maze variabes as parameters for my heuristic function at the
start of the A* algorithm.

Next, I remove them from the queue in order to add them to the closed state list, and lastly,
I add the new state to the priority queue once again to complete the process of getting to the end
state.

The reason I stuck with this heuristic algorithm is because it operates on average 10-11x faster
than a breadth-first search as well as keeping around the same amount of steps as the shortest path found by
the breadth-first search.

"""
## import LifoQueue, Queue, PriorityQueue
from queue import LifoQueue, Queue, PriorityQueue

## import puzzle api
from path import create_path, add_state_to_path, print_path
from maze_puzzle import *


## DFS solver
def DFS(start_state, maze):
    closed = []                 # init open, closed
    open = LifoQueue()
    open.put((start_state, create_path(start_state)))

    while not open.empty():        # loop until no more open states

        state, path = open.get(False)    # get next state to expand

        if state not in closed:    # prune?

            closed.append(state)   # mark state visited (closed)

            if is_goal(maze, state):     # success?
                print()
                print("Number of steps:",len(path)-1)
                #print_maze_path(maze, path)
                return True

            for new_state in next_states(state):    # expand state
                new_path = add_state_to_path(path, new_state)
                if new_state not in closed:
                    open.put((new_state, new_path))      # new states are open
    return False              # goal not found


## BFS solver
def BFS(start_state, maze):
    closed = []                 # init open, closed
    open = Queue()
    open.put((start_state, create_path(start_state)))

    while not open.empty():        # loop until no more open states

        state, path = open.get(False)    # get next state to expand

        if state not in closed:    # prune?

            closed.append(state)   # mark state visited (closed)

            if is_goal(maze, state):     # success?
                print()
                print("Number of steps:",len(path)-1)
                return True

            for new_state in next_states(state):    # expand state
                new_path = add_state_to_path(path, new_state)
                if new_state not in closed:
                    open.put((new_state, new_path))      # new states are open

    return False              # goal not found


## AStar solver
def AStar(start_state, maze):
    closed = []                     # init open, closed
    open = PriorityQueue()
    path = create_path(start_state)
    cost = f(start_state, maze)     # init cost using heuristic function (f)
    open.put((cost, start_state, path))

    while not open.empty():         # loop until no more open states
        cost, state, path = open.get(False) # get next state and cost to expand

        if state not in closed:     # prune?
            closed.append(state)    # mark state visited
            new_path = add_state_to_path(path, state)

            goal_loc = get_goal_coordinates(maze)
            if state[1] == goal_loc:
                print()
                print("Number of steps:",len(path)-1)
                return True

            for new_state in next_states(state):    # expand state
                new_cost = f(new_state, maze)
                open.put((new_cost, new_state, new_path))   # new states are open

    return False                       # goal not found

## Heuristic search
def f(state, maze):
    goal_row, goal_col = get_goal_coordinates(maze)
    row, col = state[1]
    return abs(goal_row - row) + abs(goal_col - col)

## run the solvers
from time import time
width = int(input("Please enter a width: "))
height = int(input("Please enter a height: "))

maze = generate_maze(height, width, True)
print()
print("====================DFS====================")
print()
print_maze(maze)

initial_state = (maze, start_state(maze))

start = time()
result = DFS(initial_state, maze)
end = time()
print()
print("Result: ", result)
print("Time:",end-start,"seconds")

print()
print("====================BFS====================")
print()
print_maze(maze)

start = time()
result = BFS(initial_state, maze)
end = time()
print()
print("Result: ", result)
print("Time:",end-start,"seconds")

print()
print("====================BeFS====================")
print()
print_maze(maze)

start = time()
result = AStar(initial_state, maze)
end = time()
print()
print("Result: ", result)
print("Time:",end-start,"seconds")