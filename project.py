banco_de_dados = []
matricula_atual = 0

def criarAluno(nome, idade, curso):
    # Permite alterar o valor de uma variavel global
    global matricula_atual
    matricula_atual += 1
    # Criando um aluno através de um dicionário
    aluno = {
        'matricula': matricula_atual,
        'nome': nome,
        'idade': idade,
        'curso': curso
    }
    return aluno

def adicionarAluno(nome, idade, curso):
    aluno = criarAluno(nome, idade, curso)
    banco_de_dados.append(aluno)
    print('Aluno adicionado com sucesso!')

def listarAlunos():
    print('----------Alunos matriculados-------')
    for aluno in banco_de_dados:
        print(f"Matricula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print('------------------------------\n')

def editarAluno(matricula, nome, idade, curso):
    aluno = alunoExiste(matricula)
    if aluno:
        aluno['nome'] = nome
        aluno['idade'] = idade
        aluno['curso'] = curso
        print('Dados alterados com sucesso!')
    else:
        print('Matricula não encontrada!')

def alunoExiste(matricula):
    for aluno in banco_de_dados:
        if aluno['matricula'] == matricula:
            return aluno
    return False

def removerAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
        banco_de_dados.remove(aluno)
        print('Aluno removido com sucesso!')
    else:
        print('Aluno não encontrado!')

def consultarAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
        print('-----Dados do Aluno------')
        print(f"Matricula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print('------------------------------\n')
    else:
        print('Matricula não encontrada!')

def menu():
    while True:
        print('-------BEM VINDO AO MENU ESCOLAR--------------')
        print('1 - Adicionar aluno')
        print('2 - Editar aluno')
        print('3 - Remover aluno')
        print('4 - Buscar aluno')
        print('5 - Listar todos os alunos')
        print('6 - Sair do sistema')
        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            nome = input('Digite o nome: ')
            idade = int(input('Digite a idade: '))
            curso = input('Digite o curso: ')
            adicionarAluno(nome, idade, curso)
        elif opcao == '2':
            matricula = int(input('Digite a matricula: '))
            nome = input('Digite o nome: ')
            idade = int(input('Digite a idade: '))
            curso = input('Digite o curso: ')
            editarAluno(matricula, nome, idade, curso)
        elif opcao == '3':
            matricula = int(input('Digite a matricula: '))
            removerAluno(matricula)
        elif opcao == '4':
            matricula = int(input('Digite a matricula: '))
            consultarAluno(matricula)
        elif opcao == '5':
            listarAlunos()
        elif opcao == '6':
            break
        else:
            print('Opção Inválida')

menu()

# adicionarAluno('Luis', 19, 'Python')
# adicionarAluno('Paulo', 23, 'Java')
# adicionarAluno('Rebeca', 39, 'HTML')
# adicionarAluno('Carla', 15, 'CSS')
#print(banco_de_dados)
#listarAlunos()
#editarAluno(1, 'Luis Silva', 25, 'React')
#editarAluno(5, 'Fernanda', 25, 'Python')
#listarAlunos()
#alunoExiste()
#removerAluno(4)
#listarAlunos()
#consultarAluno(2)