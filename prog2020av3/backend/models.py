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
