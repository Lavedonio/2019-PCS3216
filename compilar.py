import os
import os.path


class AssemblyError(Exception):
    """Instrução não encontrada"""
    pass


def load_available_instructions(config_file):
    ''' Carrega as instruções disponíveis dos arquivos "instruction_set",
        retornando um dicionário com a relação entre os mnemônicos e seus
        respectivos códigos hexadecimais.
    '''
    with open(os.path.join(os.getcwd(), "Config", config_file), "r") as file_instruction_set:
        instruction_set = {}
        file_instruction_set.readline()  # ignorar primeira linha

        for line in file_instruction_set:
            d_key, d_value = line[:-1].split()
            instruction_set[d_key] = d_value[1:]

    return instruction_set


def compile(arquivo_asm, instr_set_1, instr_set_2):
    os.makedirs(os.path.join(os.getcwd(), "Arquivos_HEX"), exist_ok=True)
    arquivo_hex = arquivo_asm[:-4] + ".hex"

    file_path_asm = os.path.join(os.getcwd(), "Arquivos_ASM", arquivo_asm)
    file_path_hex = os.path.join(os.getcwd(), "Arquivos_ASM", arquivo_hex)

    # Abre ambos os arquivos, o ASM em modo de leitura e o HEX em modo de escrita
    with open(file_path_asm, "r") as file_ASM, open(file_path_hex, "w") as file_HEX:
        instr_hex = ""
        mem_start = "0"

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

                        # Se instrução não existe, o compilador falha
                        elif instr_asm[0] not in instr_set_1 and instr_asm[1] not in instr_set_1:
                            raise(AssemblyError)

                        # Se o primeiro argumento existe, passa para o próximo teste
                        elif instr_asm[0] in instr_set_1:
                            pass


def teste():
    print("\ninst_set1: {}".format(load_available_instructions("instruction_set_dig1.txt")))
    print("\ninst_set2: {}".format(load_available_instructions("instruction_set_dig2.txt")))


if __name__ == "__main__":
    teste()
