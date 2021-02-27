''' Programa para uma rede de academia de ginástica '''

import os
import time 
import pandas as pd

class Pessoa():
    # Método Construtor
    def __init__(self, nome, cpf, idade, alt, peso, sts, plano):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.altura = alt
        self.peso = peso
        self.status = sts
        self.plano = plano

    # Métodos Especiais gets e sets
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getCpf(self):
        return self.cpf
    def setCpf(self, cpf):
        self.cpf = cpf

    def getIdade(self):
        return self.idade
    def setIdade(self, idade):
        self.idade = idade
    
    def getAltura(self):
        return self.altura
    def setAltura(self, alt):
        self.altura = alt

    def getPeso(self):
        return self.peso
    def setPeso(self, peso):
        self.peso = peso
    
    def getStatus(self):
        return self.status
    def setStatus(self, sts):
        self.status = sts
    
    def getPlanoAluno(self):
        return self.plano
    def setPlanoAluno(self, plan):
        self.plano = plan



class Pacotes():
    # Método Construtor
    def __init__(self, plano):
        self.plano = plano

    # Métodos Especiais gets e sets
    def getPlano(self):
        return self.plano
    def setPlano(self, plano):
        self.plano.append(plano)


class Sistema():
    # iniciando listas vazias
    nomelista = []
    cpflista = []
    idadelista = []
    alturalista = []
    pesolista = []
    statuslista = []
    planolista = []
    contadorAtivo = 0
    contadorNaoAtivo = 0

    def __init__(self):
        self.dic_aluno = {}


    def cabecalho(self):
        print('==================================================================\n\t\t\tSISTEMA DE ACADEMIA\n==================================================================\n\n')
        
    def menuInicial(self):
        print('\n1 - Cadastrar Aluno\n2 - lista de aluno matriculados\n3 - Alunos ativos e não ativos\n0 - Sair\n')

    def ativo(self):
        Sistema.contadorAtivo = Sistema.contadorAtivo + 1

    def naoAtivo(self):
        Sistema.contadorNaoAtivo = Sistema.contadorNaoAtivo + 1
    
    def getAtivo(self):
        return self.contadorAtivo
    def getNaoAtivo(self):
        return self.contadorNaoAtivo

    def BDAlunos(self, n,c,i,a,p,s,pl):
        # inserindo dados nas listas
        Sistema.nomelista.append(n)
        Sistema.cpflista.append(c)
        Sistema.idadelista.append(i)
        Sistema.alturalista.append(a)
        Sistema.pesolista.append(p)
        Sistema.statuslista.append(str(s))
        Sistema.planolista.append(pl)
        
    def listarAlunos(self):
        if Sistema.nomelista == [] and Sistema.cpflista  == [] and Sistema.idadelista == [] and Sistema.alturalista == [] and Sistema.pesolista == [] and Sistema.statuslista == [] and Sistema.planolista == []:
            print('Nenhum Aluno cadastrado. :(')
        else:
            #Criando o DataFrame com os dados dos alunos cadastrados
            self.dic_aluno = {'Aluno': Sistema.nomelista,
                'CPF': Sistema.cpflista,
                'Idade': Sistema.idadelista,
                'Altura': Sistema.alturalista,
                'Peso': Sistema.pesolista,
                'Status': Sistema.statuslista,
                'Plano': Sistema.planolista}
                
            planilha = pd.DataFrame(self.dic_aluno)
            print(planilha)
            
    def menuPlano(self):
        print('\n1 - PlanoA\n2 - PlanoB\n3 - PlanoC\n') 




# ------------------------- Programa Pricipal -------------------------
stop = 2
while stop != 0:
    os.system('cls')  # limpando a tela
    sistema = Sistema() # instanciando um objeto (objeto sistema é uma instacia da classe Sistema)
    sistema.cabecalho() # chamando o cabeçalho do sistema 
    sistema.menuInicial() # chamando o menu inicial do sistema
    opcao = input('Digite o número da opção que deseja: ') # pedindo ao usuário uma entrada

    if opcao != '0' and opcao != '1' and opcao != '2' and opcao != '3': # primeira condição para a entrada do usuário
        print('Opção inválida!\nTente novamente')
        time.sleep(2) # programa espera 2 segundos
    if opcao == '1': # cadastro - segunda condição para a entrada do usuário
        os.system('cls')
        sistema.cabecalho()
        print('-------- CADASTRO ------------------------------------------------\n')
        # entradas
        nome = input(str('Nome completo do aluno: '))
        cpf = input(str('CPF: '))
        idade = input(str('Idade: '))
        alt = input(str('Altura: '))
        peso = input(str('Peso: '))
        sts = input('Status do aluno:\n(Digite 1 para Ativo ou 2 para não ativo): ')
        # condições para a entrada do status
        while sts != '1' and sts != '2':
            print('Opção inválida!\nTente novamente')
            time.sleep(2) # programa espera 2 segundos
            sts = input('Status do aluno:\n(Digite 1 para Ativo ou 2 para não ativo): ')
        if sts == '1':
            sts = True
            sistema.ativo()
        elif sts == '2':
            sts = False
            sistema.naoAtivo()
        
        sistema.menuPlano() # chamando o menu dos planos

        pla = input('Plano do aluno (Informe um número de um plano acima): ')
        # condições para a entrada do plano
        while pla != '1' and pla != '2' and pla != '3':
            print('Opção inválida!\nTente novamente')
            time.sleep(2) # programa espera 2 segundos
            pla = input('Plano do aluno (Informe um número de um plano acima): ')
        if pla == '1':
            pla = 'PlanoA'
        elif pla == '2':
            pla = 'PlanoB'
        elif pla == '3':
            pla = 'PlanoC'
        
        # instanciando objetos
        planoDoPacote = Pacotes(pla) 
        aluno = Pessoa(nome, cpf, idade, alt, peso, sts, planoDoPacote.plano)
        # chamando o banco de dados dos alunos e passando resultados de métodos como parâmetros
        print(aluno.getNome(), aluno.getCpf(), aluno.getIdade(), aluno.getAltura(), aluno.getPeso(), aluno.getStatus(), aluno.getPlanoAluno())
        sistema.BDAlunos(aluno.getNome(), aluno.getCpf(), aluno.getIdade(), aluno.getAltura(), aluno.getPeso(), aluno.getStatus(), aluno.getPlanoAluno())
        os.system('pause') # pausando o programa
        os.system('cls')
        print('ALUNO CADASTRADO COM SUCESSO! :)\n\n')
        cont_stop = input('Digite 1 para voltar ao Menu ou 0 para encerrar o sistema: ')
        # condições para parar o programa ou não
        while cont_stop != '0' and cont_stop != '1':
            print('Opção inválida!\nTente novamente')
            time.sleep(2) # programa espera 2 segundos
            cont_stop = input('Digite 1 ou 0: ')
        if int(cont_stop) == 1:
            # os.system('Pause')
            pass
        elif int(cont_stop) == 0:
            stop = 0
            print('\nPrograma Finalizado!')
            time.sleep(1)
            os.system('Pause')
    elif opcao == '2': # listar os alunos - terceira condição para a entrada do usuário
        os.system('cls')
        sistema.cabecalho()
        print('-------- ALUNOS CADASTRADOS -------------------------------------\n')
        sistema.listarAlunos() # chamando a lista de alunos
        cont_stop = input('\nDigite 1 para voltar ao Menu ou 0 para encerrar o sistema: ')
        # condições para parar o programa ou não
        while cont_stop != '0' and cont_stop != '1':
            print('Opção inválida!\nTente novamente')
            time.sleep(2) # programa espera 2 segundos
            cont_stop = input('Digite 1 ou 0: ')
        if int(cont_stop) == 1:
            # os.system('Pause')
            time.sleep(2)
        elif int(cont_stop) == 0:
            stop = 0
            print('\nPrograma Finalizado!')
            time.sleep(1)
            os.system('Pause')
    elif opcao == '3': # contagem de ativos e não ativos - quarta condição para a entrada do usuário
        os.system('cls')
        sistema.cabecalho()
        print('-------- ALUNOS ATIVOS E NÃO ATIVOS -----------------------------\n')
        print('Quantidade de alunos ATIVOS: {}'.format(sistema.getAtivo()))
        print('Quantidade de alunos NÃO ATIVOS: {}'.format(sistema.getNaoAtivo()))
        os.system('Pause')
    elif opcao == '0': # sair - quinta condição para a entrada do usuário
        stop = 0
        print('\nPrograma Finalizado!')
        time.sleep(1)
        os.system('Pause')