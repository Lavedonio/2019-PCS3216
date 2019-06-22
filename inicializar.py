import numpy as np


class Memoria(object):
    """Inicializador da Memoria do PC"""
    def __init__(self):
        self.A1 = 0x0000
        self.A2 = 0x0000
        self.A3 = 0x0000
        self.A4 = 0x0000

        self.D1 = 0x0000
        self.D2 = 0x0000
        self.D3 = 0x0000
        self.D4 = 0x0000

        self.PC = 0x0000

        self.memoria_ram = np.zeros(int(str(0x10), 16), int(str(0x30), 16) / int(str(0x10), 16))

Computador = Memoria()

print(Computador.memoria_ram)
