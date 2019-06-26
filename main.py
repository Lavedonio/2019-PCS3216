from .inicializar import *
from .interface import *
from .compilar import *
from .loader import *

import os


def main():
    run = True

    # Inicializando memória
    Memoria = Inicializar_Memoria_Virtual()

    # Carregando instruções disponíveis
    instr_set_1, rev_instr_set_1 = load_available_instructions("instruction_set_dig1.txt", multi_col=True)
    instr_set_2, rev_instr_set_2 = load_available_instructions("instruction_set_dig2.txt")

    while run:
        opcao = menu()

        # Compilar
        if opcao == "1":
            os.makedirs(os.path.join(os.getcwd(), "Arquivos_ASM"), exist_ok=True)
            arquivo = instrucoes_compilar()
            marcadores = encontrar_marcadores(arquivo, instr_set_1)
            compile(arquivo, marcadores, instr_set_1, instr_set_2)

        # Load
        elif opcao == "2":
            arquivo = instrucoes_loader()
            load(Memoria, arquivo)

        # Memória
        elif opcao == "3":
            Memoria.mostrar()

        # Run
        elif opcao == "4":
            pass

        # Sair
        else:
            run = False


if __name__ == "__main__":
    main()
