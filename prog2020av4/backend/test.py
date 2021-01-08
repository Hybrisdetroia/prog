from config import *
from models import Computador

if __name__ == "__main__":
    if os.path.exists(caminho_bd):
      os.remove(caminho_bd)

    bd.create_all()

    computador1 = Computador(
      processador="i7-10700K",
      ram="8GB DDR4",
      memoria="HD-500GB",
      fonte="AX1200i"
      )
    bd.session.add(computador1)

    computador2 = Computador(
      processador="i3-5100K",
      ram="4GB DDR3",
      memoria="HD-250GB",
      fonte="VS500"
      )
    bd.session.add(computador2)

    computador3 = Computador(
      processador="i5-7400",
      ram="12GB DDR4",
      memoria="HD-1TB",
      fonte="AX1200i"
      )
    bd.session.add(computador3)

    computador4 = Computador(
      processador="i9-10900K",
      ram="32GB DDR4",
      memoria="SSD-2TB",
      fonte="VTC800"
      )
    bd.session.add(computador4)

    computador5 = Computador(
      processador="i7-8700",
      ram="8GB DDR3",
      memoria="HD-1TB",
      fonte="EVGA400"
      )
    bd.session.add(computador5)

    bd.session.commit()