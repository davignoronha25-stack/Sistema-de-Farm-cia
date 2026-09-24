import csv

ARQUIVO = "medicamentos.csv"

def carregar_medicamentos():
    try:
        with open(ARQUIVO, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            medicamentos = []
            for medicamento in leitor:
                medicamentos["Quantidade"] = int(medicamento["Quantidade"])
                medicamentos.append(medicamento)
            return medicamentos
    except FileNotFoundError:
        return[] 

def salvar_medicamentos(medicamentos):
    with open(ARQUIVO, mode='w', newline='', encoding='utf-8') as arquivo:
        campos = ['Nome', 'Categoria', 'Quantidade']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        for medicamento in medicamentos:
<<<<<<< HEAD
            escritor.writerow(medicamento)
=======
            escritor.writerow(medicamentos)
>>>>>>> 36901240290c056176344e5f6169e6cb6500389d

def cadastrar_medicamento(medicamentos):
    print("\n==========CADASTRAR MEDICAMENTOS==========")
    nome = input("Digite o nome do medicamento: ")
    categoria = input("Digite a categoria do medicamento: ")
    quantidade = int(input("Digite a quantidade do medicamento: "))

    medicamento = {
<<<<<<< HEAD
        "Nome": nome,
        "Categoria": categoria,
        "Quantidade": quantidade
=======
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
>>>>>>> 36901240290c056176344e5f6169e6cb6500389d
    }
    medicamentos.append(medicamento)
    salvar_medicamentos(medicamentos)

    print("\nMedicamento cadastrado com sucesso!")
    return medicamentos

def listar_medicamentos(medicamentos):
    print("\n==========MEDICAMENTOS CADASTRADOS==========")
    if len(medicamentos)==0:
        print("Nenhum medicamento cadastrado.")
        return False
    for medicamento in medicamentos:
        print("------------------------")
<<<<<<< HEAD
        print("Nome: ", medicamento["Nome"])
        print("Categoria: ", medicamento["Categoria"])
        print("Quantidade: ", medicamento["Quantidade"])
=======
        print("Nome: ", medicamento["nome"])
        print("Categoria: ", medicamento["categoria"])
        print("Quantidade: ", medicamento["quantidade"])
>>>>>>> 36901240290c056176344e5f6169e6cb6500389d

    return True

def buscar_medicamento(medicamentos):
    print("\n==========BUSCAR MEDICAMENTO==========")
    termo = input("Digite o nome do medicamento que deseja buscar: ")

    encontrados = []

    for medicamento in medicamentos:
<<<<<<< HEAD
        if (termo.lower() in medicamento["Nome"].lower() or
                termo.lower() in medicamento["Categoria"].lower()):
=======
        if (termo.lower() in medicamento["nome"].lower() or
                termo.lower() in medicamento["categoria"].lower()):
>>>>>>> 36901240290c056176344e5f6169e6cb6500389d

            encontrados.append(medicamento)

    if len(encontrados)==0:
        print("Nenhum medicamento encontrado")

    else:
        print("\n=====Medicamentos Encontrados====")

        for medicamento in encontrados:
            print("------------------------------")
<<<<<<< HEAD
            print("Nome: ", medicamento["Nome"])
            print("Categoria: ", medicamento["Categoria"])
=======
            print("Nome: ", medicamento["nome"])
            print("Categoria: ", medicamento["categoria"])
>>>>>>> 36901240290c056176344e5f6169e6cb6500389d

    return encontrados

def main():
    medicamentos = carregar_medicamentos()

    while True:
        print("\n========================================")
        print("      MENU PRINCIPAL: FARMÁCIA")
        print("========================================")
        print("1- Cadastrar Medicamento")
        print("2- Listar Medicamento")
        print("3- Buscar Medicamento")
        print("4- Sair")
        print("========================================")
    
        opcao = input("\nEscolha uma opção: ")

        if opcao=="1":
            cadastrar_medicamento(medicamentos)

        elif opcao=="2":
            listar_medicamentos(medicamentos)

        elif opcao=="3":
            buscar_medicamento(medicamentos)

        elif opcao=="4":
            print("\nPrograma encerrado")
            break

        else:
            print("opção inválida")

main()