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
import time
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


def Stack_Empty_Check(stack):
    if stack.isEmpty():
        return True
    else:
        return False

def Problem_Goal_State_Check(problem, node):
    if problem.isGoalState(node):
        return True
    else:
        return False
def Successor(problem, node):
    return problem.getSuccessors(node)


def Explored_Check(successor, explored_list, uniformcost):
    for i in range(len(explored_list)):
        E=explored_list[i]
        if (uniformcost>=E[1]):
            if (successor[0]==E[0]):
                return True

def depthFirstSearch(problem):
    stack = util.Stack()
    path_array = []
    stack.push((problem.getStartState(), path_array))
    explored_list = set()
    while Stack_Empty_Check(stack) is False:
        (node, path) = stack.pop()
        if Problem_Goal_State_Check(problem, node) is True:
            return path
        else:
            explored_list.add(node)
        for i in Successor(problem, node):
            if i[0] not in explored_list:
                stack.push((i[0], path + [i[1]]))

def breadthFirstSearch(problem):
    queue=util.Queue()
    queue.push((problem.getStartState(),[],0))
    node,path,search_cost=queue.pop()
    explored_list=[node]
    while Problem_Goal_State_Check(problem, node) is False:
      for i in Successor(problem, node):
        if i[0] not in explored_list:
          queue.push((i[0],path+[i[1]],search_cost+i[2]))
          explored_list.append(i[0])
      node,path,search_cost=queue.pop()
    return  path


def uniformCostSearch(problem):
    P_queue=util.PriorityQueue()
    P_queue.push((problem.getStartState(),[],0),0)
    node,path,search_cost=P_queue.pop()
    explored_list=[(node,0)]
    
    while Problem_Goal_State_Check(problem, node) is False:
        for successor in Successor(problem, node):
            uniformcost=problem.getCostOfActions(path+[successor[1]])
            if Explored_Check(successor, explored_list, uniformcost) is not True:
                explored_list.append((successor[0],uniformcost))
                P_queue.push((successor[0],path+[successor[1]],uniformcost),uniformcost)
        node,path,search_cost=P_queue.pop()
    return  path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    P_queue=util.PriorityQueue()
    P_queue.push((problem.getStartState(),[],0),0)
    node,path,search_cost=P_queue.pop()
    explored_list=[(node,0)]
    while Problem_Goal_State_Check(problem, node) is False:
        for successor in Successor(problem, node):
            aStarcost=problem.getCostOfActions(path+[successor[1]])
            if Explored_Check(successor, explored_list, aStarcost) is not True:
                aStarcost=problem.getCostOfActions(path+[successor[1]])
                P_queue.push((successor[0],path+[successor[1]],aStarcost),aStarcost+heuristic(successor[0],problem))
                explored_list.append((successor[0],aStarcost))
        node,path,search_cost=P_queue.pop()
    return  path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
