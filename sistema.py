import sys
import string

print("======== SISTEMA DE INSCRIÇÕES ========")

opcao = ''
usuarios = [{"nome": "João Silva", "email": "joaosilva@email.com"}]

def mostrar_menu():
    print ("\n O que deseja fazer?\n")

    print("1. Novo cadastro")
    print("2. Listar usuários por ordem de cadastro")
    print("3. Listar usuários por ordem alfabética")
    print("4. Buscar usuário por nome")
    print("5. Remover usuário cadastrado")
    print("6. Alterar nome de um usuário")
    print("7. Fechar")

    global opcao
    opcao = input("\nDigite o número correspondente a ação que deseja realizar: ")

mostrar_menu()

def cadastro():
    nome = input("\nDigite o nome completo do usuário: ")
    email = input ("Digite o email do usuário: ")

    nome_maiusculo = string.capwords(nome)

    usuarios.append({'nome': nome_maiusculo, 'email': email})

    print("\n-------- USUÁRIO CADASTRADO COM SUCESSO -------- ")
    mostrar_menu()

def mostrar_usuarios_por_cadastro():
    for usuario in usuarios:
        print("Nome: " + usuario['nome'] + "  Email: " + usuario['email']) 
    mostrar_menu()

def encerrar():
    sys.exit()

def default():
    print("\nOPÇÃO INVÁLIDA")
    mostrar_menu()

while True:
    if opcao == "1":
        cadastro()
    elif opcao == "2": 
        mostrar_usuarios_por_cadastro()
    elif opcao == "3":
        mostrar_usuarios_por_ordem_alfabetica()
    elif opcao == "4":
        buscar_usuario_pelo_nome()
    elif opcao == "5":
        remover_usuario_por_email()
    elif opcao == "6":
        alterar_nome_por_email()
    elif opcao == "7":
        encerrar()
    else:
        default()