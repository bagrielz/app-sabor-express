### Construção do aplicativo Sabor Express utilizando o paradigma de OO ###

class Restaurante:
  restaurantes = []

  # __init__() é o método construtor e é chamado automaticamente quando uma nova instância é criada. O self é uma convenção usada para representar a instância atual da classe e permite acessar e manipular os atributos e métodos da própria instância. É similar ao this no Java
  def __init__(self, nome, categoria): 
    self._nome = nome.title() # O title() transforma a primeira letra da string em maiúsculo
    self._categoria = categoria
    self._ativo = False # Ao adicionar o underline, o atributo passa a ser protegido, pois o valor dele não será alterado pelo o usuário

    Restaurante.restaurantes.append(self) # Adiciona o novo objeto/restaurante na lista restaurantes

  # O __str__() é um método especial que apresenta os objetos em formato de texto
  def __str__(self):
    return f'{self._nome} | {self._categoria}'
  
  @classmethod # O @classmethod é um decorator usado para métodos da classe, ou seja, métodos que fazem referência a própria classe
  def listar_restaurantes(cls): # O 'cls' é uma convenção que faz referência a classe
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')

  @property # O @property é um decorator usado quando queremos pegar um atributo e modificar a forma de como ele vai ser lido
  def ativo(self):
    return 'Ativado' if self._ativo else 'Desativado'

  def alternar_estado(self):
    self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Comida Brasileira')
restaurante_praca.alternar_estado()

restaurante_pizza = Restaurante('Pizzaria Central', 'Italiana')

Restaurante.listar_restaurantes()