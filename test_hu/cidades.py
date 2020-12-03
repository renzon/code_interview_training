estados = [
    (1, 'Acre', 'AC', 1),
    (2, 'Alagoas', 'AL', 1),
    (3, 'Amazonas', 'AM', 1),
    (4, 'Amapá', 'AP', 1),
    (5, 'Bahia', 'BA', 1),
    (6, 'Ceará', 'CE', 1),
    (7, 'Distrito Federal', 'DF', 1),
    (8, 'Espírito Santo', 'ES', 1),
    (9, 'Goiás', 'GO', 1),
    (10, 'Maranhão', 'MA', 1),
    (11, 'Minas Gerais', 'MG', 1),
    (12, 'Mato Grosso do Sul', 'MS', 1),
    (13, 'Mato Grosso', 'MT', 1),
    (14, 'Pará', 'PA', 1),
    (15, 'Paraíba', 'PB', 1),
    (16, 'Pernambuco', 'PE', 1),
    (17, 'Piauí', 'PI', 1),
    (18, 'Paraná', 'PR', 1),
    (19, 'Rio de Janeiro', 'RJ', 1),
    (20, 'Rio Grande do Norte', 'RN', 1),
    (21, 'Rondônia', 'RO', 1),
    (22, 'Roraima', 'RR', 1),
    (23, 'Rio Grande do Sul', 'RS', 1),
    (24, 'Santa Catarina', 'SC', 1),
    (25, 'Sergipe', 'SE', 1),
    (26, 'São Paulo', 'SP', 1),
    (27, 'Tocantins', 'TO', 1)
]


def normalizar(estado):
    estado = estado.lower().replace(' ', '-').replace('á', 'a_com_fatia_linar').replace('ã', 'a_com_fatia_linar').replace('í', 'i')
    return estado


estados_nomes = {normalizar(tpl[1]): tpl[1] for tpl in estados}

print(estados_nomes)
