### Construção do aplicativo Sabor Express utilizando o paradigma POO ###

class Restaurante:
  restaurantes = []

  def __init__(self, nome, categoria): # __init__() é o método construtor. O self é uma convenção usada para representar a instância atual da classe e permite acessar e manipular os atributos e métodos da própria instância. É similar ao this no Java
    self.nome = nome
    self.categoria = categoria
    self.ativo = False

    Restaurante.restaurantes.append(self)

  def __str__(self): # O __str__() é um método especial que apresenta os objetos em formato de texto
    return f'{self.nome} | {self.categoria}'
  
  def listar_restaurantes():
    for restaurante in Restaurante.restaurantes:
      print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Comida Brasileira')
restaurante_pizza = Restaurante('Pizzaria Central', 'Italiana')

Restaurante.listar_restaurantes()