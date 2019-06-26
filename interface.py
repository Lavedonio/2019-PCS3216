def menu():
    print("Selecione a operação desejada:\n")
    print("1. (COMPILE) Compilar um programa Assembly em hex")
    print("2.  (LOAD)   Carregar um programa hex na memória")
    print("3.  (MEM)    Olhar estado atual da memória")
    print("4.  (RUN)    Rodar programa na memória")
    print("x.  (EXIT)   Sair")
    return input("Operação: ")


def instrucoes_compilar():
    print("")
    print("Coloque o arquivo .asm no diretório \"Arquivos_ASM\".")
    print("Pressione ENTER para continuar...")
    input()
    return input("Digite o nome do arquivo (com extensão .asm): ")


def instrucoes_loader():
    print("")
    return input("Digite o nome do arquivo (com extensão .hex): ")


def teste():
    print("Teste da função menu():")
    print(menu())
    print("")
    print("Teste da função instrucoes_compilar():")
    print(instrucoes_compilar())
    print("Teste da função instrucoes_loader():")
    print(instrucoes_loader())

if __name__ == "__main__":
    teste()
