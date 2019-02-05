"""
Solução para o balanceador de carga

>>> tarefa = Tarefa(t_task=4)
>>> tarefa._tiques_para_terminar
4
>>> tarefa.tique()
3
>>> tarefa.tique()
2
>>> tarefa.esta_ativa()
True
>>> tarefa.tique()
1
>>> tarefa.esta_ativa()
True
>>> tarefa.tique()
0
>>> tarefa.esta_ativa()
False
>>> servidor = Servidor(u_max=2)
>>> servidor.possui_tarefas()
False
>>> str(servidor)
'0'
>>> servidor.adicionar_usuario()
True
>>> str(servidor)
'1'
>>> servidor.possui_tarefas()
True
>>> servidor.adicionar_usuario()
True
>>> str(servidor)
'2'
>>> servidor.possui_tarefas()
True
>>> servidor.adicionar_usuario()  # Terceiro usuário não pode ser adocionado
False
>>> str(servidor)
'2'
>>> servidor.tique()
>>> str(servidor)
'2'
>>> servidor.tique()  # precisa de 4 tiques para terminar
>>> servidor.tique()
>>> str(servidor)
'2'
>>> servidor.tique()
>>> str(servidor)
'0'
>>> balanceador=BalancedorDeCarga()
>>> str(balanceador)
''
>>> balanceador.servir_usuarios(n_usuario=1)
>>> str(balanceador)
'1'
>>> balanceador.tique()
>>> str(balanceador)
'1'
>>> balanceador.servir_usuarios(3)
>>> str(balanceador)
'2,2'
>>> balanceador.tique()
>>> str(balanceador)
'2,2'
>>> balanceador.servir_usuarios(0)
>>> str(balanceador)
'2,2'
>>> balanceador.tique()
>>> str(balanceador)
'2,2'
>>> balanceador.servir_usuarios(1)
>>> str(balanceador)
'2,2,1'
>>> balanceador.tique()
>>> str(balanceador)
'1,2,1'
>>> balanceador.servir_usuarios(0)
>>> str(balanceador)
'1,2,1'
>>> balanceador.tique()
>>> str(balanceador)
'1'
>>> balanceador.servir_usuarios(1)
>>> str(balanceador)
'2'
>>> balanceador.possui_servidores_ativos()
True
>>> balanceador.tique()
>>> str(balanceador)
'2'
>>> balanceador.tique()
>>> str(balanceador)
'1'
>>> balanceador.tique()
>>> str(balanceador)
'1'
>>> balanceador.tique()
>>> str(balanceador)
''
>>> balanceador.possui_servidores_ativos()
False
"""


class BalancedorDeCarga:
    def __init__(self):
        self._servidores = []

    def __str__(self):
        return ','.join(str(s) for s in self._servidores)

    def servir_usuarios(self, n_usuario):

        for servidor in self._servidores:
            for i in range(n_usuario):
                adicinou = servidor.adicionar_usuario()
                if adicinou:
                    n_usuario -= 1
                else:
                    break
        if n_usuario > 0:
            self._servidores.append(Servidor())
            self.servir_usuarios(n_usuario)

    def tique(self):
        for servidor in self._servidores:
            servidor.tique()
        self._servidores = list(filter(lambda servidor: servidor.possui_tarefas(), self._servidores))

    def possui_servidores_ativos(self):
        return bool(self._servidores)


class Servidor:
    def __init__(self, u_max=2):
        self._u_max = u_max
        self._tarefas = []

    def possui_tarefas(self):
        return len(self._tarefas) > 0

    def adicionar_usuario(self):
        if len(self._tarefas) >= self._u_max:
            return False
        self._tarefas.append(Tarefa())
        return True

    def __str__(self):
        return str(len(self._tarefas))

    def tique(self):
        for tarefa in self._tarefas:
            tarefa.tique()

        self._tarefas = [t for t in self._tarefas if t.esta_ativa()]


class Tarefa:
    def __init__(self, t_task=4):
        self._tiques_para_terminar = t_task

    def tique(self):
        self._tiques_para_terminar -= 1
        return self._tiques_para_terminar

    def esta_ativa(self):
        """
        Informa se tarefa está ativa. True -> está ativa, False -> Não está tiva
        :return: bool
        """
        return self._tiques_para_terminar > 0
