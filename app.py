import database

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Inserir novo usuário")
        print("2 - Listar usuários")
        print("3 - Deletar usuário")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            email = input("Digite o e-mail: ")
            database.insert_user(nome, idade, email)
            print("Usuário cadastrado com sucesso!")

        elif escolha == '2':
            users = database.fetch_users()
            if users:
                print("\n--- Lista de Usuários ---")
                for user in users:
                    print(f"ID: {user[0]} | Nome: {user[1]} | Idade: {user[2]} | Email: {user[3]} | Criado em: {user[4]}")
            else:
                print("Nenhum usuário encontrado.")

        elif escolha == '3':
            user_id = int(input("Digite o ID do usuário que deseja deletar: "))
            database.delete_user(user_id)
            print("Usuário deletado com sucesso!")

        elif escolha == '0':
            print("Saindo... Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    database.create_table()
    menu()
