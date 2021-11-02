try:
    import queue
except ImportError:
    import Queue as queue

from queue import PriorityQueue

graph = {
    'Sports Complex': {'Siwaka': 450},
    'Siwaka': {'Ph.1A': 10, 'Ph.1B': 230, 'Sports Complex': 450},
    'Ph.1A': {'Ph.1B': 100, 'Mada': 850, 'Siwaka': 10},
    'Ph.1B': {'Phase2': 112, 'STC': 50, 'Siwaka': 230},
    'STC': {'Parking lot': 250, 'Ph.1B': 50},
    'Phase2': {'J1': 600, 'Phase3': 500, 'Ph.1B': 112},
    'J1': {'Mada': 200, 'Phase2': 600},
    'Mada': {'Parking lot': 700, 'J1': 200, 'Ph1.A': 850},
    'Phase3': {'Parking lot': 350, 'Phase2': 500},
    'Parking lot': {'Phase3': 350, 'STC': 250, 'Mada': 700},

}

heuristic = {'Sports Complex': 730, 'Siwaka': 405, 'Ph.1A': 380, 'Ph.1B': 280, 'STC': 213, 'Phase2': 210, 'J1': 500,
             'Phase3': 160, 'Mada': 630, 'Parking lot': 0}


def greedy_best_first_search(problem: Problem):

    node = Node(problem, None, None)

    if (problem.goal_test(node.state)):
        return solution(node)

    frontier = []
    frontier_states = []
    frontier.append(node)
    frontier_states.append(node.state)

    explored = []

    while True:
        if (len(frontier) == 0):
            return []

        node = frontier.pop(0)
        frontier_states.pop(0)

        explored.append(node.state)

        actions = problem.get_actions(node.state)
        best_action = actions[0]
        for action in problem.get_actions(node.state):
            if (heuristics[action.dest] < heuristics[best_action.dest]):
                best_action = action

        child = Node(problem, node, best_action)

        if (child.state not in explored and child.state not in frontier_states):
            if (problem.goal_test(child.state)):
                return solution(child)
            frontier.append(child)
            frontier_states.append(child.state)