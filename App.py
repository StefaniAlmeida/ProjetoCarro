from Carro import Carro
from Hibrido import Hibrido

def main():
    carro1 = Carro( "Branco", "Esportivo", 2015)
    print(carro1)

    carro2 = Carro("Preto", "Trilha", 2016)
    print(carro2)

    carro3 = carro1
    carro3.cor = "Preto"
    print(carro3)

if __name__ == "__main__":
    main()
