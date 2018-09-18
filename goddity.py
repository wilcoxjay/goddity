import copy

import networkx as nx

class State:

    def step(self, action):
        pass

    def heuristic(self):
        pass

def run(state):

    init = copy.deepcopy(state)
    graph = nx.DiGraph()
    graph.add_node(init)
    old_states = [init]

    while True:
        print(state)

        # query the user
        possible = state.heuristic()
        for i, p in enumerate(possible):
            print('{}. {}'.format(i, p))

        while True:
            try:
                choice = input('Pick one: ')
                if choice == 'b':
                    choice = old_states.pop()
                    break
                choice = possible[int(choice)]
                break
            except Exception as e:
                print(e)
                pass

        # take the action
        if choice in graph:
            state = copy.deepcopy(choice)
        else:
            state.step(choice)
            new_state = copy.deepcopy(state)
            graph.add_edge(old_states[-1], new_state)
            old_states.append(new_state)
