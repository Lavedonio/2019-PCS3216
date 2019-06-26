import os
import os.path


class AssemblyError(Exception):
    """Instrução não encontrada"""
    pass


def load_available_instructions(config_file, multi_col=False):
    ''' Carrega as instruções disponíveis dos arquivos "instruction_set",
        retornando um dicionário com a relação entre os mnemônicos e seus
        respectivos códigos hexadecimais.
    '''
    with open(os.path.join(os.getcwd(), "Config", config_file), "r") as file_instruction_set:
        instruction_set = {}
        reversed_instruction_set = {}
        file_instruction_set.readline()  # ignorar primeira linha

        for line in file_instruction_set:
            if multi_col:
                line_split = line[:-1].split()
                ris = line_split[:]  # copiando lista

                # instruction_set key & value
                d_key = line_split.pop(0)
                d_value = [line_split[0][1:]] + line_split[1:]
                instruction_set[d_key] = d_value

                # reversed_instruction_set key & value
                d_key = ris.pop(1)[1:]
                d_value = ris
                reversed_instruction_set[d_key] = d_value
            else:
                d_key, d_value = line[:-1].split()
                instruction_set[d_key] = d_value[1:]
                reversed_instruction_set[d_value[1:]] = d_key

    return instruction_set, reversed_instruction_set


def encontrar_marcadores(arquivo_asm, instr_set_1):
    file_path_asm = os.path.join(os.getcwd(), "Arquivos_ASM", arquivo_asm)

    # Abre o arquivo ASM em modo de leitura
    with open(file_path_asm, "r") as file_ASM:
        memoria = 0
        marcadores = {}

        # Lê linha por linha do ASM
        for line_asm in file_ASM:

            # Se não houver nada na linha, pula para a próxima
            if len(line_asm) > 0:
                instr_asm = line_asm[:-1].split()  # Separa as instruções, ignora o \n

                # Se não começa com ' lê o que tá na linha (' denomina comentário)
                if instr_asm[0][0] != "'":
                    if len(instr_asm) > 1:

                        # Instrução especial org que seta o valor inicial onde será escrito o valor na memória
                        if instr_asm[0] == "org":
                            memoria = int(instr_asm[1], 16)

                        # Se instrução não existe, o compilador falha
                        elif instr_asm[0] not in instr_set_1 and instr_asm[1] not in instr_set_1:
                            raise(AssemblyError)

                        # Se o primeiro argumento existe, passa para o próximo teste
                        elif instr_asm[0] in instr_set_1:
                            pass

                        # Se o primeiro argumento não existe, então ele é um marcador (para uma instrução jump)
                        else:
                            pass
    return marcadores


def compile(arquivo_asm, marcadores, instr_set_1, instr_set_2):
    os.makedirs(os.path.join(os.getcwd(), "Arquivos_HEX"), exist_ok=True)
    arquivo_hex = arquivo_asm[:-4] + ".hex"

    file_path_asm = os.path.join(os.getcwd(), "Arquivos_ASM", arquivo_asm)
    file_path_hex = os.path.join(os.getcwd(), "Arquivos_HEX", arquivo_hex)

    # Abre ambos os arquivos, o ASM em modo de leitura e o HEX em modo de escrita
    with open(file_path_asm, "r") as file_ASM, open(file_path_hex, "w") as file_HEX:
        instr_hex = ""
        mem_start = "0"
        file_HEX.write("OpStart: {} ".format(mem_start))

        # Lê linha por linha do ASM
        for line_asm in file_ASM:
            linha_hex = ""

            # Se não houver nada na linha, pula para a próxima
            if len(line_asm) > 0:
                instr_asm = line_asm[:-1].split()  # Separa as instruções, ignora o \n

                # Se não começa com ' lê o que tá na linha (' denomina comentário)
                if instr_asm[0][0] != "'":
                    if len(instr_asm) > 1:

                        # Instrução especial org que seta o valor inicial onde será escrito o valor na memória
                        if instr_asm[0] == "org":
                            mem_start = instr_asm[1]
                            file_HEX.write("\nOpStart: {} ".format(mem_start))

                        # Se instrução não existe, o compilador falha
                        elif instr_asm[0] not in instr_set_1 and instr_asm[0] not in marcadores:
                            raise(AssemblyError)

                        # Se o primeiro argumento existe, passa para o próximo teste
                        elif instr_asm[0] in instr_set_1:
                            pass

                        # Se o primeiro argumento não existe, então ele é um marcador (para uma instrução jump)
                        else:
                            pass


def teste():
    instr_set_1, rev_instr_set_1 = load_available_instructions("instruction_set_dig1.txt", multi_col=True)
    print("\ninst_set1: {}\n\nrev_inst_set1: {}".format(instr_set_1, rev_instr_set_1))

    instr_set_2, rev_instr_set_2 = load_available_instructions("instruction_set_dig2.txt")
    print("\ninst_set2: {}\n\nrev_inst_set2: {}".format(instr_set_2, rev_instr_set_2))

    os.makedirs(os.path.join(os.getcwd(), "Arquivos_ASM"), exist_ok=True)
    os.makedirs(os.path.join(os.getcwd(), "Arquivos_HEX"), exist_ok=True)


if __name__ == "__main__":
    teste()
