import os


def load(Memoria, arquivo_hex):
    ''' Carrega o conteúdo do arquivo .hex na memória. '''

    file_path_hex = os.path.join(os.getcwd(), "Arquivos_HEX", arquivo_hex)

    # Abre ambos os arquivos, o ASM em modo de leitura e o HEX em modo de escrita
    with open(file_path_hex, "r") as file_HEX:
        primeiro_cmd = True
        for linha in file_HEX:
            conteudo = linha.split()

            if len(conteudo) > 2:
                PC = int(conteudo[1], 16)

                if primeiro_cmd:
                    Memoria.PC = PC
                    Memoria.atualizar_memoria()
                    primeiro_cmd = False

                for instr in conteudo[2:]:
                    Memoria.mem[(PC // 16) + 1][PC % 16] = instr
                    PC += 1


if __name__ == "__main__":
    from inicializar import *

    Memoria = Inicializar_Memoria_Virtual()
    load(Memoria, "soma.hex")
    Memoria.mostrar()
