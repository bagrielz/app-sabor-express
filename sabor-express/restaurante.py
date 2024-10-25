### Construção do aplicativo Sabor Express em Python ###

import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},{'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True}, {'nome': 'Cantina', 'categoria': 'Brasileira', 'ativo': False}]

def exibir_nome_do_programa():
  ''' Exibe o nome estilizado do programa na tela '''

  print('Sabor Express\n')

def exibir_opcoes():
  ''' Exibe as opções disponíveis no menu principal '''

  print('1. Cadastrar restaurante')
  print('2. Listar restaurantes')
  print('3. Alternar o estado do restaurante')
  print('4. Sair\n')

def finalizar_app():
  ''' Exibe mensagem de finalização do aplicativo '''

  exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
  '''
  Solicita uma tecla para voltar ao menu principal 
    
  Outputs:
  - Retorna ao menu principal
  '''

  input('\nDigite uma tecla para voltar ao menu principal')
  main()

def opcao_invalida():
  '''
  Exibe mensagem de opção inválida e retorna ao menu principal 
    
  Outputs:
  - Retorna ao menu principal
  '''
  
  print('Opção inválida!')
  voltar_ao_menu_principal()

def exibir_subtitulo(texto):
  '''
  Exibe um subtítulo estilizado na tela 
    
  Inputs:
  - texto: str - O texto do subtítulo
  '''
  os.system('cls')
  print(texto)
  print()

def cadastrar_novo_restaurante():
  '''
  Essa função é responsável por cadastrar um novo restaurante
  
  Inputs:
  - Nome do restaurante
  - Categoria
  
  Outputs:
  - Adiciona um novo restaurante a lista de restaurantes
  '''

  exibir_subtitulo('Cadastro de novos restaurantes')
  nome = input('Digite o nome do restaurante que deseja cadastrar: ')
  categoria = input(f'Digite o nome da categoria do restaurante {nome}: ')
  dados = {'nome': nome, 'categoria': categoria, 'ativo': False}

  restaurantes.append(dados)
  print(f'O restaurante {nome} foi cadastrado com sucesso!')
  voltar_ao_menu_principal()

def listar_restaurantes():
  '''Lista os restaurantes presentes na lista 
    
  Outputs:
  - Exibe a lista de restaurantes na tela
  '''
  
  exibir_subtitulo('Lista de restaurantes')

  print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

  for restaurante in restaurantes:
    ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
    print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {ativo}')
  voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
  '''
  Altera o estado ativo/desativado de um restaurante 
    
  Outputs:
  - Exibe mensagem indicando o sucesso da operação
  '''

  exibir_subtitulo('Alterar o estado do restaurante')
  
  nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
  restaurante_encontrado = False

  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo']
      mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)

  if not restaurante_encontrado:
    print('O restaurante não foi encontado')
    
  voltar_ao_menu_principal()

def escolher_opcao():
  '''
  Solicita e executa a opção escolhida pelo usuário 
    
  Outputs:
  - Executa a opção escolhida pelo usuário
  '''
  
  # O try e o except tratam um erro de execução, como o input está recebendo um valor inteiro, se o usuário digitar uma string, o erro de execução vai acontecer, mas não vai quebrar o código, permitindo a gente voltar para a tela inicial e testar novamente
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      alternar_estado_do_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app();
    else:
      opcao_invalida()
  except:
    opcao_invalida()

  # Outra forma
  # opcao_escolhida = int(input('Escolha uma opção: '))
  # match opcao_escolhida:
  #     case 1:
  #         print('Adicionar restaurante')
  #     case 2:
  #         print('Listar restaurantes')
  #     case 3:
  #         print('Ativar restaurante')
  #     case 4:
  #         print('Finalizar app')
  #     case _:
  #         print('Opção inválida!')

def main():
  ''' Função principal que inicia o programa '''
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()