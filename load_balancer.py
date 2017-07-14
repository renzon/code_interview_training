# Load Balancing is quite important in Cloud environments. We are always trying to minimize the costs so we keep the number of servers as low as possible. On the other hand we know that capacity and performance improves when we add more servers. The challenge is to keep the servers as busy as possible under a certain load capacity. On our simulation environment, at each clock tick (time unit), users connect to available servers and request the same task to be executed. Each task consumes Ttask ticks of time to get accomplished and after that the user disconnects immediately. The servers are virtual machines that can be spin up immediately to accommodate new users. Each servers costs $1.00 per clock tick and can handle with Umax number of simultaneous users. You can terminate the empty servers. Your challenge is to build a program in Python that handles with the incoming users and assign them to servers keeping the cost as low as possible. Input: A file where each line contains the number of new users for that tick. Output: A file where each line contains a list of the available servers at the end of that tick, represented by the number of users on each server. Example with Ttask	=	4 and Umax	=	2
#
#
# Clock Ticks
# Input
# Output
# Tip
# 1
# 1
# 1
# 1 server for 1 size. (1 server created)
# 2
# 3
# 2,2
# 2 servers for 4 users. (1 server created)
# 3
# 0
# 2,2
# idem
# 4
# 1
# 2,2,1
# 3 servers for 5 users. (1 server created)
# 5
# 0
# 1,2,1
# 3 servers for 4 users. (First size left after 4 ticks)
# 6
# 1
# 2
# 1 server for 2 users (3 users left, 1 joined. 2 servers terminated)


users_in = [1, 3, 0, 1, 0]

TTASK_TICKS = 4

TICK_COST = 1  # 1 USD

USER_MAX_SLOT = 2

servers = []


class UserTask():
    # tarefa
    def __init__(self):
        self.ticks = TTASK_TICKS


    def tick(self):
        self.ticks -= 1


    def finished(self):
        return self.ticks == 0


class Server():
    def __init__(self):
        print('Turning on a server')
        self.tasks = []

    def add_task(self, task):
        # verifica a quantidade maxima de usuarios por servidor
        if len(self.tasks) == USER_MAX_SLOT:
            return False
        self.tasks.append(task)
        return True


    def tick(self):
        for t in self.tasks:
            t.tick()
            # ticks ativas no servidor
        self.tasks = [t for t in self.tasks if not t.finished()]

        # usuarios ativos no momento, tarefas no momento


    def active_tasks_len(self):
        return len(self.tasks)


# [1,3,0,1,0,1]

# users_number= 1
#servers =[]
for users_number in users_in:
    # executando tick para todos servidores
    for s in servers:
        s.tick()

    # Remover servidor zerado
    server = [s for s in servers if s.active_tasks_len() >= 1]

    # numero de usuarios que acessam no momento

    def use_existing_server(task):
        for s in servers:
            task_appended = s.add_task(task)
            if task_appended:
                return True
        return False

    #users_number=1
    #i= 0
    for i in range(users_number):
        new_task = UserTask()
        # servidor ocioso
        task_appended = use_existing_server(new_task)
        if not task_appended:
            # novo servidor
            server = Server()
            server.add_task(new_task)
            servers.append(server)
        # tempo 4
        # server = [Server(UserTask(0), UserTask(1)), Server(UserTask(1), UserTask(1)), Server(UserTask(3)) ]
        # server = [Server(UserTask(1)), Server(UserTask(1), UserTask(1)), Server(UserTask(3)) ]

        # server = [Server(UserTask(0)), Server(UserTask(0), UserTask(0)), Server(UserTask(2)) ]

        # server = [Server(), Server(), Server(UserTask(2)) ]

        # server = [Server(UserTask(2), UserTask(4)) ]

    print([s.active_tasks_len() for s in servers])

# Output=[2]		



































