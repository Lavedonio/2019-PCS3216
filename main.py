from .inicializar import *
from .interface import *
from .compilar import *

import os


def main():
    run = True

    while run:
        opcao = menu()

        # Compilar
        if opcao == "1":
            os.makedirs(os.path.join(os.getcwd(), "Arquivos_ASM"), exist_ok=True)
            arquivo = instrucoes_compilar()
            instr_set_1 = load_available_instructions("instruction_set_dig1.txt")
            instr_set_2 = load_available_instructions("instruction_set_dig2.txt")
            compile(arquivo, instr_set_1, instr_set_2)

        # Load
        elif opcao == "2":
            pass

        # Memória
        elif opcao == "3":
            pass

        # Run
        elif opcao == "4":
            pass

        # Sair
        else:
            run = False


if __name__ == "__main__":
    main()
