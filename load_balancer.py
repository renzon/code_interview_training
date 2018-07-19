U_MAX = 2


class Task:
    t_task = 4

    def __init__(self):
        self.missing_ticks = self.t_task

    def execute_tick(self):
        self.missing_ticks -= 1

    def finished(self):
        return self.missing_ticks <= 0

    def __repr__(self):
        return f'Task({self.missing_ticks})'


class Server:
    u_max = 2

    def __init__(self):
        self.tasks = []

    def is_full(self):
        return self.u_max == len(self.tasks)

    def is_empty(self):
        return 0 == len(self.tasks)

    def add(self, task):
        if not self.is_full():
            self.tasks.append(task)

    def execute_tick(self):
        for task in self.tasks:
            task.execute_tick()
        self.tasks = [t for t in self.tasks if not t.finished()]

    def __repr__(self):
        return f'Sever({self.tasks!r})'

    def __str__(self):
        return str(len(self))

    def __len__(self):
        return len(self.tasks)


class LoadBalancer:
    def __init__(self):
        self.servers = []
        self.cost = 0

    def __repr__(self):
        return f'LoadBalancer(cost={self.cost},{self.servers!r})'

    def execute_tick(self):
        for server in self.servers:
            server.execute_tick()
        self.cost += len(self)
        self.servers = [s for s in self.servers if not s.is_empty()]

    def handle(self, users):
        for _ in range(users):
            for server in self.servers:
                if not server.is_full():
                    server.add(Task())
                    break
            else:
                server = Server()
                server.add(Task())
                self.servers.append(server)

    def __len__(self):
        return len(self.servers)

    def __str__(self):
        return ','.join(str(s) for s in self.servers)


users_per_tick = [1, 3, 0, 1, 0, 1]

balancer = LoadBalancer()
for users in users_per_tick:
    balancer.execute_tick()
    # print(users, balancer)
    balancer.handle(users)
    print(balancer)

while len(balancer) != 0:
    balancer.execute_tick()
    print(balancer)

print(f'${balancer.cost}')
