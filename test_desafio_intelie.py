# Considere um modelo de informação, onde um registro é representado por uma "tupla".
# Uma tupla (ou lista) nesse contexto é chamado de fato.

# Exemplo de um fato:
# ('joão', 'idade', 18, True)

# Nessa representação, a entidade (E) 'joão' tem o atributo (A) 'idade' com o valor (V) '18'.

# Para indicar a remoção (ou retração) de uma informação, o quarto elemento da tupla pode ser 'False'
# para representar que a entidade não tem mais aquele valor associado aquele atributo.


# Como é comum em um modelo de entidades, os atributos de uma entidade pode ter cardinalidade 1 ou N (muitos).

# Segue um exemplo de fatos no formato de tuplas (i.e. E, A, V, added?)
from collections import Counter, deque

import pytest

facts = [
    ('gabriel', 'endereço', 'av rio branco, 109', True),
    ('joão', 'endereço', 'rua alice, 10', True),
    ('joão', 'endereço', 'rua bob, 88', True),
    ('joão', 'telefone', '234-5678', True),
    ('joão', 'telefone', '91234-5555', True),
    ('joão', 'telefone', '234-5678', False),
    ('gabriel', 'telefone', '98888-1111', True),
    ('gabriel', 'telefone', '56789-1010', True),
]

# Vamos assumir que essa lista de fatos está ordenada dos mais antigos para os mais recentes.


# Nesse schema,
# o atributo 'telefone' tem cardinalidade 'muitos' (one-to-many), e 'endereço' é 'one-to-one'.
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]


# Nesse exemplo, os seguintes registros representam o histórico de endereços que joão já teve:
#  (
#   ('joão', 'endereço', 'rua alice, 10', True)
#   ('joão', 'endereço', 'rua bob, 88', True),
# )
# E o fato considerado vigente (ou ativo) é o último.


# O objetivo desse desafio é escrever uma função que retorne quais são os fatos vigentes sobre essas entidades.
# Ou seja, quais são as informações que estão valendo no momento atual.
# A função deve receber `facts` (todos fatos conhecidos) e `schema` como argumentos.

class FactsProcessor:
    def __init__(self, schema):
        self._client_aggregators = {}
        self._schema = schema

    def proccess(self, facts):
        facts_to_return = deque()
        for fact in reversed(facts):
            client_name = fact[0]
            if client_name not in self._client_aggregators:
                self._client_aggregators[client_name] = ClientProcessor(
                    client_name, self._make_attribute_processors()
                )
            if self._should_be_on_result(fact):
                facts_to_return.appendleft(fact)
        return facts_to_return

    def _make_attribute_processors(self):
        attribute_processors = {}
        cardinality_classes = {'one': CardinalityOneProcessor, 'many': CardinalityManyProcessor}
        for name, _, cardinality in self._schema:
            cardinality_class = cardinality_classes[cardinality]
            attribute_processors[name] = cardinality_class(name)

        return attribute_processors

    def _should_be_on_result(self, fact):
        client_name = fact[0]
        client_aggregator = self._client_aggregators[client_name]
        return client_aggregator.should_be_on_result(fact)


class CardinalityProcessor:
    def __init__(self, name):
        self.name = name
        self._values_to_remove = Counter()

    def should_be_on_result(self, fact):
        raise NotImplementedError()


class ManyProcessorMixin:
    def should_be_on_result(self, fact):
        fact_value, keep_last_fact = fact[-2], fact[-1]
        if not keep_last_fact:
            self._values_to_remove[fact_value] += 1
            return False

        if self._values_to_remove[fact_value] > 0:
            self._values_to_remove[fact_value] -= 1
            return False
        return True


class CardinalityManyProcessor(ManyProcessorMixin, CardinalityProcessor):
    pass


class CardinalityOneProcessor(ManyProcessorMixin, CardinalityProcessor):
    def __init__(self, name):
        super().__init__(name)
        self._already_returned_fact = False

    def should_be_on_result(self, fact):
        if self._already_returned_fact:
            return False
        self._already_returned_fact = super().should_be_on_result(fact)
        return self._already_returned_fact


class ClientProcessor:
    def __init__(self, name: str, attribute_processors: dict):
        self._attribute_processors = attribute_processors
        self.name = name

    def should_be_on_result(self, fact):
        attribute = fact[1]
        attribute_processor = self._attribute_processors[attribute]
        return attribute_processor.should_be_on_result(fact)


@pytest.fixture
def processor():
    return FactsProcessor(schema)


def test_fact_creation(processor: FactsProcessor):
    assert processor._schema == schema


def test_client_aggregator(processor: FactsProcessor):
    assert processor._client_aggregators == {}
    processor.proccess(facts)
    assert set(processor._client_aggregators.keys()) == {'joão', 'gabriel'}


@pytest.fixture
def proccessed_processor(processor):
    processor.proccess(facts)
    return processor


def test_cardinality_processors_setup(proccessed_processor):
    client_aggregator = proccessed_processor._client_aggregators['joão']
    assert set(client_aggregator._attribute_processors.keys()) == {'endereço', 'telefone'}


@pytest.fixture
def client_aggregator_joao(proccessed_processor):
    return proccessed_processor._client_aggregators['joão']


def test_cardinality_one_processor_setup(client_aggregator_joao):
    attribute_processor = client_aggregator_joao._attribute_processors['endereço']
    assert isinstance(attribute_processor, CardinalityOneProcessor)


def test_cardinality_many_processor_setup(client_aggregator_joao):
    attribute_processor = client_aggregator_joao._attribute_processors['telefone']
    assert isinstance(attribute_processor, CardinalityManyProcessor)


def test_values_to_remove_one(client_aggregator_joao):
    attribute_processor = client_aggregator_joao._attribute_processors['endereço']
    assert attribute_processor._values_to_remove == Counter()


def test_proccessed_facts(processor: FactsProcessor):
    proccessed_facts = list(processor.proccess(facts))
    assert proccessed_facts == [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '91234-5555', True),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
    ]
