### Construção do aplicativo Sabor Express utilizando o paradigma de OO ###

from modelos.avaliacao import Avaliacao

class Restaurante:
  """Representa um restaurante e suas características"""

  restaurantes = []

  # __init__() é o método construtor e é chamado automaticamente quando uma nova instância é criada. O self é uma convenção usada para representar a instância atual da classe e permite acessar e manipular os atributos e métodos da própria instância. É similar ao this no Java
  def __init__(self, nome, categoria):
    """
        Inicializa uma instância de Restaurante

        Parâmetros:
        - nome (str): O nome do restaurante
        - categoria (str): A categoria do restaurante
    """
    self._nome = nome.title() # O title() transforma a primeira letra da string em maiúsculo
    self._categoria = categoria
    self._ativo = False # Ao adicionar o underline, o atributo passa a ser protegido, pois o valor dele não será alterado pelo o usuário
    self._avaliacao = []

    Restaurante.restaurantes.append(self) # Adiciona o novo objeto/restaurante na lista restaurantes

  # O __str__() é um método especial que apresenta os objetos em formato de texto
  def __str__(self):
    """Retorna uma representação em string do restaurante"""
    return f'{self._nome} | {self._categoria}'
  
  @classmethod # O @classmethod é um decorator usado para métodos da classe, ou seja, métodos que fazem referência a própria classe
  def listar_restaurantes(cls): # O 'cls' é uma convenção que faz referência a classe
    """Exibe uma lista formatada de todos os restaurantes"""
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | Status')
    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

  @property # O @property é um decorator usado quando queremos pegar um atributo e modificar a forma de como ele vai ser lido
  def ativo(self):
    """Retorna um símbolo indicando o estado de atividade do restaurante"""
    return 'Ativado' if self._ativo else 'Desativado'

  def alternar_estado(self):
    """Alterna o estado de atividade do restaurante"""
    self._ativo = not self._ativo

  def receber_avaliacao(self, cliente, nota):
    """
        Registra uma avaliação para o restaurante

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5)
    """
    if 0 < nota <= 5:
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)

  @property
  def media_avaliacoes(self):
    """Calcula e retorna a média das avaliações do restaurante"""
    if not self._avaliacao:
      return 'Sem avaliação'
    
    soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) # Pega todas as avaliações da lista avaliacao[] e para cada avaliacao, pegue o item/a propriedade nota e faça a soma delas
    quantidade_de_notas = len(self._avaliacao)
    media = round(soma_das_notas / quantidade_de_notas, 1)
    return media