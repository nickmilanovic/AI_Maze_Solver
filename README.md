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
