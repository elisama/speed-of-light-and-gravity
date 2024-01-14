"""

- Class sistema
- Classe corpo
1) Atualiza forças resultantes

2) Atualiza posição

3) Guarda posição de cada corpo em um arquivo

4) Atualiza imagem em tela

5) Estabiliza órbita elíptica

6) Inicia processo de desaceleração da luz

7) Restabelece velocidade da luz
"""
import class_OrbitingBody as ob

CONSTANTE_G = 1
LIMITE = 100

# carrega os dados iniciais de cada corpo do sistema
orbital_system = []
def carrega_dados_aleatorios():
    """
    fofoca 2
    """
    for i in range(1, 10):
        orbital_system.append(ob.OrbitingBody(i, i+2, i+3, i+4, i+5))

# Simula o sistema
carrega_dados_aleatorios()
for i, linha in enumerate(orbital_system):
    print(f'{linha.mass}, {linha.velocity_x}, {linha.velocity_y}')
