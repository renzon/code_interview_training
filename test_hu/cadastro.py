from test_hu.test_cadastro import top_colaborador

colaboradores = [
    ('Joao Pereira', [25, 'joao.pereira@hurb.com', 'marketing', 1950]),
    ('Maria Silva', [23, 'maria.silva@hurb.com', 'comercial', 2300]),
    ('Pedro Peixoto', [32, 'pedro.peixoto@hurb.com', 'operacao', 2625]),
    ('Pedro Peixoto', [32, 'pedro.peixoto@hurb.com', 'operacao', 2625]),
    ('Luiza Almeida', [28, 'luiza.almeida@hurb.com', 'atendimento', 2120]),
    ('Luana', [18, 'luiza.almeida@hurb.com', 'atendimento', 8120]),
]

print(top_colaborador(colaboradores))