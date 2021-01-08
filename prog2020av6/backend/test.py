from config import *
from models import Computador, Usuario, LanHouse

if __name__ == "__main__":
    if os.path.exists(caminho_bd):
      os.remove(caminho_bd)

    bd.create_all()

    computador = Computador(
      processador="i7-10700K",
      ram="8GB DDR4",
      memoria="HD-500GB",
      fonte="AX1200i"
      )
    bd.session.add(computador)

    usuario = Usuario(
      nome="Cleito",
      idade=15,
      email="cleitin@email.com"
      )
    bd.session.add(usuario)

    lanhouse = LanHouse(
      nome="WanBuilding",
      endereco="Rua Ali ó",
      numero="(22) 55555-4444",
      computador=computador,
      usuario=usuario,
      )
    bd.session.add(lanhouse)

    bd.session.commit()


    print(computador)
    print(computador.json())
    print("\n")
    print(usuario)
    print(usuario.json())
    print("\n")
    print(lanhouse)
    print(lanhouse.json())