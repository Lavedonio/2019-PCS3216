import random


class Inicializar_Memoria_Virtual(object):
    """Inicializador da Memoria do PC"""

    def __init__(self):
        self.D0 = 0x0000
        self.D1 = 0x0000
        self.D2 = 0x0000
        self.D3 = 0x0000

        self.A0 = 0x0000
        self.A1 = 0x0000
        self.A2 = 0x0000

        self.PC = 0x0000

        init_mem = []
        linha = []

        for i in range(int(0x10)):
            linha.append("00")

        for i in range(int(0x110) // int(0x10)):
            linha = linha[:]
            init_mem.append(linha)

        self.mem = init_mem

    def limpar(self):
        ''' Limpa a memória, zerando todos os seus valores. '''

        init_mem = []
        linha = []

        for i in range(int(0x10)):
            linha.append("00")

        for i in range(int(0x110) // int(0x10)):
            linha = linha[:]
            init_mem.append(linha)

        self.mem = init_mem

    def corromper(self):
        ''' Coloca valores aleatórios nas posições de memória. Apenas para teste. '''
        init_mem = []

        for i in range(int(0x110) // int(0x10)):
            linha = []

            for j in range(int(0x10)):
                linha.append("{:02X}".format(random.randint(0, 255)))
            init_mem.append(linha)

        self.mem = init_mem

    def atualizar_registradores(self):
        ''' Atualiza os registradores com os valores na linha oculta da memória. '''

        registradores = self.mem[0]
        self.D0 = int(registradores[0] + registradores[1], 16)
        self.D1 = int(registradores[2] + registradores[3], 16)
        self.D2 = int(registradores[4] + registradores[5], 16)
        self.D3 = int(registradores[6] + registradores[7], 16)

        self.A0 = int(registradores[8] + registradores[9], 16)
        self.A1 = int(registradores[10] + registradores[11], 16)
        self.A2 = int(registradores[12] + registradores[13], 16)
        self.PC = int(registradores[14] + registradores[15], 16)

    def atualizar_memoria(self):
        ''' Atualiza a memória da linha ocultacom os valores dos registradores. '''

        D0 = "{:04X}".format(self.D0)
        self.mem[0][0] = D0[:2]
        self.mem[0][1] = D0[2:]

        D1 = "{:04X}".format(self.D1)
        self.mem[0][2] = D1[:2]
        self.mem[0][3] = D1[2:]

        D2 = "{:04X}".format(self.D2)
        self.mem[0][4] = D2[:2]
        self.mem[0][5] = D2[2:]

        D3 = "{:04X}".format(self.D3)
        self.mem[0][6] = D3[:2]
        self.mem[0][7] = D3[2:]

        A0 = "{:04X}".format(self.A0)
        self.mem[0][8] = A0[:2]
        self.mem[0][9] = A0[2:]

        A1 = "{:04X}".format(self.A1)
        self.mem[0][10] = A1[:2]
        self.mem[0][11] = A1[2:]

        A2 = "{:04X}".format(self.A2)
        self.mem[0][12] = A2[:2]
        self.mem[0][13] = A2[2:]

        PC = "{:04X}".format(self.PC)
        self.mem[0][14] = PC[:2]
        self.mem[0][15] = PC[2:]

    def mostrar(self):
        ''' Mostra o estado atual da memória. '''

        self.atualizar_registradores()

        print("")
        print("A0: {:04X}          D0: {:04X}".format(self.A0, self.D0))
        print("A1: {:04X}          D1: {:04X}".format(self.A1, self.D1))
        print("A2: {:04X}          D2: {:04X}".format(self.A2, self.D2))
        print("PC: {:04X}          D3: {:04X}".format(self.PC, self.D3))
        print("")
        print("")
        print("          0   1   2   3   4   5   6   7   8   9   A   B   C   D   E   F")
        print("")

        num_linha = 0

        for linha_array in self.mem[1:]:
            linha = ""
            for i in linha_array:
                linha += i + "  "
            print("{:03X}0 ::  {}".format(num_linha, linha[:-2]))

            num_linha += 1


if __name__ == "__main__":
    Memoria = Inicializar_Memoria_Virtual()

    Memoria.corromper()
    Memoria.mostrar()
    Memoria.limpar()
    Memoria.mostrar()
