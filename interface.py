def menu():
    print("Selecione a operação desejada:\n")
    print("1. (COMPILE) Compilar um programa Assembly em hex")
    print("2.  (LOAD)   Carregar um programa hex na memória")
    print("3.  (RUN)    Rodar programa na memória")
    print("x.  (EXIT)   Sair")
    return input("Operação: ")


def instrucoes_compilar():
    print("Coloque o arquivo .asm no mesmo diretório que este programa.")
    print("Pressione ENTER para continuar...")
    input()


def teste():
    print("Teste da função menu():")
    print(menu())


if __name__ == "__main__":
    teste()
