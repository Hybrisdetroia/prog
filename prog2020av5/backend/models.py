from config import bd


class Computador(bd.Model):
  id = bd.Column(bd.Integer, primary_key=True)
  processador = bd.Column(bd.String(256))
  ram = bd.Column(bd.String(256))
  memoria = bd.Column(bd.String(256))
  fonte = bd.Column(bd.String(256))


  def __str__(self):
    return f'{self.id}. {self.processador}; {self.ram}; {self.memoria}; {self.fonte}'


  def json(self):
    return {
      "id": self.id,
      "processador": self.processador,
      "ram": self.ram,
      "memoria": self.memoria,
      "fonte": self.fonte,
    }


class Usuario(bd.Model):
  id = bd.Column(bd.Integer, primary_key=True)
  nome = bd.Column(bd.String(256))
  idade = bd.Column(bd.Integer)
  email = bd.Column(bd.String(256))


  def __str__(self):
    return f'{self.id}. {self.nome}; {self.idade}; {self.email}.'


  def json(self):
    return {
      "id": self.id,
      "nome": self.nome,
      "idade": self.idade,
      "email": self.email,
    }


class LanHouse(bd.Model):
  id = bd.Column(bd.Integer, primary_key=True)
  nome = bd.Column(bd.String(256))
  endereco = bd.Column(bd.Integer)
  numero = bd.Column(bd.String(256))

  computador_id = bd.Column(bd.Integer, bd.ForeignKey(Computador.id), nullable=False)
  computador = bd.relationship("Computador")

  usuario_id = bd.Column(bd.Integer, bd.ForeignKey(Usuario.id), nullable=False)
  usuario = bd.relationship("Usuario")


  def __str__(self):
    return f'{self.id}. {self.nome}; {self.endereco}; {self.numero}.' +\
    f'Computador: {self.computador_id}. {self.computador}' +\
    f'Usuario: {self.usuario_id}. {self.usuario}'


  def json(self):
    return {
      "id": self.id,
      "nome": self.nome,
      "endereco": self.endereco,
      "numero": self.numero,
      "computador_id": self.computador_id,
      "computador": self.computador.json(),
      "usuario_id": self.usuario_id,
      "usuario": self.usuario.json(),
    }