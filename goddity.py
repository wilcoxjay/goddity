import copy
import networkx as nx
import http.server

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

STATIC_FILES = {
    '/': 'index.html',
    '/index.html': 'index.html',
    '/main.js': 'main.js',
}

class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path in STATIC_FILES:
            self.send_response(200)
            self.end_headers()
            with open(STATIC_FILES[self.path], 'rb') as f:
                self.wfile.write(f.read())
                return
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            self.wfile.write(self.server.render_choices())

class Server(http.server.HTTPServer):
    def __init__(self, address, state, req_handler = RequestHandler):
        self.state = state

        init = copy.deepcopy(state)
        self.graph = nx.DiGraph()
        self.graph.add_node(init)
        self.old_states = [init]

        self.possible = state.heuristic()

        super().__init__(address, req_handler)

    def render_choices(self):
        lines = []

        for i, p in enumerate(self.possible):
            s = self.state.render_action(p)
            lines.append('{}. {}'.format(i, s))

        return str.encode('\n'.join(lines))

    def step(self):
        pass

def run_app(state):

    PORT = 5000
    print("hellow")
    with Server(("", PORT), state) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
