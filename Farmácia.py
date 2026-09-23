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
            escritor.writerow(medicamentos)

def cadastrar_medicamento(medicamentos):
    print("\n==========CADASTRAR MEDICAMENTOS==========")
    nome = input("Digite o nome do medicamento: ")
    categoria = input("Digite a categoria do medicamento: ")
    quantidade = int(input("Digite a quantidade do medicamento: "))

    medicamento = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
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
        print("Nome: ", medicamento["nome"])
        print("Categoria: ", medicamento["categoria"])
        print("Quantidade: ", medicamento["quantidade"])

    return True

def buscar_medicamento(medicamentos):
    print("\n==========BUSCAR MEDICAMENTO==========")
    termo = input("Digite o nome do medicamento que deseja buscar: ")

    encontrados = []

    for medicamento in medicamentos:
        if (termo.lower() in medicamento["nome"].lower() or
                termo.lower() in medicamento["categoria"].lower()):

            encontrados.append(medicamento)

    if len(encontrados)==0:
        print("Nenhum medicamento encontrado")

    else:
        print("\n=====Medicamentos Encontrados====")

        for medicamento in encontrados:
            print("------------------------------")
            print("Nome: ", medicamento["nome"])
            print("Categoria: ", medicamento["categoria"])

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