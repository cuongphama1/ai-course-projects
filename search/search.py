# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    visited = set()  # create an empty set to keep track of visited states
    stack = util.Stack()  # create a stack using the Stack class from the util module
    stack.push((problem.getStartState(), []))  # push the starting state and an empty action list to the stack

    while not stack.isEmpty():  # loop until the stack is empty
        state, actions = stack.pop()  # get the state and its associated action list from the top of the stack
        if problem.isGoalState(state):  # if the current state is the goal state, return the action list
            return actions
        if state not in visited:  # if the current state has not been visited
            visited.add(state)  # add the current state to the visited set
            for next_state, action, _ in problem.getSuccessors(state):  # loop through the successor states and actions
                if next_state not in visited:  # if the successor state has not been visited
                    stack.push((next_state, actions + [action]))  # add the successor state and its action to the stack
    return []  # return an empty list if no goal state is found
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue = Queue()
    visited = set()

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    queue.push((startState, []))

    while not queue.isEmpty():
        state, actions = queue.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return actions

        successors = problem.getSuccessors(state)
        for successor, action, stepCost in successors:
            if successor not in visited:
                queue.push((successor, actions + [action]))

    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    queue = PriorityQueue()
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []
    queue.push((start_state, []), 0)
    visited = set()
    cost_cache = {start_state: 0}
    while not queue.isEmpty():
        current, path = queue.pop()
        if current in visited:
            continue
        visited.add(current)
        if problem.isGoalState(current):
            return path
        current_cost = cost_cache[current]
        for successor, action, step_cost in problem.getSuccessors(current):
            new_cost = current_cost + step_cost
            if successor in cost_cache and new_cost >= cost_cache[successor]:
                continue
            cost_cache[successor] = new_cost
            queue.push((successor, path + [action]), new_cost)
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    pq = PriorityQueue()
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    pq.push((start, []), 0)
    visited = set()
    cost_so_far = {start: 0}
    while not pq.isEmpty():
        current, path = pq.pop()
        if current in visited:
            continue
        visited.add(current)
        if problem.isGoalState(current):
            return path
        current_cost = cost_so_far[current]
        for successor, action, step_cost in problem.getSuccessors(current):
            new_cost = current_cost + step_cost
            if successor in cost_so_far and new_cost >= cost_so_far[successor]:
                continue
            cost_so_far[successor] = new_cost
            priority = new_cost + heuristic(successor, problem)
            pq.push((successor, path + [action]), priority)
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
